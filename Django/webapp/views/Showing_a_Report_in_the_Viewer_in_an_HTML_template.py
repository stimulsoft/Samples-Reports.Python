from django.shortcuts import render
from django.templatetags.static import static
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

def index(request):
    viewer = StiViewer()
    viewer.options.appearance.scrollbarsMode = True
    viewer.options.width = '1000px'
    viewer.options.height = '600px'

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    report = StiReport()
    reportUrl = static('reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    viewer.report = report

    js = viewer.javascript.getHtml()
    html = viewer.getHtml()

    return render(request, 'Showing_a_Report_in_the_Viewer_in_an_HTML_template.html', {'viewerJavaScript': js, 'viewerHtml': html})
