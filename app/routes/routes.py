from fastapi import APIRouter
from app.controllers.uf_controller import UFController

router = APIRouter()

router.add_api_route(path='/last_ufs', endpoint=UFController.get_last_ufs, summary="Show the list of fomento unit for current year")
router.add_api_route(path='/ufs/{year}', endpoint=UFController.get_ufs, summary="Show the list of fomento unit for a specific year")
router.add_api_route(path='/uf/{uf_date}', endpoint=UFController.get_uf, summary="Show the fomento unit for a specific date")

