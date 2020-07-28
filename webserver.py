from flask import Flask, render_template
from flask_socketio import SocketIO,send,emit
from flask import render_template
import cv2 
import base64
from threading import Thread
from time import sleep

def call_at_interval(period, callback, args):
    while True:
        sleep(period)
        callback(*args)

def setInterval(period, callback, *args):
    Thread(target=call_at_interval, args=(period, callback, args)).start()

# wCap = cv2.VideoCapture('http://192.168.1.3:4747/video')
wCap = cv2.VideoCapture(0)
wCap.set(cv2.CAP_PROP_FRAME_WIDTH,600)
wCap.set(cv2.CAP_PROP_FRAME_HEIGHT,600)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
camstat = "OFF"
FPS = 20

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gambar')
def gambar():
    retval, image = wCap.read()
    retval, buffer = cv2.imencode('.jpg', image)
    data = base64.b64encode(buffer)
    # wCap.release()
    return data




def hello(word):
    retval, image = wCap.read()
    retval, buffer = cv2.imencode('.jpg', image)
    data = base64.b64encode(buffer)
    socketio.emit('kirei', data)

# def cameraOff(arg):
#     print('camera mati')
#     wCap.release()

setInterval(1/FPS, hello, '')


        
        

if __name__ == '__main__':
    socketio.run(app)
    