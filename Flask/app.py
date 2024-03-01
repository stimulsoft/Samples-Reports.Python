import os
from flask import Flask, render_template, send_from_directory
from views import *

app = Flask(__name__)
app.register_blueprint(Showing_a_Report_in_the_Viewer)
app.register_blueprint(Showing_a_Report_in_the_Viewer_in_an_HTML_template)
app.register_blueprint(Editing_a_Report_Template_in_the_Designer)
app.register_blueprint(Editing_a_Report_Template_in_the_Designer_in_an_HTML_template)
app.register_blueprint(Exporting_a_Report_from_Code)
app.register_blueprint(Registering_a_Data_from_Code)
app.register_blueprint(How_to_Activate_the_Product)
app.register_blueprint(Registering_Data_when_Creating_a_New_Report)
app.register_blueprint(Rendering_a_Report_from_Code)
app.register_blueprint(Using_a_Handler_in_a_Separate_Function)
app.register_blueprint(Working_with_onDesign_and_onExit_events)
app.register_blueprint(Changing_an_Export_Settings_on_the_Server_Side)
app.register_blueprint(Changing_the_Viewer_Theme)
app.register_blueprint(Localizing_the_Designer)
app.register_blueprint(Opening_the_Report_in_the_Viewer_and_Changing_it_on_the_Server_Side)
app.register_blueprint(Saving_a_Report_Template_on_the_Server_Side)
app.register_blueprint(Sending_a_Report_by_Email)
app.register_blueprint(Sending_an_Exported_Report_to_the_Server_Side)
app.register_blueprint(Setting_Report_Variables_on_the_Server_Side)
app.register_blueprint(Using_Parameters_in_SQL_Query)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
     return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True, port=8040)