import cv2
from simple_facerec import SimpleFacerec

#Encode all faces

sfr = SimpleFacerec()
sfr.load_encoding_images('C:/Users/dkhan/Desktop/Python VSCode/Face Software Slow/Images')
cap = cv2.VideoCapture(1)


while True:
    ret, frame = cap.read()
    
    #Detect the person
    face_location, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_location, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        
        cv2.putText(frame, name , (x1, y1-10), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,255), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
    
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    if(key == 'q'):
        break
    
cap.release()
cv2.destroyAllWindows()