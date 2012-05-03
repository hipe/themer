from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    arr = ['alpha-beta.wav', 'gamma-delta.wav']
    output = ''
    for name in arr:
        output += ("ok: " + name)
    return output + "Hello World!!"

if __name__ == '__main__':
    app.run(debug = True)
