import json
import os
from flask import Blueprint, request, url_for
from stimulsoft_reports import StiResult
from stimulsoft_reports.designer import StiDesigner
from stimulsoft_reports.events import StiReportEventArgs
from stimulsoft_reports.report import StiReport

Saving_a_Report_Template_on_the_Server_Side = app = Blueprint('Saving_a_Report_Template_on_the_Server_Side', __name__)


# The function will be called when saving the report (both manual and automatic)
def saveReport(args: StiReportEventArgs):

    # Getting the absolute path to the report file to save
    filePath = os.path.normpath(os.getcwd() + url_for('static', filename = 'reports/' + args.fileName))
    
    try:
        # Opening the file for saving, converting the report to JSON and saving it
        with open(filePath, mode='w', encoding='utf-8') as file:
            jsonReport = json.dumps(args.report, indent = 4)
            file.write(jsonReport)
            file.close()
    except Exception as e:
        # In case of an error, the error message is passed to the designer
        return StiResult.getError(str(e))

    # If the save is successful, a message can be displayed
    # If the message is not required, do not return the result, or return None
    return f'The report was successfully saved to a {args.fileName} file.'


@app.route('/Saving_a_Report_Template_on_the_Server_Side', methods = ['GET', 'POST'])
def index():
    # Creating a designer object
    designer = StiDesigner()
    designer.javascript.appendHead('<link rel="shortcut icon" href="' + url_for('static', filename = 'favicon.ico') + '" type="image/x-icon">')

    # Defining designer events
    # When assigning a function name as a string, it will be called on the JavaScript client side
    # When assigning a function itself, it will be called on the Python server side
    designer.onSaveReport += saveReport

    # If the request processing was successful, you need to return the result to the client side
    if designer.processRequest(request):
        return designer.getFrameworkResponse()
    
    # Creating a report object
    report = StiReport()

    # Loading a report by URL
    # This method does not load the report object on the server side, it only generates the necessary JavaScript code
    # The report will be loaded into a JavaScript object on the client side
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)

    # Assigning a report object to the designer
    designer.report = report

    # Displaying the visual part of the designer as a prepared HTML page
    return designer.getFrameworkResponse()
