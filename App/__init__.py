from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Groundwater App
from App.dashApps.Groundwater.dataCleansing.app import create_groundwater_dataCleansing_app
# from App.dashApps.Groundwater.dataVisualization.app import create_groundwater_dataVisualization_app
# from App.dashApps.Groundwater.unitHydrograph.app import create_groundwater_unitHydrograph_app

app = Flask(
    import_name=__name__,
    static_folder='static'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'Assets/Files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SECRET_KEY'] = 'd3946e1cf4b2b53d4dcf5d9e3b126498ac2876892270735eddbb7e3aca8a7bbe'

# Groundwater App
create_groundwater_dataCleansing_app(server=app)
# create_groundwater_dataVisualization_app(server=app)
# create_groundwater_unitHydrograph_app(server=app)

from App import routes