from fastapi import HTTPException, Path
from datetime import date, datetime

class Validate:
    @staticmethod
    def validate_year(uf_year: str = Path(..., regex=r'^\d{4}$')) -> str:
        today = date.today()
        if int(uf_year) < 2013 or int(uf_year) > today.year:
            raise HTTPException(status_code=400, detail="The year must be within the range of 2013 to current year")
        return uf_year

    @staticmethod
    def validate_date(uf_date: str) -> date:
        try:
            format_date = datetime.strptime(uf_date, "%Y-%m-%d").date()
            today = date.today()
            if format_date.year != today.year:
                raise HTTPException(status_code=400, detail="The year date must be equal to current year")
            return format_date
        except ValueError as e:

            raise HTTPException(status_code=400, detail=f"Incorrect date format, should be in the format YYYY-MM-DD. {e}")