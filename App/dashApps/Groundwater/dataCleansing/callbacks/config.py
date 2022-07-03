
# SECTION ::: Load Libraries

import base64
import io
import pandas as pd
import psycopg2
from sqlalchemy import *

# SECTION ::: Load Database

url_db_hydrograph = "postgresql://postgres:1234@127.0.0.1:5432/geoInfo"
engine_db_hydrograph = create_engine(url_db_hydrograph, echo=False)


# FUNCTION ::: Read Spreadsheet File

def read_spreadsheet(contents, filename):
    if '.xlsx' in filename or '.xls' in filename:
        data = {}
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        spreadsheet_file = pd.ExcelFile(io.BytesIO(decoded))
        if len(spreadsheet_file.sheet_names) >= 2:
            for sheet_name in spreadsheet_file.sheet_names:
                data[sheet_name] = spreadsheet_file.parse(sheet_name).to_dict()
            return data, spreadsheet_file.sheet_names
        else:
            return None, None
    else:
        return None, None


# -----------------------------------------------------------------------------
# HydrographData Template: Columns
# -----------------------------------------------------------------------------
HydrographDataSample = pd.ExcelFile('./Assets/Files/Groundwater/HydrographData_Template.xlsx')
HydrographDataSample_DataColumns = pd.read_excel(HydrographDataSample, sheet_name='Data').columns
HydrographDataSample_GeoInfoColumns = pd.read_excel(HydrographDataSample, sheet_name='GeoInfo').columns


# -----------------------------------------------------------------------------
# GEOINFO TABLE
# -----------------------------------------------------------------------------

def create___geoinfo_table___spreadsheet_database(
    data,
    con,
    name,
    column,
    if_exists
):
    data = data[column]
    COLs = ['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME']
    data[COLs] = data[COLs].apply(lambda x: x.str.rstrip())
    data[COLs] = data[COLs].apply(lambda x: x.str.lstrip())
    data[COLs] = data[COLs].apply(lambda x: x.str.replace('ي','ی'))
    data[COLs] = data[COLs].apply(lambda x: x.str.replace('ئ','ی'))
    data[COLs] = data[COLs].apply(lambda x: x.str.replace('ك', 'ک'))
    
    data.to_sql(
        name=name,
        con=con,
        if_exists=if_exists
    )


