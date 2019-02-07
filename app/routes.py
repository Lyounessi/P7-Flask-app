from flask import Flask
from flask import render_template, request

app = Flask(__name__)
user_name = ""

@app.route('/', methods=['GET','POST'])
def index():
    
    
    if request.method == 'POST':
        response = request.form['ask']
        return render_template('home.html', response = response)
    else:
        return render_template('home.html')
if __name__ == "__main__":
    app.run(debug=False)