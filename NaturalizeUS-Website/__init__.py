from flask import Flask,render_template

app = Flask(__name__, template_folder = 'templates')

@ app.route('/')
def starter():
    return render_template('main.html', title = 'home')

if __name__ == '__main__':
    app.run (host = '0.0.0.0', debug = True, use_reload = True)
