from flask import Flask, redirect, url_for, session, render_template, request
import speech_recognition as sr

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    transcript=""
    if request.method=="POST":
        if "file" not in request.files:
            return redirect(request.url)
        file= request.files['file']
        if file.filename=="":
           return redirect(request.url)
        if file:
            recognizer= sr.Recognizer()
            audioFile= sr.AudioFile(file)
            with audioFile as source:
                data=recognizer.record(source)
            transcript= recognizer.recognize_google(data, key=None)
        return render_template("index.html", transcript= transcript)

    return render_template("index.html")




if __name__=='__main__':
    app.run(debug=True, threaded=True)


