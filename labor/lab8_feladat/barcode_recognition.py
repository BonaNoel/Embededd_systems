from pyzbar import pyzbar
import cv2

image_path = "/home/noel/beagyazott_rendszerek/labor/lab8_feladat/barcode.png"
image = cv2.imread(image_path)
barcodes = pyzbar.decode(image)

for barcode in barcodes:
    # draw bounding box around the detected object
    (x, y, w, h) = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # the barcode data is a bytes object so if we want to draw it on
    # our output image we need to convert it to a string first
    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type
    # draw the barcode description and type on the image
    text = "{} ({})".format(barcodeData, barcodeType)
    cv2.putText(image, text, (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
