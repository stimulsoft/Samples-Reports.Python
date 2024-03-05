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

        # Getting the necessary JavaScript code and visual HTML part of the designer
        js = designer.javascript.getHtml()
        html = designer.getHtml()

        # Rendering an HTML template, inside which JavaScript and HTML code of the designer are displayed
        self.render('Editing_a_Report_Template_in_the_Designer_in_an_HTML_template.html', designerJavaScript = js, designerHtml = html)
    
    def post(self):
        # A separate event handler is required to process POST requests
        handler = StiHandler()
        if handler.processRequest(self.request):
            return handler.getFrameworkResponse(self)
