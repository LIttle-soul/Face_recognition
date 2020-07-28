import cv2
import dlib

detector = dlib.get_frontal_face_detector()
#predictor = dlib.shape_predictor('./FaceInfomation/shape_predictor_68_face_landmarks.dat')

cap = cv2.VideoCapture(0)
cap.set(3, 480)
while cap.isOpened():
    flag, img_rd = cap.read()
    kk = cv2.waitKey(50)
    if kk == ord('q'):
        break
    img_gray = cv2.cvtColor(img_rd, cv2.COLOR_BGR2GRAY)
    faces = detector(img_gray, 0)
    for kk, d in enumerate(faces):
        cv2.rectangle(img_rd, tuple([d.left(), d.top()]), tuple([d.right(), d.bottom()]), (0, 255, 255), 5)
    cv2.imshow("camera", img_rd)
cap.release()
cv2.destroyAllWindows()