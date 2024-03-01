from flask import Blueprint, request, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

How_to_Activate_the_Product = app = Blueprint('How_to_Activate_the_Product', __name__)


@app.route('/How_to_Activate_the_Product', methods = ['GET', 'POST'])
def index():
    # Creating a viewer object
    viewer = StiViewer()

    # If the request processing was successful, you need to return the result to the client side
    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    # You can use one of the methods below to register your license key
    # viewer.license.setFile(url_for('static', filename='private/license.key'))
    # viewer.license.setKey('6vJhGtLLLz2GNviWmUTrhSqnO...')
    
    # Creating a report object and loading a report by URL
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)

    # Assigning a report object to the viewer
    viewer.report = report

    # Displaying the visual part of the viewer as a prepared HTML page
    return viewer.getFrameworkResponse()
