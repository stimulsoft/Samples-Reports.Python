from django.shortcuts import render
from django.templatetags.static import static
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

def viewer(request):
    viewer = StiViewer()
    viewer.onBeginProcessData += 'beginProcessData'
	
    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
	
    report = StiReport()
    reportUrl = static('reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    viewer.report = report

    js = viewer.javascript.getHtml()
    html = viewer.getHtml()

    return render(request, 'Registering_a_Data_from_Code.html', {'viewerJavaScript': js, 'viewerHtml': html})