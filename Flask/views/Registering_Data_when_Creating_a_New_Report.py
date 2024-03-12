from flask import Blueprint, request, render_template
from stimulsoft_reports.designer import StiDesigner

Registering_Data_when_Creating_a_New_Report = app = Blueprint('Registering_Data_when_Creating_a_New_Report', __name__)


@app.route('/Registering_Data_when_Creating_a_New_Report', methods = ['GET', 'POST'])
def index():
    # Creating a designer object
    designer = StiDesigner()

    # Defining designer events
    # When assigning a function name as a string, it will be called on the JavaScript client side
    # When assigning a function itself, it will be called on the Python server side
    designer.onCreateReport += 'createReport'

    # Defining designer options: enabling full-screen mode
    designer.options.appearance.fullScreenMode = True

    # If the request processing was successful, you need to return the result to the client side
    if designer.processRequest(request):
        return designer.getFrameworkResponse()

    # Getting the necessary JavaScript code and visual HTML part of the designer
    js = designer.javascript.getHtml()
    html = designer.getHtml()

    # Rendering an HTML template, inside which JavaScript and HTML code of the designer are displayed
    return render_template('Registering_Data_when_Creating_a_New_Report.html', designerJavaScript = js, designerHtml = html)
