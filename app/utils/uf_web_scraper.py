import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException
import os

class SIIUFWebScraper:
    def __init__(self, year):
        url = os.getenv('SII_UF_URL')
        self.year = year
        self.url = url.format(year=year)

    def get_uf_soup(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=f"An error has occurred while trying to obtain the units of fomento. {e}")

    def create_uf_data(self, rows):
        try:
            data = {}
            for row in rows:
                cols = row.findAll('td')
                for i, col in enumerate(cols):
                    date_key = f'{self.year}-{i + 1:02d}-{int(row.find("th").text):02d}'
                    row_value = col.text
                    if not row_value.isspace():
                        data[date_key] = row_value
            return data
        except (ValueError, IndexError) as e:
            raise HTTPException(status_code=500, detail=f"An error has occurred creating the data: {e}")


    def get_uf_data(self):
        soup = self.get_uf_soup()
        uf_export_table = soup.find('table', {'id': 'table_export'})
        uf_rows = uf_export_table.find_all('tr')
        return self.create_uf_data(uf_rows)