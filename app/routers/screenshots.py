from fastapi import APIRouter
from fastapi.responses import JSONResponse, FileResponse
from app import utils
from app.db import mongodb
import os
import uuid

router = APIRouter()

@router.get("/{id}")
def get_screenshot(id: str):
    screenshots_path = os.path.join(f"{os.getcwd()}/screenshots/{id}")

    if not os.path.exists(screenshots_path):
        return JSONResponse(status_code=404, content={"message": "the ID does not exist"})

    utils.create_zip(id, zip_path=screenshots_path)

    created_zip_path = os.path.join(f"{os.getcwd()}/{id}.zip")

    return FileResponse(status_code=200, path=created_zip_path, filename=f"{id}.zip", media_type='application/zip')

@router.post("/")
async def create_screenshot(start_url: str, number_of_links: int):
    scrape_id = str(uuid.uuid1())
    
    inserted_id = mongodb.insert_document({"_id": scrape_id})

    await utils.screenshot_scraped_pages(start_url, number_of_links, scrape_id)

    return JSONResponse(status_code=201, content={"ID": inserted_id})
