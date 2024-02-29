from django.shortcuts import render
from django.templatetags.static import static
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

def index(request):
	viewer = StiViewer()
	if viewer.processRequest(request):
		return viewer.getFrameworkResponse()

	report = StiReport()
	reportUrl = static('reports/SimpleList.mrt')
	report.loadFile(reportUrl)

	viewer.report = report

	return viewer.getFrameworkResponse()
