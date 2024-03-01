from flask import Blueprint, request, render_template, url_for
from stimulsoft_reports import StiHandler
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

Using_a_Handler_in_a_Separate_Function = app = Blueprint('Using_a_Handler_in_a_Separate_Function', __name__)


# Creating an event handler object and setting the URL for requests
mainHandler = StiHandler('/Using_a_Handler_in_a_Separate_Function/handler')

@app.route('/Using_a_Handler_in_a_Separate_Function')
def index():
    # Creating a viewer object and defining options (enabling the scrollbar, setting the event handler)
    viewer = StiViewer()
    viewer.handler = mainHandler
    viewer.options.appearance.fullScreenMode = True

    # Creating a report object and loading a report by URL
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)

    # Assigning a report object to the viewer
    viewer.report = report

    # Getting the necessary JavaScript code and visual HTML part of the viewer
    js = viewer.javascript.getHtml()
    html = viewer.getHtml()

    # Rendering an HTML template, inside which JavaScript and HTML code of the viewer are displayed
    return render_template('Using_a_Handler_in_a_Separate_Function.html', viewerJavaScript = js, viewerHtml = html)


@app.route('/Using_a_Handler_in_a_Separate_Function/handler', methods = ['GET', 'POST'])
def handler():
    # Processing the request and returning the result to the client side
    mainHandler.processRequest(request)
    return mainHandler.getFrameworkResponse()
