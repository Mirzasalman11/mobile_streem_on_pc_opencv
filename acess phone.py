# # Import essential libraries 
# import requests 
# import cv2 
# import numpy as np 
# import imutils 

# # Replace the below URL with your own. Make sure to add "/shot.jpg" at last. 
# url = "http://192.168.137.128:8080/shot.jpg"

# # While loop to continuously fetching data from the Url 
# while True: 
# 	img_resp = requests.get(url) 
# 	img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
# 	img = cv2.imdecode(img_arr, -1) 
# 	img = imutils.resize(img, width=1000, height=1800) 
# 	cv2.imshow("Android_cam", img) 

# 	# Press Esc key to exit 
# 	if cv2.waitKey(1) == 27: 
# 		break

# cv2.destroyAllWindows() 









import cv2
import imutils
import time



url = "http://192.168.43.218:8080/video"

cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    if not ret:
        break



    cv2.imshow("Android_cam", frame)

    time.sleep(0.0001)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()









