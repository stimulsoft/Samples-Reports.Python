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
        
        # You can use one of the methods below to register your license key
        # viewer.license.setFile(self.static_url('private/license.key'))
        # viewer.license.setKey('6vJhGtLLLz2GNviWmUTrhSqnO...')
        
        # Creating a report object and loading a report by URL
        report = StiReport()
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