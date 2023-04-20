from fastapi import Depends
from app.services.uf_service import UFService
from app.utils.validate import Validate
import datetime

class UFController:
    def __init__(self):
        self.uf_service = UFService()

    @staticmethod
    def get_last_ufs():
        today = datetime.date.today()
        return UFService.get_ufs_data_by_year(today.year)

    @staticmethod
    def get_ufs(uf_year: str = Depends(Validate.validate_year)):
        return UFService.get_ufs_data_by_year(uf_year)

    @staticmethod
    def get_uf(uf_date: str = Depends(Validate.validate_date)):
        return UFService.get_uf_data_by_date(uf_date)