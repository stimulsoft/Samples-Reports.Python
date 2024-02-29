from flask import Blueprint, request, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

How_to_Activate_the_Product = app = Blueprint('How_to_Activate_the_Product', __name__)

@app.route('/How_to_Activate_the_Product', methods = ['GET', 'POST'])
def index():
    viewer = StiViewer()

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    """Please use one of the methods below to register your license key"""
    #viewer.license.setFile(url_for('static', filename='private/license.key'))
    #viewer.license.setKey('6vJhGtLLLz2GNviWmUTrhSqnO...')
    
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    viewer.report = report

    return viewer.getFrameworkResponse()
