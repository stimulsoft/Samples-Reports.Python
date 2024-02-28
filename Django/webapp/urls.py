from django.urls import path
from .views import index
from .views import Exporting_a_Report_from_Code, Registering_a_Data_from_Code
from .views import Showing_a_Report_in_the_Viewer, Showing_a_Report_in_the_Viewer_in_an_HTML_template
from .views import Editing_a_Report_Template_in_the_Designer, Editing_a_Report_Template_in_the_Designer_in_an_HTML_template

urlpatterns = [
    path("", index.home, name="index"),
    path("Showing_a_Report_in_the_Viewer", Showing_a_Report_in_the_Viewer.viewer, name="Showing_a_Report_in_the_Viewer"),
    path("Showing_a_Report_in_the_Viewer_in_an_HTML_template", Showing_a_Report_in_the_Viewer_in_an_HTML_template.viewer, name="Showing_a_Report_in_the_Viewer_in_an_HTML_template"),
    path("Editing_a_Report_Template_in_the_Designer", Editing_a_Report_Template_in_the_Designer.designer, name="Editing_a_Report_Template_in_the_Designer"),
    path("Editing_a_Report_Template_in_the_Designer_in_an_HTML_template", Editing_a_Report_Template_in_the_Designer_in_an_HTML_template.designer, name="Editing_a_Report_Template_in_the_Designer_in_an_HTML_template"),
    path("Exporting_a_Report_from_Code", Exporting_a_Report_from_Code.index, name="Exporting_a_Report_from_Code"),
    path("Exporting_a_Report_from_Code/export", Exporting_a_Report_from_Code.export, name="Exporting_a_Report_from_Code_Export"),
    path("Registering_a_Data_from_Code", Registering_a_Data_from_Code.viewer, name="Registering_a_Data_from_Code")
]