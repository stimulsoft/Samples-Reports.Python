from flask import Blueprint, request, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner

Localizing_the_Designer = app = Blueprint('Localizing_the_Designer', __name__)


@app.route('/Localizing_the_Designer', methods = ['GET', 'POST'])
def index():
    # Creating a designer object
    designer = StiDesigner()

    # Defining the required interface localization
    # The list of available localizations can be obtained from the GitHub repository:
    # https://github.com/stimulsoft/Stimulsoft.Reports.Localization
    designer.options.localization = 'de.xml'

    # Additionally, it is possible to add optional localizations
    # They will be displayed in the localization menu in the designer panel
    designer.options.localizations.append('es.xml')
    designer.options.localizations.append('pt.xml')

    # If the request processing was successful, you need to return the result to the client side
    if designer.processRequest(request):
        return designer.getFrameworkResponse()
    
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
