from django.shortcuts import render
from django.templatetags.static import static
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.report.enums import StiExportFormat


def index(request):
    # Rendering an HTML template
    return render(request, 'Exporting_a_Report_from_Code.html')


def export(request):
    # Creating a report object
    report = StiReport()

    # If the request processing was successful, you need to return the result to the client side
    if report.processRequest(request):
        return report.getFrameworkResponse()

    # Loading a report by URL and calling the report build
    reportUrl = static('reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    report.render()

    # Getting the export format passed in the GET request parameters
    requestFormat = request.GET.get('format')
    exportFormat = StiExportFormat.DOCUMENT
    if requestFormat == 'pdf':
        exportFormat = StiExportFormat.PDF
    elif requestFormat == 'excel':
        exportFormat = StiExportFormat.EXCEL
    elif requestFormat == 'html':
        exportFormat = StiExportFormat.HTML

    # Calling a report export to a specified format
    report.exportDocument(exportFormat)
    
    # Getting the necessary JavaScript code and HTML part of the report generator
    js = report.javascript.getHtml()
    html = report.getHtml()

    # Rendering an HTML template, inside which JavaScript and HTML code of the report are displayed
    return render(request, 'Exporting_a_Report_from_Code.html', {'reportJavaScript': js, 'reportHtml': html})
