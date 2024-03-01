from flask import Blueprint, request, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner

Localizing_the_Designer = app = Blueprint('Localizing_the_Designer', __name__)


@app.route('/Localizing_the_Designer', methods = ['GET', 'POST'])
def index():
    # Creating a designer object and defining the required interface localization
    designer = StiDesigner()
    designer.options.localization = 'de.xml'

    # If the request processing was successful, you need to return the result to the client side
    if designer.processRequest(request):
        return designer.getFrameworkResponse()
    
    # Creating a report object and loading a report by URL
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)

    # Assigning a report object to the designer
    designer.report = report

    # Displaying the visual part of the designer as a prepared HTML page
    return designer.getFrameworkResponse()
