from tornado.web import RequestHandler
from stimulsoft_reports import StiHandler
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer


class IndexHandler(RequestHandler):
    def get(self):
        # Creating a viewer object and defining JavaScript events
        viewer = StiViewer()
        viewer.onBeginProcessData += 'beginProcessData'
        
        # If the request processing was successful, you need to return the result to the client side
        if viewer.processRequest(self.request):
            return viewer.getFrameworkResponse(self)
        
        # Creating a report object and loading a report by URL
        report = StiReport()
        reportUrl = self.static_url('reports/SimpleList.mrt')
        report.loadFile(reportUrl)

        # Assigning a report object to the viewer
        viewer.report = report

        # Getting the necessary JavaScript code and visual HTML part of the viewer
        js = viewer.javascript.getHtml()
        html = viewer.getHtml()

        # Rendering an HTML template, inside which JavaScript and HTML code of the viewer are displayed
        self.render('Registering_a_Data_from_Code.html', viewerJavaScript = js, viewerHtml = html)
    
    def post(self):
        # A separate event handler is required to process POST requests
        handler = StiHandler()
        if handler.processRequest(self.request):
            return handler.getFrameworkResponse(self)
