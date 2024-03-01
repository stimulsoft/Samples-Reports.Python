from django.shortcuts import render
from django.templatetags.static import static
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

def index(request):
    # Creating a viewer object and defining JavaScript events
    viewer = StiViewer()
    viewer.onBeginProcessData += 'beginProcessData'
	
    # If the request processing was successful, you need to return the result to the client side
    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
	
    # Creating a report object and loading a report by URL
    report = StiReport()
    reportUrl = static('reports/SimpleList.mrt')
    report.loadFile(reportUrl)

    # Assigning a report object to the viewer
    viewer.report = report

    # Getting the necessary JavaScript code and visual HTML part of the viewer
    js = viewer.javascript.getHtml()
    html = viewer.getHtml()

    # Rendering an HTML template, inside which JavaScript and HTML code of the viewer are displayed
    return render(request, 'Registering_a_Data_from_Code.html', {'viewerJavaScript': js, 'viewerHtml': html})