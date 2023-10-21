from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
capture = PiRGBArray(camera)
# allow the camera to warm up
time.sleep(1.0)
camera.capture(capture, format="bgr")
image = capture.array
# show image until a key is pressed
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
