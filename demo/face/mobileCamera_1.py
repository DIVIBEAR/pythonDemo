import cv2
import numpy as np

cv2.namedWindow("camera")
video="http://admin:XXX@192.168.1.104:8081/"
cap = cv2.VideoCapture(video)
success, frame = cap.read()
color = (255,0,0)
classfier = cv2.CascadeClassifier(r'G:/python/Lib/haarcascades/haarcascade_frontalface_alt_tree.xml')
while success:
    success, frame = cap.read()
    size = frame.shape[:2]# 获得当前桢彩色图像的大小
    image = np.zeros(size, dtype=np.float16)
    #np.zeros(shape, dtype=float, order='C')
    # 参数：shape: 形状
    # dtype: 数据类型，可选参数，默认numpy.float64
    # dtype类型：t, 位域, 如t4代表4位
    # b, 布尔值，true or false
    # i, 整数, 如i8(64位）
    # u, 无符号整数，u8(64位）
    # f, 浮点数，f8（64位）
    # c, 浮点负数，
    # o, 对象，
    # s, a，字符串，s24
    # u, unicode, u24
    # order: 可选参数，c代表与C语言类似，行优先；F代表列优先
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.equalizeHist(image, image)
    divisor = 8
    h, w = size
    minSize = (w // divisor, h // divisor)
    faceRects = classfier.detectMultiScale(image, 1.1, 2 ,cv2.CASCADE_SCALE_IMAGE, minSize)
    #image：图片路径
    #1.1：被检测对象的尺度变化。尺度越大，越容易漏掉检测的对象，但检测速度加快；尺度越小，检测越细致准确，但检测速度变慢
    #2：数值越大，检测到对象的条件越苛刻，反之检测到对象的条件越宽松；
    #minSize：检测的对象最小尺寸，单位是像素*像素，使对象落在检测器的大小范围内；
    #maxSize：检测的对象最大尺寸，单位是像素 * 像素，使对象落在检测器的大小范围内。
    #cv2.CASCADE_SCALE_IMAGE：:scale0为比例系数，即被检测图像每一次被压缩的比例
    #说明：该方法返回的是一个列表，每个列表元素是长度为四的元组，分别表示脸部左上角的x，y值，脸部区域的宽度和高度。
    if len(faceRects) > 0:
        for faceRect in faceRects:
            x, y, w, h = faceRect
            cv2.rectangle(frame, (x, y), (x + w, y + h), color)
    cv2.imshow("camera", frame)
    key = cv2.waitKey(10)
    c = chr(key & 255)
    if c in ['q','Q', chr(27)]:
        break
cv2.destroyWindow("test")
