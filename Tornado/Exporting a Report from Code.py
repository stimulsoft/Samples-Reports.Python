import asyncio, os
from tornado.web import Application, RequestHandler, url
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.report.enums import StiExportFormat

class MainHandler(RequestHandler):
    def get(self):
        self.render('Exporting a Report from Code.html')

class ExportHandler(RequestHandler):
    def get(self):
        report = StiReport()

        if report.processRequest(self.request):
            return report.getFrameworkResponse(self)

        reportUrl = self.static_url('reports/SimpleList.mrt')
        report.loadFile(reportUrl)
        report.render()

        requestFormat = self.get_argument('format')
        exportFormat = StiExportFormat.DOCUMENT
        if requestFormat == 'pdf':
            exportFormat = StiExportFormat.PDF
        elif requestFormat == 'excel':
            exportFormat = StiExportFormat.EXCEL
        elif requestFormat == 'html':
            exportFormat = StiExportFormat.HTML

        report.exportDocument(exportFormat)

        return report.getFrameworkResponse(self)

class WebApplication(Application):
	def __init__(self):
		handlers = [
			url(r'/', MainHandler),
            url(r'/export', ExportHandler, name='export')
		]
		settings = dict(
			template_path=os.path.join(os.path.dirname(__file__), 'templates'),
			static_path=os.path.join(os.path.dirname(__file__), 'static')
		)
		Application.__init__(self, handlers, **settings)

async def main():
	app = WebApplication()
	app.listen(8040)
	print('Starting development server at http://127.0.0.1:8040/')
	await asyncio.Event().wait()

if __name__ == '__main__':
	asyncio.run(main())