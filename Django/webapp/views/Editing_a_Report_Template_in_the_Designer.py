from django.templatetags.static import static
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner


def index(request):
	# Creating a designer object
	designer = StiDesigner()

	# If the request processing was successful, you need to return the result to the client side
	if designer.processRequest(request):
		return designer.getFrameworkResponse()

	# Creating a report object and loading a report by URL
	report = StiReport()
	reportUrl = static('reports/SimpleList.mrt')
	report.loadFile(reportUrl)

	# Assigning a report object to the designer
	designer.report = report

	# Displaying the visual part of the designer as a prepared HTML page
	return designer.getFrameworkResponse()
