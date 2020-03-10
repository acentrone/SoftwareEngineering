from flask_wtf import FlaskForm, Form
from wtforms import SubmitField, SelectField
#if we end up creating more wt form classes we will hae to import
#more parts of wtforms


#this is a wt forms class that consists of just
#a submit button that has the label "Record"
#When this form is submitted the speech to text process
#will be called
class RecordButton(FlaskForm):
    #Anthony Centrone - Language option drop down menu for the user to choose their target language
    #'thelang' is used in app.py as input for the google translate API
    thelang = SelectField(label='Languages', choices=[('fr', 'French'), ('ja', 'Japanese'), ('es', 'Spanish'), ('it', 'Italian'),
                                                      ('zh-hk', 'Chinese'), ('ko', 'Korean'), ('ru', 'Russian'), ('de', 'German')])
    record = SubmitField(label='Record')



#this is a wt form that consists of a drop down menu where users
#can select a target language from
