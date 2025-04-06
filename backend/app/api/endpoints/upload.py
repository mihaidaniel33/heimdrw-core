from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from typing import List
import xml.etree.ElementTree as ET
import io
import pandas as pd
from datetime import datetime

router = APIRouter()

def process_xml_to_dataframe(xml_content: bytes) -> pd.DataFrame:
    # Parse XML content
    tree = ET.parse(io.BytesIO(xml_content))
    root = tree.getroot()
    
    # Initialize lists to store data
    data = []
    
    # Example XML processing - adjust according to your XML structure
    for element in root.findall('.//transaction'):  # Adjust the path according to your XML structure
        row = {
            'date': element.find('date').text if element.find('date') is not None else '',
            'description': element.find('description').text if element.find('description') is not None else '',
            'amount': element.find('amount').text if element.find('amount') is not None else '',
            'category': element.find('category').text if element.find('category') is not None else '',
        }
        data.append(row)
    
    # Create DataFrame
    df = pd.DataFrame(data)
    return df

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith('.xml'):
        raise HTTPException(status_code=400, detail="Only XML files are allowed")
    
    try:
        # Read the file content
        content = await file.read()
        
        # Process XML and convert to DataFrame
        try:
            df = process_xml_to_dataframe(content)
            
            # Create Excel file in memory
            excel_file = io.BytesIO()
            with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Financial Data')
            
            # Reset the pointer
            excel_file.seek(0)
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"processed_{timestamp}.xlsx"
            
            # Return the Excel file
            return StreamingResponse(
                excel_file,
                media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                headers={
                    "Content-Disposition": f"attachment; filename={output_filename}"
                }
            )
            
        except ET.ParseError:
            raise HTTPException(status_code=400, detail="Invalid XML file")
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing XML: {str(e)}")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 