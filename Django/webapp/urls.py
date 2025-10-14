from django.urls import path
from django.contrib.staticfiles import views
from .views import *

urlpatterns = [
    path("favicon.ico", lambda req: views.serve(req, "favicon.ico")),
    path("", index.home, name="index"),
    path("Configuring_and_Installing_Node_js", Configuring_and_Installing_Node_js.index, name="Configuring_and_Installing_Node_js"),
    path("Showing_a_Report_in_the_Viewer", Showing_a_Report_in_the_Viewer.index, name="Showing_a_Report_in_the_Viewer"),
    path("Showing_a_Report_in_the_Viewer_in_an_HTML_template", Showing_a_Report_in_the_Viewer_in_an_HTML_template.index, name="Showing_a_Report_in_the_Viewer_in_an_HTML_template"),
    path("Editing_a_Report_Template_in_the_Designer", Editing_a_Report_Template_in_the_Designer.index, name="Editing_a_Report_Template_in_the_Designer"),
    path("Editing_a_Report_Template_in_the_Designer_in_an_HTML_template", Editing_a_Report_Template_in_the_Designer_in_an_HTML_template.index, name="Editing_a_Report_Template_in_the_Designer_in_an_HTML_template"),
    path("Exporting_a_Report_from_Code", Exporting_a_Report_from_Code.index, name="Exporting_a_Report_from_Code"),
    path("Exporting_a_Report_from_Code/export", Exporting_a_Report_from_Code.export, name="Exporting_a_Report_from_Code_Export"),
    path("Exporting_a_Report_from_Code_on_the_Server_Side", Exporting_a_Report_from_Code_on_the_Server_Side.index, name="Exporting_a_Report_from_Code_on_the_Server_Side"),
    path("Registering_a_Data_from_Code", Registering_a_Data_from_Code.index, name="Registering_a_Data_from_Code"),
    path("How_to_Activate_the_Product", How_to_Activate_the_Product.index, name="How_to_Activate_the_Product")
]