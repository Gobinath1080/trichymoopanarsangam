
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration/',methods=['GET','POST'])
def registration():
    if request.method == 'POST':
        return request.form.get('email')
    return render_template('registration.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()

