from flask import Flask, render_template, url_for, redirect, request
from speech2text import speech2text
from wtf import RecordButton
import os, json
from google.cloud import translate_v2 as translator

app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"

#wtf forms requires a "secret key" for security purposes so i set it to
#a random string of 32 hex digits
app.config['SECRET_KEY'] = '4defe45c2481d91d4df5696f570525e2'

# get path to base directory that the project is in
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# constructs the rest of the path, this is a little janky, but works for now
credential_path = os.path.join(BASE_DIR, "Group_Project")
credential_path = os.path.join(credential_path, "CloudKey_SEClassProj.json")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html')



#have to have the methods post and get here since we are asking for
#input from the user
@app.route('/translate', methods=['POST', 'GET'])
def translate():

    #setting form to the RecordButton wt form that we created in wtf.py
    form = RecordButton()

    text = ""

    #target language is french until the drop down menu changes it
    target = 'fr'


    #this says if the wt form is valid when the submit button is pressed.
    #there is nothing that can make our form invalid and our submit button
    #is really the "record" button. It's a bit of a janky setup but it works
    if form.validate_on_submit():
        #when the record button is pressed call the speech2text() function that
        #is in speech2text.py and save that interpreted text in the variable text
        text_conf = speech2text()
        text = text_conf['transcript']
        confidence = text_conf['confidence']

        #translation begins
        translate_client = translator.Client()

        target = form.thelang.data  # translation to user selected language

        result = translate_client.translate(text, target_language=target )

        #passing the wt form and the text variable to the html so that it can be displayed
        return render_template('translate.html', form=form, oldtext=text, confidence=confidence,
                               newtext=result['translatedText'])
    return render_template('translate.html', form=form, text=text)



@app.route("/team")
def team():
    return render_template('team.html')


if __name__ == '__main__':
    app.run(debug = True)
