from imutils.video import VideoStream
import imutils
import datetime
import argparse
import time
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-p", "--picamera", type=int, default=-1,
                help="Picamera or the USB camera will be used")
args = vars(ap.parse_args())

vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)


while True:
    # acquire a frame from the video stream and resize it
    # to have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    # draw the timestamp on the frame
    timestamp = datetime.datetime.now()
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(frame, ts, (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    # show the frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# cleanup – close window(s) and stop video stream
cv2.destroyAllWindows()
vs.stop()
