from App.dashApps.Groundwater.dataCleansing.callbacks.database_tab import groundwater___dataCleansing___callback___database_tab
from App.dashApps.Groundwater.dataCleansing.callbacks.dataCleansing_tab import groundwater___dataCleansing___callback___dataCleansing_tab
from App.dashApps.Groundwater.dataCleansing.callbacks.missingData_tab import groundwater___dataCleansing___callback___missingData_tab
from App.dashApps.Groundwater.dataCleansing.callbacks.syncDate_tab import groundwater___dataCleansing___callback___syncDate_tab

def groundwater___dataCleansing___callback(app):
    groundwater___dataCleansing___callback___database_tab(app=app)
    groundwater___dataCleansing___callback___dataCleansing_tab(app=app)
    groundwater___dataCleansing___callback___missingData_tab(app=app)
    groundwater___dataCleansing___callback___syncDate_tab(app=app)
