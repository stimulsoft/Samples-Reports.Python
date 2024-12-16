from tornado.web import RequestHandler
from stimulsoft_reports import StiHandler, StiLicense
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer


class IndexHandler(RequestHandler):
    def get(self):
        # Creating a viewer object
        viewer = StiViewer()
        viewer.javascript.appendHead('<link rel="shortcut icon" href="' + self.static_url('favicon.ico') + '" type="image/x-icon">')

        # If the request processing was successful, you need to return the result to the client side
        if viewer.processRequest(self.request):
            return viewer.getFrameworkResponse(self)
        
        # You can use one of the methods below to register your license key
        # StiLicense.setFile(self.static_url('private/license.key'))
        # StiLicense.setKey('6vJhGtLLLz2GNviWmUTrhSqnO...')
        
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