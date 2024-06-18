from flask import Blueprint, request, make_response, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.report.enums import StiEngineType

Rendering_a_Report_from_Code_on_the_Server_Side = app = Blueprint('Rendering_a_Report_from_Code_on_the_Server_Side', __name__)


@app.route('/Rendering_a_Report_from_Code_on_the_Server_Side', methods = ['GET', 'POST'])
def index():
    # Creating a report object
    report = StiReport()

    # Setting the server-side rendering mode
    report.engine = StiEngineType.SERVER_NODE_JS

    # If the request processing was successful, you need to return the result to the client side
    if report.processRequest(request):
        return report.getFrameworkResponse()
    
    # Loading a report by URL
    # This method loads a report file and stores it as a compressed string in an object.
    # The report will be loaded from this string into a JavaScript object when using Node.js
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl, True)

    # Building a report
    # The report is not built using Python code.
    # This method will prepare JavaScript code and pass it to Node.js, which will build a report and return the finished document.
    result = report.render()

    if result:
        # After successfully building a report, the finished document can be saved as a string or to a file
        document = report.saveDocument()
        # result = report.saveDocument(url_for('static', filename = 'reports/SimpleList.mdc'))
        
        message = f'The finished document takes {len(document)} bytes.'
    else:
        # If there is a build error, you can display the error text.
        message = report.nodejs.error
    
    # Returning a text message as the server response.
    return make_response(message)

    