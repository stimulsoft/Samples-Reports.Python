from flask import Blueprint, request, render_template, url_for
from stimulsoft_reports.report import StiReport

Rendering_a_Report_from_Code = app = Blueprint('Rendering_a_Report_from_Code', __name__)


@app.route('/Rendering_a_Report_from_Code', methods = ['GET', 'POST'])
def index():
    # Creating a report object
    report = StiReport()

    # Defining report events
    # When assigning a function name as a string, it will be called on the JavaScript client side
    # When assigning a function itself, it will be called on the Python server side
    report.onAfterRender += 'afterRender'

    # If the request processing was successful, you need to return the result to the client side
    if report.processRequest(request):
        return report.getFrameworkResponse()
    
    # Loading a report by URL
    # This method does not load the report object on the server side, it only generates the necessary JavaScript code
    # The report will be loaded into a JavaScript object on the client side
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)

    # Calling the report build
    # This method does not render the report on the server side, it only generates the necessary JavaScript code
    # The report will be rendered using a JavaScript engine on the client side
    report.render()

    # Getting the necessary JavaScript code and HTML part of the report generator
    js = report.javascript.getHtml()
    html = report.getHtml()

    # Rendering an HTML template, inside which JavaScript and HTML code of the report are displayed
    return render_template('Rendering_a_Report_from_Code.html', reportJavaScript = js, reportHtml = html)
