from deepface import DeepFace
import cv2
camera = cv2.VideoCapture(0)
cv2.waitKey(5000)
return_value, image = camera.read()
cv2.imwrite('opencv'+'.png', image)
cv2.imshow("opencv.png", image)
del(camera)
try:
    face_analysis = DeepFace.analyze(img_path = "opencv.png")
except:
    print("No face")
val = len(face_analysis)
print(val)
