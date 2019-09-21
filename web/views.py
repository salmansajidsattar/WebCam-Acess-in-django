from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2 as cv
import imutils
from django.http import request
# Create your views here.
def index(request):
    return render(request,'index.html')

def VidFeed(request):
    return StreamingHttpResponse(Main(),content_type='multipart/x-mixed-replace;boundary=frame')
def Main():
    print("[INFO] starting video stream...")
    cap = cv.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        #print(frame)
        # frame=imutils.rotate(frame,270)
        if ret is False:
            break
        frame = imutils.resize(frame, width=600)
        (h, w) = frame.shape[:2]
        imgencode = cv.imencode('.jpg', frame)[1]
        stringData = imgencode.tostring()
        yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n' + stringData + b'\r\n')