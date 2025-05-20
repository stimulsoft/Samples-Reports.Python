from tornado.web import RequestHandler
from stimulsoft_reports import StiHandler
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer


class IndexHandler(RequestHandler):
    # A separate event handler is required to process POST requests
    handler = StiHandler()

    def get(self):
        # Creating a viewer object and assign an event handler
        viewer = StiViewer()
        viewer.handler = self.handler

        # Defining viewer options: enabling the scrollbar, setting the width and height of the viewer
        viewer.options.appearance.scrollbarsMode = True
        viewer.options.width = '1000px'
        viewer.options.height = '600px'

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

        # Getting the necessary JavaScript code and visual HTML part of the viewer
        js = viewer.javascript.getHtml()
        html = viewer.getHtml()

        # Rendering an HTML template, inside which JavaScript and HTML code of the viewer are displayed
        self.render('Showing_a_Report_in_the_Viewer_in_an_HTML_template.html', viewerJavaScript = js, viewerHtml = html)
    
    def post(self):
        # Processing POST requests
        if self.handler.processRequest(self.request):
            return self.handler.getFrameworkResponse(self)
