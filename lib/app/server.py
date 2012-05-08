from flask import Flask
from flask import render_template
from flask import url_for
import subprocess
import os
import app.constant
from app.sound import Sound


server = Flask(__name__)

# server.sounds_dir = os.path.join(os.path.dirname(__file__), app.constant.SOUNDS_DIR)
def sounds_dir():
    return os.path.join(os.path.dirname(__file__), app.constant.SOUNDS_DIR)

def sounds():
    for dirname, _dirnames, filenames in os.walk(sounds_dir()):
        _filtered = filter(lambda x: app.constant.SOUND_RE.search(x), filenames)
        _res = map(lambda x: Sound(x, dirname), _filtered)
        return _res

@server.route('/')
def index():
    _sounds = sounds()
    return render_template('index.html', sounds=_sounds, no_sounds=(0 == len(_sounds)))

def test():
    [ user, password ] = get_cred
    cmd = [ 'sshpass', '-p', password, 'ssh',
            '-o', 'StrictHostKeyChecking=no',
            '-o', 'UserKnownHostsFile=/dev/null',
            user, 'mpg123 chime.mp3' ]
    p = subprocess.call(cmd)
    return 'OK'

# if __name__ == '__main__':
#     server.run(host='0.0.0.0', debug = True)

