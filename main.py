import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


img=cv2.imread('2.png')
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))

himg,wimg,_=img.shape

# boxes = pytesseract.image_to_boxes(img) #for letters
# for b in boxes.splitlines():
#     b = b.split(' ')
#     x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img , (x,himg-y) , (w,himg-h) , (0,0,255) , 2)
#     #print(b[0])
#     cv2.putText(img , b[0] , (x , himg-y+25) , cv2.FONT_HERSHEY_PLAIN , 1 , (50,50,255) , 2)

# boxes = pytesseract.image_to_data(img) #for words
# for x,b in enumerate(boxes.splitlines()):
#     if (x!=0):
#         b = b.split()
#         if len(b)==12:
#             x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
#             cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 1)
#             print(b[11])
#             cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (50, 50, 255), 1)
cv2.imshow('result',img)
cv2.waitKey(0)