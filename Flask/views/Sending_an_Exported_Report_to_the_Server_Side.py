import os
from flask import Blueprint, request, url_for
from stimulsoft_reports import StiResult
from stimulsoft_reports.events import StiExportEventArgs
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

Sending_an_Exported_Report_to_the_Server_Side = app = Blueprint('Sending_an_Exported_Report_to_the_Server_Side', __name__)


# The function will be called after exporting the report
def endExportReport(args: StiExportEventArgs):
    
    # Getting the absolute path to the report file to save
    filePath = os.path.normpath(os.getcwd() + url_for('static', filename='reports/' + args.fileName))
    
    try:
        # Opening the file for saving, and saving the byte data stream of the exported report
        with open(filePath, mode='wb') as file:
            file.write(args.data)
            file.close()
    except Exception as e:
        # In case of an error, the error message is passed to the viewer
        return StiResult.getError(str(e))
    
    # If the save is successful, a message can be displayed
    # If the message is not required, do not return the result, or return None
    return f'The exported report was successfully saved to a {args.fileName} file.'


@app.route('/Sending_an_Exported_Report_to_the_Server_Side', methods = ['GET', 'POST'])
def index():
    # Creating a viewer object
    viewer = StiViewer()
    viewer.javascript.appendHead('<link rel="shortcut icon" href="' + url_for('static', filename = 'favicon.ico') + '" type="image/x-icon">')

    # Defining viewer events
    # When assigning a function name as a string, it will be called on the JavaScript client side
    # When assigning a function itself, it will be called on the Python server side
    viewer.onEndExportReport += endExportReport

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

    # Displaying the visual part of the viewer as a prepared HTML page
    return viewer.getFrameworkResponse()
