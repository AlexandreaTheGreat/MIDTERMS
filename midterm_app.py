from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_app():
    return render_template('login.html')

@app.route('/registration.html')
def register():
    return render_template('registration.html')

if __name__ == '__main__':
    app.run()