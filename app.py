from flask import Flask, render_template, url_for, redirect, request
from speech2text import speech2text
from wtf import RecordButton

app = Flask(__name__)

#wtf forms requires a "secret key" for security purposes so i set it to
#a random string of 32 hex digits
app.config['SECRET_KEY'] = '4defe45c2481d91d4df5696f570525e2'


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
    #this says if the wt form is valid when the submit button is pressed.
    #there is nothing that can make our form invalid and our submit button
    #is really the "record" button. It's a bit of a janky setup but it works
    if form.validate_on_submit():
        #when the record button is pressed call the speech2text() function that
        #is in speech2text.py and save that interpreted text in the variable text
        text_conf = speech2text()
        text = text_conf['transcript']
        confidence = text_conf['confidence']
        #passing the wt form and the text variable to the html so that it can be displayed
        return render_template('translate.html', form=form, text=text, confidence=confidence)
    return render_template('translate.html', form=form, text=text)


@app.route("/team")
def team():
    return render_template('team.html')


if __name__ == '__main__':
    app.run(debug = True)
