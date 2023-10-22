from imutils.video import VideoStream
import datetime
import imutils
import time
import cv2

T = 50
min_area = 1000
background = None

video_path = None
if video_path is None:
    vs = VideoStream().start()
    # warm up the camera
    time.sleep(2)
else:
    vs = cv2.VideoCapture(video_path)

while True:
    frame = vs.read()
    frame = frame if video_path is None else frame[1]
    # this variable keeps track the state of motion detection
    state = "No change"
    # if there is no more frame in the video break the loop
    if frame is None:
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # smooting image in 21x21 pixels regions
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # if the average frame is None, initialize it
    if background is None:
        background = gray.copy().astype("float")
        continue

    delta_frame = cv2.absdiff(gray, cv2.convertScaleAbs(background))
    threshold = cv2.threshold(delta_frame, T, 255,
                              cv2.THRESH_BINARY)[1]

    threshold = cv2.dilate(threshold, None, iterations=2)

    cnts = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv2.contourArea(c) < min_area:
            continue

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        state = "New object"

    cv2.accumulateWeighted(gray, background, 0.5)

    cv2.putText(frame, "Room Status: {}".format(state), (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    cv2.imshow("Camera image", frame)
    cv2.imshow("Threshold", threshold)
    cv2.imshow("Delta frame", delta_frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

# shut down the camera and close all open windows
vs.stop() if video_path is None else vs.release()
cv2.destroyAllWindows()
