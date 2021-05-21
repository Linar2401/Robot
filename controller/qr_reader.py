import cv2
import datetime

qrDecoder = cv2.QRCodeDetector()


def qr_recognize():
    t_s = datetime.datetime.now()
    cap = cv2.VideoCapture('/dev/video0')
    # ret, frame = cap.read()
    # frame = cv2.imread('qrcode.png')
    # cv2.imshow('frame', frame)
    # cap.release()

    flag = True
    t_f = datetime.datetime.now()
    td = t_f - t_s
    data = None
    while flag and td.seconds < 10:
        ret, frame = cap.read()
        data, bbox, rectifiedImage = qrDecoder.detectAndDecode(frame)
        if len(data) > 0:
            # print("Decoded Data : {}".format(data))
            flag = False
        else:
            # print("QR Code not detected")
            t_f = datetime.datetime.now()
            td = t_f - t_s

    cap.release()
    cv2.destroyAllWindows()
    if flag:
        return 1
    return data
