from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from fastapi.responses import StreamingResponse
from typing import List
import xml.etree.ElementTree as ET
import io
import pandas as pd
from datetime import datetime
import re
import logging

from app.api.endpoints.utils import validate_xml
from app.xml_parser.parser import parse_saft_to_excel

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def is_valid_email(email: str) -> bool:
    """Validate email format using regex."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    email: str = Form(...)
):
    try:
        logger.info(f"Received upload request from email: {email}")
        
        # Validate email format
        if not is_valid_email(email):
            logger.error(f"Invalid email format: {email}")
            raise HTTPException(status_code=400, detail="Invalid email format")

        # Read file content
        file_content = await file.read()
        logger.info(f"Received file: {file.filename} ({len(file_content)} bytes)")
        
        schema_path = "app/schemas/saft_schema.xsd"

        try:
            validate_xml(file_content, schema_path)
            logger.info("XML validation successful")
        except ET.ParseError as e:
            logger.error(f"XML parsing error: {str(e)}")
            raise HTTPException(status_code=400, detail=f"Invalid XML format: {str(e)}")
        except Exception as e:
            logger.error(f"XML validation error: {str(e)}")
            raise HTTPException(status_code=400, detail=f"Validation failed: {str(e)}")

        try:
            excel_buffer = parse_saft_to_excel(io.BytesIO(file_content))
            excel_buffer.seek(0)
            logger.info("Excel file generated successfully")
        except Exception as e:
            logger.error(f"Excel generation error: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error generating Excel file: {str(e)}")
        
        return StreamingResponse(
            excel_buffer, 
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", 
            headers={
                "Content-Disposition": f"attachment; filename=saft_data_{email.split('@')[0]}.xlsx"
            }
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    