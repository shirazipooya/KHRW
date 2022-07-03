from flask import render_template
from App import app

@app.route('/')
def home():
    return render_template(template_name_or_list="home.html")

@app.route('/groundwater')
def groundwater():
    return render_template(template_name_or_list="groundwater.html")

@app.route('/groundwater/dataCleansing')
def groundwater_dataCleansing():
    return app.index()

@app.route('/groundwater/dataVisualization')
def groundwater_dataVisualization():
    return app.index()

@app.route('/groundwater/unitHydrograph')
def groundwater_unitHydrograph():
    return app.index()