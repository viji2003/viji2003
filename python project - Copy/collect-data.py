import cv2
import numpy as np
import os

# Create the directory structure
if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    os.makedirs("data/train/a")
    os.makedirs("data/train/b")
    os.makedirs("data/train/c")
    os.makedirs("data/train/d")
    os.makedirs("data/train/e")
    os.makedirs("data/train/f")
    os.makedirs("data/test/a")
    os.makedirs("data/test/b")
    os.makedirs("data/test/c")
    os.makedirs("data/test/d")
    os.makedirs("data/test/e")
    os.makedirs("data/test/f")
    
    

# Train or test 
mode = 'TRAIN'
directory = 'data/'+mode+'/'

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Getting count of existing images
    count = {'a': len(os.listdir(directory+"/a")),
             'b': len(os.listdir(directory+"/b")),
             'c': len(os.listdir(directory+"/c")),
             'd': len(os.listdir(directory+"/d")),
             'e': len(os.listdir(directory+"/e")),
             'f': len(os.listdir(directory+"/f"))}
    
    # Printing the count in each set to the screen
    cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "A : "+str(count['a']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "B : "+str(count['b']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "C : "+str(count['c']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "D : "+str(count['d']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "E : "+str(count['e']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "F : "+str(count['f']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    
    
    # Coordinates of the ROI
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (310,310)) 
 
    cv2.imshow("Frame", frame)
    
    #_, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)
    #kernel = np.ones((1, 1), np.uint8)
    #img = cv2.dilate(mask, kernel, iterations=1)
    #img = cv2.erode(mask, kernel, iterations=1)
    # do the processing after capturing the image!
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
   # _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'a/'+str(count['a'])+'.jpg', roi)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'b/'+str(count['b'])+'.jpg', roi)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'c/'+str(count['c'])+'.jpg', roi)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(directory+'d/'+str(count['d'])+'.jpg', roi)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory+'e/'+str(count['e'])+'.jpg', roi)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(directory+'f/'+str(count['f'])+'.jpg', roi)
        
    
cap.release()
cv2.destroyAllWindows()

