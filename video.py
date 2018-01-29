import cv2

class Video(object):
    def __init__(self):
        #webcam
        self.video = cv2.VideoCapture(0)
        #video
        # self.video = cv2.VideoCapture('images/small.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        #encode to jpeg
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()