from django.templatetags.static import static
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer


def index(request):
	# Creating a viewer object
	viewer = StiViewer()
	
	# If the request processing was successful, you need to return the result to the client side
	if viewer.processRequest(request):
		return viewer.getFrameworkResponse()

	# Creating a report object and loading a report by URL
	report = StiReport()
	reportUrl = static('reports/SimpleList.mrt')
	report.loadFile(reportUrl)

	# Assigning a report object to the viewer
	viewer.report = report

	# Displaying the visual part of the viewer as a prepared HTML page
	return viewer.getFrameworkResponse()
