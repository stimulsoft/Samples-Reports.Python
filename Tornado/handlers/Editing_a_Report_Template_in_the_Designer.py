from tornado.web import RequestHandler
from stimulsoft_reports import StiHandler
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner


class IndexHandler(RequestHandler):
    def get(self):
        # Creating a designer object
        designer = StiDesigner()

        # If the request processing was successful, you need to return the result to the client side
        if designer.processRequest(self.request):
            return designer.getFrameworkResponse(self)
        
        # Creating a report object and loading a report by URL
        report = StiReport()
        reportUrl = self.static_url('reports/SimpleList.mrt')
        report.loadFile(reportUrl)

        # Assigning a report object to the designer
        designer.report = report

        # Displaying the visual part of the designer as a prepared HTML page
        return designer.getFrameworkResponse(self)
    
    def post(self):
        # A separate event handler is required to process POST requests
        handler = StiHandler()
        if handler.processRequest(self.request):
            return handler.getFrameworkResponse(self)

