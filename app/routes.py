from flask import Flask
from flask import render_template, request
from . import bot

app = Flask(__name__)
user_name = ""


@app.route('/', methods=['GET','POST'])
def index():

    
    if request.method == 'POST':
        MyApp = bot.App(request.form['ask'])
        MyApp.GooglGeo()
        MyApp.GooglMapFrame()
        MyApp.ReadSW()
        return render_template('home.html', response = MyApp.MediaWiki())
                    
    else:
        
        
        return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)