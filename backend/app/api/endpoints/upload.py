from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from typing import List
import xml.etree.ElementTree as ET
import io
import pandas as pd
from datetime import datetime

from app.api.endpoints.utils import validate_xml

router = APIRouter()



@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    # Create a temporary file-like object from the uploaded file
    file_content = await file.read()
    
    schema_path = "app/schemas/saft_schema.xsd"

    try:
        validate_xml(file_content, schema_path)
        
    except ET.ParseError as e:
        raise HTTPException(status_code=400, detail=f"Invalid XML format: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Validation failed: {str(e)}")
    finally:
        await file.close()