from tornado.web import RequestHandler
from stimulsoft_reports import StiHandler
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.report.enums import StiExportFormat


class IndexHandler(RequestHandler):
    def get(self):
        # Rendering an HTML template
        self.render('Exporting_a_Report_from_Code.html', reportJavaScript = '', reportHtml = '')


class ExportHandler(RequestHandler):
    def get(self):
        # Creating a report object
        report = StiReport()

        # If the request processing was successful, you need to return the result to the client side
        if report.processRequest(self.request):
            return report.getFrameworkResponse(self)

        # Loading a report by URL and calling the report build
        reportUrl = self.static_url('reports/SimpleList.mrt')
        report.loadFile(reportUrl)
        report.render()

        # Getting the export format passed in the GET request parameters
        requestFormat = self.get_argument('format')
        exportFormat = StiExportFormat.DOCUMENT
        if requestFormat == 'pdf':
            exportFormat = StiExportFormat.PDF
        elif requestFormat == 'excel':
            exportFormat = StiExportFormat.EXCEL
        elif requestFormat == 'html':
            exportFormat = StiExportFormat.HTML

        # Calling a report export to a specified format
        report.exportDocument(exportFormat)

        # Getting the necessary JavaScript code and HTML part of the report generator
        js = report.javascript.getHtml()
        html = report.getHtml()

        # Rendering an HTML template, inside which JavaScript and HTML code of the report are displayed
        return self.render('Exporting_a_Report_from_Code.html', reportJavaScript = js, reportHtml = html)
    
    def post(self):
        # A separate event handler is required to process POST requests
        handler = StiHandler()
        if handler.processRequest(self.request):
            return handler.getFrameworkResponse(self)
