import asyncio, os
from tornado.web import Application, RequestHandler, url
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner

class MainHandler(RequestHandler):
    def get(self):
        designer = StiDesigner()

        if designer.processRequest(self.request):
            return designer.getFrameworkResponse(self)
        
        report = StiReport()
        reportUrl = self.static_url('reports/SimpleList.mrt')
        report.loadFile(reportUrl)
        designer.report = report

        return designer.getFrameworkResponse(self)

class WebApplication(Application):
	def __init__(self):
		handlers = [
			url(r'/', MainHandler)
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
