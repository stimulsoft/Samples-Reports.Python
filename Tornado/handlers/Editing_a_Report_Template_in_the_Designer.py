from tornado.web import RequestHandler
from stimulsoft_reports import StiHandler
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner


class IndexHandler(RequestHandler):
    # A separate event handler is required to process POST requests
    handler = StiHandler()

    def get(self):
        # Creating a designer object and assign an event handler
        designer = StiDesigner()
        designer.handler = self.handler
        designer.javascript.appendHead('<link rel="shortcut icon" href="' + self.static_url('favicon.ico') + '" type="image/x-icon">')

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

