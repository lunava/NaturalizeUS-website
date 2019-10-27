from flask import Flask,render_template

app = Flask(__name__, template_folder = 'templates')

@ app.route('/')
def starter():
    return render_template('main.html', title = 'home')
@app.route('/test-breakdown')
def breakdown():
    return render_template('test_breakdown.html', title = 'test_breakdown')

if __name__ == '__main__':
    app.run (host = '0.0.0.0', debug = True, use_reload = True)
