from django.shortcuts import render
from django.templatetags.static import static
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.report.enums import StiExportFormat

def index(request):
    return render(request, 'Exporting_a_Report_from_Code.html')

def export(request):
    report = StiReport()

    if report.processRequest(request):
        return report.getFrameworkResponse()

    reportUrl = static('reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    report.render()

    requestFormat = request.GET.get('format')
    exportFormat = StiExportFormat.DOCUMENT
    if requestFormat == 'pdf':
        exportFormat = StiExportFormat.PDF
    elif requestFormat == 'excel':
        exportFormat = StiExportFormat.EXCEL
    elif requestFormat == 'html':
        exportFormat = StiExportFormat.HTML

    report.exportDocument(exportFormat)
    
    js = report.javascript.getHtml()
    html = report.getHtml()

    return render(request, 'Exporting_a_Report_from_Code.html', {'reportJavaScript': js, 'reportHtml': html})
