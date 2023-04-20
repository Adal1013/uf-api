from app.utils.uf_web_scraper import SIIUFWebScraper
from fastapi import HTTPException

class UFService:
    @staticmethod
    def get_ufs_data_by_year(year):
        uf_web_scraper = SIIUFWebScraper(year)
        return uf_web_scraper.get_uf_data()

    @staticmethod
    def get_uf_data_by_date(date):
        uf_data = UFService.get_ufs_data_by_year(date.year)
        try:
            return uf_data[date.strftime("%Y-%m-%d")]
        except KeyError:
            raise HTTPException(status_code=404, detail="There is no fomento unit for that date.")