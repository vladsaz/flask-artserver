from flask import Flask, render_template, make_response, Response, jsonify
from video import Video
import json, base64


app = Flask(__name__)

def gen(video):
    while True:
        frame = video.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/angular', methods=['GET'])
def angular():
    resp = make_response(open('images/img1.png', 'rb').read())
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/video')
def video_feed():
    resp = Response(gen(Video()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/dogs')
def dogs():
    resp = make_response(open('data/dogs.json', 'rb').read())
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/base64')
def to_base():
    my_file = open('images/img1.png', 'rb').read()
    encoded_file = base64.b64encode(my_file).decode('ascii')
    resp = make_response(encoded_file)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    
    return resp


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
