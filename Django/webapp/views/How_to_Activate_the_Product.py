from django.shortcuts import render
from django.templatetags.static import static
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

def index(request):
    viewer = StiViewer()

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    """Please use one of the methods below to register your license key"""
    #viewer.license.setFile(url_for('static', filename='private/license.key'))
    #viewer.license.setKey('6vJhGtLLLz2GNviWmUTrhSqnO...')
    
    report = StiReport()
    reportUrl = static('reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    viewer.report = report

    return viewer.getFrameworkResponse()
