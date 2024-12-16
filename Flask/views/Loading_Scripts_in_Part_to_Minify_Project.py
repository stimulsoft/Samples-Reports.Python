from flask import Blueprint, request, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner

Loading_Scripts_in_Part_to_Minify_Project = app = Blueprint('Loading_Scripts_in_Part_to_Minify_Project', __name__)


@app.route('/Loading_Scripts_in_Part_to_Minify_Project', methods = ['GET', 'POST'])
def index():
    # Creating a designer object
    designer = StiDesigner()
    designer.javascript.appendHead('<link rel="shortcut icon" href="' + url_for('static', filename = 'favicon.ico') + '" type="image/x-icon">')

    # If the request processing was successful, you need to return the result to the client side
    if designer.processRequest(request):
        return designer.getFrameworkResponse()
    
    # Defining JavaScript modules required for the report designer to work
    designer.javascript.reportsSet = False
    designer.javascript.blocklyEditor = False
    designer.javascript.reportsChart = True
    designer.javascript.reportsExport = True
    designer.javascript.reportsImportXlsx = False
    designer.javascript.reportsMaps = False
    
    # Creating a report object
    report = StiReport()

    # Loading a report by URL
    # This method does not load the report object on the server side, it only generates the necessary JavaScript code
    # The report will be loaded into a JavaScript object on the client side
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)

    # Assigning a report object to the designer
    designer.report = report

    # Displaying the visual part of the designer as a prepared HTML page
    return designer.getFrameworkResponse()
