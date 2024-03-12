from flask import Blueprint, request, url_for
from stimulsoft_reports.events import StiEmailEventArgs
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

Sending_a_Report_by_Email = app = Blueprint('Sending_a_Report_by_Email', __name__)


# The function will be called when sending a report by mail, after it has been exported
def emailReport(args: StiEmailEventArgs):

    # Defining the required options for sending (host, login, password), they will not be passed to the client side
    args.settings.fromAddr = 'mail.sender@stimulsoft.com'
    args.settings.host = 'smtp.stimulsoft.com'
    args.settings.port = 456
    args.settings.login = '********'
    args.settings.password = '********'

    # You can return a message about the successful sending of an email
    # If the message is not required, do not return the result, or return None
    # If an error occurred while sending an email, a message from the email sending module will be displayed
    return 'The Email has been sent successfully.'


@app.route('/Sending_a_Report_by_Email', methods = ['GET', 'POST'])
def index():
    # Creating a viewer object
    viewer = StiViewer()

    # Defining viewer options: displaying the Send Email button
    viewer.options.toolbar.showSendEmailButton = True

    # Defining viewer events
    # When assigning a function name as a string, it will be called on the JavaScript client side
    # When assigning a function itself, it will be called on the Python server side
    viewer.onEmailReport += emailReport

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
