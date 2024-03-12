from django.shortcuts import render
from django.templatetags.static import static
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

def index(request):
    # Creating a viewer object
    viewer = StiViewer()

    # Defining viewer events
    # When assigning a function name as a string, it will be called on the JavaScript client side
    # When assigning a function itself, it will be called on the Python server side
    viewer.onBeginProcessData += 'beginProcessData'
    
    # If the request processing was successful, you need to return the result to the client side
    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    # Creating a report object
    report = StiReport()

    # Loading a report by URL
    # This method does not load the report object on the server side, it only generates the necessary JavaScript code
    # The report will be loaded into a JavaScript object on the client side
    reportUrl = static('reports/SimpleList.mrt')
    report.loadFile(reportUrl)

    # Assigning a report object to the viewer
    viewer.report = report

    # Getting the necessary JavaScript code and visual HTML part of the viewer
    js = viewer.javascript.getHtml()
    html = viewer.getHtml()

    # Rendering an HTML template, inside which JavaScript and HTML code of the viewer are displayed
    return render(request, 'Registering_a_Data_from_Code.html', {'viewerJavaScript': js, 'viewerHtml': html})