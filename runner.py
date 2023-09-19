import mediapipe as mp 
import cv2 

mp_drawing = mp.solutions.drawing_utils 
mp_hands = mp.solutions.hands
print('________START__________')
capture = cv2.VideoCapture(0)
    

def fob(handpoints, image):
    if(handpoints[4].x>handpoints[20].x):
        if(handpoints[12].y < handpoints[0].y):
            cv2.putText(image,"FRONT",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        else:
            cv2.putText(image,"BACK",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
            
    elif(handpoints[4].x<handpoints[20].x):
        if(handpoints[12].y < handpoints[0].y):
            cv2.putText(image,"BACK",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        else:
            cv2.putText(image,"FRONT",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)

def letter(handpoints, image):

    if(handpoints[2].y > handpoints[3].y and
       handpoints[3].y > handpoints[4].y and
       handpoints[3].x > handpoints[7].x and

       handpoints[19].y > handpoints[17].y and
       handpoints[17].y > handpoints[18].y and

       handpoints[15].y > handpoints[13].y and
       handpoints[13].y > handpoints[14].y and

       handpoints[11].y > handpoints[9].y and
       handpoints[9].y > handpoints[10].y and

       handpoints[19].y > handpoints[17].y and
       handpoints[17].y > handpoints[18].y and

       handpoints[12].y > handpoints[2].y and
       handpoints[16].y > handpoints[2].y):
        cv2.putText(image,"A",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)

    if(handpoints[4].y > handpoints[9].y and
       handpoints[4].x < handpoints[5].x and 
       handpoints[4].x > handpoints[13].x and
       handpoints[8].y < handpoints[6].y and
       handpoints[12].y < handpoints[10].y and
       handpoints[16].y < handpoints[14].y and
       handpoints[20].y < handpoints[18].y):
        cv2.putText(image,"B",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)


    if (
        handpoints[4].x < handpoints[3].x and
        handpoints[3].x < handpoints[2].x and
        handpoints[6].y < handpoints[5].y and
        handpoints[7].y < handpoints[6].y and
        handpoints[8].y < handpoints[7].y and
        handpoints[15].y < handpoints[16].y and
        handpoints[13].y < handpoints[16].y and
        handpoints[10].y < handpoints[9].y and
        handpoints[12].y < handpoints[10].y
        ):
        if((handpoints[10].x < handpoints[9].x and handpoints[11].x < handpoints[9].x and handpoints[12].x < handpoints[9].x) and
        (handpoints[5].x < handpoints[6].x and handpoints[5].x < handpoints[7].x and handpoints[5].x < handpoints[8].x)):
            cv2.putText(image,"V",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        else:
            cv2.putText(image, "U", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)

        
    if(handpoints[2].y > handpoints[3].y and
        handpoints[3].y > handpoints[4].y and
        handpoints[8].x > handpoints[4].x and
        handpoints[8].y > handpoints[7].y and
        handpoints[15].y > handpoints[13].y and
        handpoints[13].y > handpoints[14].y and
        handpoints[11].y > handpoints[9].y and
        handpoints[9].y > handpoints[10].y and
        handpoints[19].y > handpoints[17].y and
        handpoints[17].y > handpoints[18].y and
        handpoints[12].y > handpoints[2].y and
        handpoints[16].y > handpoints[2].y):
            cv2.putText(image,"T",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)

    if(
    #thumb.x
    handpoints[4].x>handpoints[3].x and
    handpoints[3].x>handpoints[2].x and
    handpoints[2].x>handpoints[1].x and
    #index.x
    handpoints[8].x > handpoints[7].x and
    handpoints[7].x > handpoints[6].x and
    handpoints[6].x > handpoints[5].x and
    #index.y
    handpoints[8].y > handpoints[7].y and
    handpoints[7].y > handpoints[6].y and
    handpoints[5].y > handpoints[6].y and
    #middle.x
    handpoints[12].x > handpoints[11].x and
    handpoints[11].x > handpoints[10].x and
    handpoints[10].x > handpoints[9].x and
    #middle.y
    handpoints[12].y > handpoints[11].y and
    handpoints[11].y > handpoints[10].y and
    handpoints[9].y > handpoints[10].y and
    #ring.x
    handpoints[16].x > handpoints[15].x and
    handpoints[15].x > handpoints[14].x and
    handpoints[14].x > handpoints[13].x and
    #ring.y
    handpoints[16].y > handpoints[15].y and
    handpoints[15].y > handpoints[14].y and
    handpoints[13].y > handpoints[14].y and
    #pinky.x
    handpoints[20].x > handpoints[19].x and
    handpoints[19].x > handpoints[18].x and
    handpoints[18].x > handpoints[17].x and
    #pinky.y
    handpoints[20].y > handpoints[19].y and
    handpoints[19].y > handpoints[18].y and
    handpoints[17].y > handpoints[18].y):
        cv2.putText(image,"C",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
    
    if(
        handpoints[8].y>handpoints[5].y and
        handpoints[8].y>handpoints[7].y and
        handpoints[8].y>handpoints[6].y and
        handpoints[7].y>handpoints[6].y and

        handpoints[12].y<handpoints[11].y and
        handpoints[11].y<handpoints[10].y and
        handpoints[10].y<handpoints[9].y and
        
        handpoints[16].y<handpoints[15].y and
        handpoints[15].y<handpoints[14].y and
        handpoints[14].y<handpoints[13].y and
        
        handpoints[20].y<handpoints[19].y and
        handpoints[19].y<handpoints[18].y and
        handpoints[18].y<handpoints[17].y and

        handpoints[4].x<handpoints[3].x and
        handpoints[3].x<handpoints[2].x and
        handpoints[2].x<handpoints[1].x 

        #do y
        
    ):
        cv2.putText(image,"F",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
    
    if(handpoints[5].x<handpoints[6].x and 
       handpoints[6].x<handpoints[7].x and

       handpoints[5].y<handpoints[9].y and

       handpoints[2].y<handpoints[4 ].y and

       handpoints[9].x<handpoints[10].x and
       handpoints[11].x<handpoints[12].x and

       handpoints[0].y<handpoints[17].y):
        cv2.putText(image,"H",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)

    if(handpoints[8].y<handpoints[6].y and
       handpoints[6].y<handpoints[5].y and
       
       handpoints[12].y<handpoints[11].y and
       handpoints[11].y<handpoints[9].y and
       
       handpoints[4].x>handpoints[9].x and
       handpoints[4].x<handpoints[5].x and
       
       handpoints[15].y>handpoints[14].y and
       handpoints[13].y>handpoints[14].y and
       
       handpoints[4].y<handpoints[9].y and
       
       handpoints[20].y>handpoints[18].y and
       handpoints[16].y>handpoints[14].y and
       handpoints[19].y>handpoints[17].y and
       handpoints[15].y>handpoints[13].y):
        cv2.putText(image,"K",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
    
    if(handpoints[4].x > handpoints[3].x and
       handpoints[3].x > handpoints[2].x and
       handpoints[17].y > handpoints[18].y and
       handpoints[18].y > handpoints[19].y and
       handpoints[19].y > handpoints[20].y and
       handpoints[13].y > handpoints[14].y and
       handpoints[15].y > handpoints[13].y and
       handpoints[9].y > handpoints[10].y and
       handpoints[11].y > handpoints[9].y and
       handpoints[5].y > handpoints[6].y and
       handpoints[7].y > handpoints[5].y):
       cv2.putText(image,"Y",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)
    
    if(handpoints[3].x > handpoints[4].x and
       handpoints[2].y > handpoints[3].y and
       handpoints[8].x > handpoints[7].x and
       handpoints[7].x > handpoints[6].x and
       handpoints[7].y > handpoints[8].y and
       handpoints[10].x > handpoints[9].x and
       handpoints[11].x > handpoints[10].x and
       handpoints[10].x > handpoints[12].x and
       handpoints[14].x > handpoints[13].x and
       handpoints[15].x > handpoints[14].x and
       handpoints[14].x > handpoints[16].x and
       handpoints[18].x > handpoints[17].x and
       handpoints[19].x > handpoints[18].x and
       handpoints[18].x > handpoints[20].x):
        cv2.putText(image,"X",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)

    if(handpoints[3].x > handpoints[4].x and
       handpoints[2].x > handpoints[3].x and
       handpoints[4].y > handpoints[16].y and
       handpoints[17].y > handpoints[19].y and
       handpoints[19].y > handpoints[18].y and
       handpoints[13].y > handpoints[15].y and
       handpoints[15].y > handpoints[14].y and
       handpoints[9].y > handpoints[11].y and
       handpoints[11].y > handpoints[10].y and
       handpoints[17].y > handpoints[19].y and
       handpoints[19].y > handpoints[18].y):
        cv2.putText(image,"E",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)
    
    if (handpoints[4].x > handpoints[3].x and
            handpoints[3].x > handpoints[2].x and
            handpoints[0].x > handpoints[17].x and

            handpoints[6].y < handpoints[5].y and
            handpoints[7].y < handpoints[6].y and
            handpoints[8].y < handpoints[7].y and

            handpoints[10].y < handpoints[9].y and
            handpoints[9].y < handpoints[12].y and
            handpoints[14].y < handpoints[13].y and
            handpoints[13].y < handpoints[16].y and

            handpoints[19].y < handpoints[20].y and
            handpoints[17].y < handpoints[20].y):
        cv2.putText(image, "L", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),1)

    if (handpoints[3].x > handpoints[4].x and
            handpoints[2].x > handpoints[3].x and
            handpoints[0].x > handpoints[17].x and

            handpoints[6].y < handpoints[5].y and
            handpoints[7].y < handpoints[6].y and
            handpoints[8].y < handpoints[7].y and

            handpoints[10].y < handpoints[9].y and
            handpoints[12].y < handpoints[10].y and
            handpoints[14].y < handpoints[13].y and
            handpoints[16].y < handpoints[14].y and

            handpoints[19].y < handpoints[20].y and
            handpoints[17].y < handpoints[20].y):
        cv2.putText(image, "W", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),1)
    
def which_hand():
    for i in results.multi_handedness:
        return (str(i).split()[-2].strip(f'"'))

with mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence=0.5) as hands:
    while capture.isOpened():
        ret, frame = capture.read()

        #Detections
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable=False
        results = hands.process(image)  
        
        image.flags.writeable=True
        image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)

                handpoints = {0:hand.landmark[mp_hands.HandLandmark.WRIST],
                              1: hand.landmark[mp_hands.HandLandmark.THUMB_CMC],
                              2: hand.landmark[mp_hands.HandLandmark.THUMB_MCP],
                              3: hand.landmark[mp_hands.HandLandmark.THUMB_IP],
                              4: hand.landmark[mp_hands.HandLandmark.THUMB_TIP],
                              5: hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP],
                              6: hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP],
                              7: hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP],
                              8: hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP],
                              9: hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP],
                              10: hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP],
                              11: hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP],
                              12: hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
                              13: hand.landmark[mp_hands.HandLandmark.RING_FINGER_MCP],
                              14: hand.landmark[mp_hands.HandLandmark.RING_FINGER_PIP],
                              15: hand.landmark[mp_hands.HandLandmark.RING_FINGER_DIP],
                              16: hand.landmark[mp_hands.HandLandmark.RING_FINGER_TIP],
                              17: hand.landmark[mp_hands.HandLandmark.PINKY_MCP],
                              18: hand.landmark[mp_hands.HandLandmark.PINKY_PIP],
                              19: hand.landmark[mp_hands.HandLandmark.PINKY_DIP],
                              20: hand.landmark[mp_hands.HandLandmark.PINKY_TIP]} 
                #fob(handpoints)
                #print(which_hand())
                if(which_hand()=='Left'):
                    letter(handpoints,image)
                    '''print(handpoints)          
                    print()'''

        cv2.imshow('Hand Tracking', image)
        if cv2.waitKey(10) & 0xFF==ord('x'):
            break

    capture.release()
    cv2.destroyAllWindows()


print('------------------END-----------------')