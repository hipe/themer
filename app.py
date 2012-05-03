from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    sounds = ['alpha-beta.wav', 'gamma-delta.wav']
    return render_template('index.html', sounds=sounds) # send tuples

if __name__ == '__main__':
    app.run(debug = True)
