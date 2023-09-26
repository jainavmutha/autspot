from deepface import DeepFace
import cv2
cam_port = 0
cam = cv2.VideoCapture(cam_port)

class Detect():
    def capture(self):
        result, image = cam.read()
        cam.release()
        if result:
            #cv2.imshow("Harshitha", image)
            # cv2.imwrite("Harshitha.png", image)
            #cv2.waitKey(0)
            #cv2.destroyWindow("Harshitha")
            try:
                face_analysis = DeepFace.analyze(image)
                print(face_analysis[0]["dominant_emotion"])
                return face_analysis[0]["dominant_emotion"]
            except:
                return self.capture()

