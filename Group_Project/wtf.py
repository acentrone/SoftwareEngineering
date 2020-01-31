from flask_wtf import FlaskForm
from wtforms import SubmitField
#if we end up creating more wt form classes we will hae to import
#more parts of wtforms


#this is a wt forms class that consists of just
#a submit button that has the label "Record"
#When this form is submitted the speech to text process
#will be called
class RecordButton(FlaskForm):
    record = SubmitField(label='Record')