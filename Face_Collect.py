import cv2
import dlib
import os
import sys
import random

class Face_Collect():
    def __init__(self,):
        super().__init__()
        self.output_dir = './Image/'
        self.size = 64

    def add_Face(self, name,):
        self.output_dir += name
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)
        detector = dlib.get_frontal_face_detector()
        camera = cv2.VideoCapture(0)
        index = 1
        while True:
            if index <= 15:
                print('Being processed picture %s'% index)
                success,img = camera.read()
                gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                dets = detector(gray_img,1)
                for i,d in enumerate(dets):
                    x1 = d.top() if d.top() > 0 else 0
                    y1 = d.bottom() if d.bottom() > 0 else 0
                    x2 = d.left() if d.left() > 0 else 0
                    y2 = d.right() if d.right() > 0 else 0
                    face = img[x1:y1,x2:y2]
                    face = self.relight(face,random.uniform(0.5,1.5),random.randint(-50,50))
                    face = cv2.resize(face,(self.size,self.size))
                    cv2.imshow('image',face)
                    cv2.imwrite(self.output_dir+'/'+str(index)+'.jpg', face)
                    index += 1
                key = cv2.waitKey(30) & 0xff
                if key == 27:
                    break
            else:
                print('Finished!')
                camera.release()
                cv2.destroyAllWindows()
                break

    def relight(self,img,light = 1,bias = 0):
        w = img.shape[1]
        h = img.shape[0]

        for i in range(0,w):
            for j in range(0,h):
                for c in range(3):
                    tmp = int(img[j,i,c]*light+bias)
                    if tmp > 255:
                        tmp = 255
                    elif tmp < 0:
                        tmp = 0
                    img[j,i,c] = tmp
        return img