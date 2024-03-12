from flask import Blueprint, request, render_template, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

Showing_a_Report_in_the_Viewer_in_an_HTML_template = app = Blueprint('Showing_a_Report_in_the_Viewer_in_an_HTML_template', __name__)


@app.route('/Showing_a_Report_in_the_Viewer_in_an_HTML_template', methods = ['GET', 'POST'])
def index():
    # Creating a viewer object
    viewer = StiViewer()

    # Defining viewer options: enabling the scrollbar, setting the width and height of the viewer
    viewer.options.appearance.scrollbarsMode = True
    viewer.options.width = '1000px'
    viewer.options.height = '600px'

    # If the request processing was successful, you need to return the result to the client side
    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    # Creating a report object
    report = StiReport()

    # Loading a report by URL
    # This method does not load the report object on the server side, it only generates the necessary JavaScript code
    # The report will be loaded into a JavaScript object on the client side
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)

    # Assigning a report object to the viewer
    viewer.report = report

    # Getting the necessary JavaScript code and visual HTML part of the viewer
    js = viewer.javascript.getHtml()
    html = viewer.getHtml()

    # Rendering an HTML template, inside which JavaScript and HTML code of the viewer are displayed
    return render_template('Showing_a_Report_in_the_Viewer_in_an_HTML_template.html', viewerJavaScript = js, viewerHtml = html)
