from flask import Flask
from flask import render_template
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    sounds = ['alpha-beta.wav', 'gamma-delta.wav']
    return render_template('index.html', sounds=sounds) # send tuples

def test():
    [ user, password ] = get_cred
    cmd = [ 'sshpass', '-p', password, 'ssh',
            '-o', 'StrictHostKeyChecking=no',
            '-o', 'UserKnownHostsFile=/dev/null',
            user, 'mpg123 chime.mp3' ]
    p = subprocess.call(cmd)
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
