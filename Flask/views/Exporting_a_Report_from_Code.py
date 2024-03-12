from flask import Blueprint, request, render_template, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.report.enums import StiExportFormat

Exporting_a_Report_from_Code = app = Blueprint('Exporting_a_Report_from_Code', __name__)


@app.route('/Exporting_a_Report_from_Code')
def index():
    # Rendering an HTML template
    return render_template('Exporting_a_Report_from_Code.html')


@app.route('/Exporting_a_Report_from_Code/export', methods = ['GET', 'POST'])
def export():
    # Creating a report object
    report = StiReport()

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

    # Getting the export format passed in the GET request parameters
    requestFormat = request.args.get('format')
    exportFormat = StiExportFormat.DOCUMENT
    if requestFormat == 'pdf':
        exportFormat = StiExportFormat.PDF
    elif requestFormat == 'excel':
        exportFormat = StiExportFormat.EXCEL
    elif requestFormat == 'html':
        exportFormat = StiExportFormat.HTML

    # Calling the report export to the specified format
    # This method does not export the report on the server side, it only generates the necessary JavaScript code
    # The report will be exported using a JavaScript engine on the client side
    report.exportDocument(exportFormat)

    # Getting the necessary JavaScript code and HTML part of the report generator
    js = report.javascript.getHtml()
    html = report.getHtml()

    # Rendering an HTML template, inside which JavaScript and HTML code of the report are displayed
    return render_template('Exporting_a_Report_from_Code.html', reportJavaScript = js, reportHtml = html)
