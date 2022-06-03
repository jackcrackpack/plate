import cv2 as cv

################################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv.CascadeClassifier("detect.xml")
minArea = 500
color = (255, 128, 128)
################################
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0
while True:
    success, img = cap.read()
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 128, 128), 2)
            cv.putText(img, "      ORZ       ", (x, y - 5),
                        cv.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y + h, x:x + w]
            cv.imshow("ROI", imgRoi)

    cv.imshow("Result", img)
    if cv.waitKey(1) & 0xFF == ord('p'):
        cv.imwrite("printed/plates"+str(count)+".png", imgRoi)
        cv.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv.FILLED)
        cv.putText(img, "printed saved", (150, 265), cv.FONT_HERSHEY_DUPLEX,
                    2, (0, 0, 255), 2)
        cv.imshow("result", img)
        cv.waitKey(500)
        count += 1
