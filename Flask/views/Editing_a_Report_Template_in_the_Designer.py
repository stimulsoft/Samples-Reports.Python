from flask import Blueprint, request, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner

Editing_a_Report_Template_in_the_Designer = app = Blueprint('Editing_a_Report_Template_in_the_Designer', __name__)


@app.route('/Editing_a_Report_Template_in_the_Designer', methods = ['GET', 'POST'])
def index():
    # Creating a designer object
    designer = StiDesigner()

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
