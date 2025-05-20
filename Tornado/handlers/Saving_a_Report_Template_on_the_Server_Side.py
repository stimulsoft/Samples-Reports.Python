import json
import os
from tornado.web import RequestHandler
from stimulsoft_data_adapters.classes.StiPath import StiPath
from stimulsoft_reports import StiHandler, StiResult
from stimulsoft_reports.designer import StiDesigner
from stimulsoft_reports.events import StiReportEventArgs
from stimulsoft_reports.report import StiReport


class IndexHandler(RequestHandler):
    # A separate event handler is required to process POST requests
    handler = StiHandler()

    # The function will be called when saving the report (both manual and automatic)
    def saveReport(self, args: StiReportEventArgs):

        # Getting the absolute path to the report file to save
        filePath = StiPath.normalize(os.path.normpath(os.getcwd() + self.static_url('reports/' + args.fileName)))
        
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

    def get(self):
        # Creating a designer object and assign an event handler
        designer = StiDesigner()
        designer.handler = self.handler
        designer.javascript.appendHead('<link rel="shortcut icon" href="' + self.static_url('favicon.ico') + '" type="image/x-icon">')
    
        # Defining designer events
        # When assigning a function name as a string, it will be called on the JavaScript client side
        # When assigning a function itself, it will be called on the Python server side
        designer.onSaveReport += self.saveReport

        # If the request processing was successful, you need to return the result to the client side
        if designer.processRequest(self.request):
            return designer.getFrameworkResponse(self)
        
        # Creating a report object
        report = StiReport()

        # Loading a report by URL
        # This method does not load the report object on the server side, it only generates the necessary JavaScript code
        # The report will be loaded into a JavaScript object on the client side
        reportUrl = self.static_url('reports/SimpleList.mrt')
        report.loadFile(reportUrl)

        # Assigning a report object to the designer
        designer.report = report

        # Displaying the visual part of the designer as a prepared HTML page
        return designer.getFrameworkResponse(self)
    
    def post(self):
        # Processing POST requests
        if self.handler.processRequest(self.request):
            return self.handler.getFrameworkResponse(self)

