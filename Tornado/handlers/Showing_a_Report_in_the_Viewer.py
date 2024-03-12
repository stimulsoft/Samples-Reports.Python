from tornado.web import RequestHandler
from stimulsoft_reports import StiHandler
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer


class IndexHandler(RequestHandler):
    def get(self):
        # Creating a viewer object
        viewer = StiViewer()
        
        # If the request processing was successful, you need to return the result to the client side
        if viewer.processRequest(self.request):
            return viewer.getFrameworkResponse(self)
        
        # Creating a report object
        report = StiReport()

        # Loading a report by URL
        # This method does not load the report object on the server side, it only generates the necessary JavaScript code
        # The report will be loaded into a JavaScript object on the client side
        reportUrl = self.static_url('reports/SimpleList.mrt')
        report.loadFile(reportUrl)

        # Assigning a report object to the viewer
        viewer.report = report

        # Displaying the visual part of the viewer as a prepared HTML page
        return viewer.getFrameworkResponse(self)
    
    def post(self):
        # A separate event handler is required to process POST requests
        handler = StiHandler()
        if handler.processRequest(self.request):
            return handler.getFrameworkResponse(self)
