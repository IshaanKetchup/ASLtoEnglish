from flask import Flask, render_template, Response
import cv2
import mediapipe as mp

app = Flask(__name__)

# Initialize Mediapipe Hands
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

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
        return "A"

    if(handpoints[4].y > handpoints[9].y and
       handpoints[4].x < handpoints[5].x and 
       handpoints[4].x > handpoints[13].x and
       handpoints[8].y < handpoints[6].y and
       handpoints[12].y < handpoints[10].y and
       handpoints[16].y < handpoints[14].y and
       handpoints[20].y < handpoints[18].y):
        return "B"

    if(
    handpoints[4].x > handpoints[3].x and
    handpoints[3].x > handpoints[2].x and
    handpoints[4].y > handpoints[5].y and
  
    handpoints[5].y > handpoints[8].y and
    handpoints[8].y > handpoints[6].y and

    handpoints[9].y > handpoints[12].y and
    handpoints[12].y > handpoints[10].y and

    handpoints[13].y > handpoints[16].y and
    handpoints[16].y > handpoints[14].y and

    handpoints[17].y > handpoints[20].y and
    handpoints[20].y > handpoints[18].y):
      return "C"

    if (
        handpoints[5].y > handpoints[6].y and
        handpoints[6].y > handpoints[7].y and
        handpoints[7].y > handpoints[8].y and
        handpoints[12].y > handpoints[9].y and
        handpoints[16].y > handpoints[13].y and
        handpoints[3].x > handpoints[4].x):
            return "D"

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
         return 'E'
        #cv2.putText(image,"E",(10,30), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255),1)
    
    if(handpoints[0].y>handpoints[1].y and
        handpoints[9].y<handpoints[5].y and
        handpoints[9].y<handpoints[13].y and
        
        handpoints[20].y<handpoints[19].y and
        handpoints[19].y<handpoints[17].y and

        handpoints[16].y<handpoints[15].y and
        handpoints[15].y<handpoints[13].y and
        
        handpoints[12].y<handpoints[11].y and
        handpoints[11].y<handpoints[9].y and
        
        handpoints[6].y<handpoints[5].y and
        handpoints[6].y<handpoints[7].y and
        
        handpoints[8].y<handpoints[4].y and
        handpoints[8].x<handpoints[4].x):
        return "F"            
    #cv2.putText(image,"F",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)

    if(handpoints[8].x>handpoints[6].x and
       handpoints[4].x>handpoints[2].x and
       
       handpoints[2].y>handpoints[6].y and
       handpoints[2].y<handpoints[14].y and
       
       handpoints[0].x<handpoints[9].x and
       
       handpoints[12].x<handpoints[10].x and
       handpoints[16].x<handpoints[14].x and
       handpoints[20].x<handpoints[18].x and
       
       handpoints[3].y>handpoints[7].y):
        return "G"

    if(handpoints[5].x<handpoints[6].x and 
       handpoints[6].x<handpoints[7].x and

       handpoints[5].y<handpoints[9].y and

       handpoints[2].y<handpoints[4 ].y and

       handpoints[9].x<handpoints[10].x and
       handpoints[11].x<handpoints[12].x and

       handpoints[0].y<handpoints[17].y):
        return "H"

    if(handpoints[20].y<handpoints[18].y and
        
        handpoints[14].y<handpoints[13].y and
        handpoints[13].y<handpoints[16].y and
        
        handpoints[10].y<handpoints[9].y and
        handpoints[9].y<handpoints[12].y and
        
        handpoints[6].y<handpoints[5].y and
        handpoints[5].y<handpoints[8].y and
        
        handpoints[17].x<handpoints[13].x and
        handpoints[4].x>handpoints[7].x and
        
        handpoints[3].x>handpoints[2].x and
        handpoints[3].x>handpoints[4].x):
        return "I"

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
        return "K"
    
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
        return "L"

    if(handpoints[19].y>handpoints[17].y and
       handpoints[19].y<handpoints[20].y and
       
       handpoints[4].x<handpoints[15].x and
       handpoints[4].x<handpoints[11].x and
       handpoints[4].x<handpoints[7].x and

       handpoints[4].y<handpoints[15].y and
       handpoints[4].y<handpoints[11].y and
       handpoints[4].y<handpoints[7].y):
        return 'M'

    if (handpoints[19].y>handpoints[17].y and
        handpoints[19].y<handpoints[20].y and
        
        handpoints[15].y>handpoints[13].y and
        handpoints[15].y<handpoints[16].y and
        
        handpoints[4].x<handpoints[12].x and
        handpoints[4].x<handpoints[8].x and
        
        handpoints[4].y<handpoints[12].y and
        handpoints[4].y<handpoints[8].y):
        return 'N'

    if(handpoints[18].y<handpoints[17].y and
        handpoints[18].y<handpoints[19].y and
                    
            handpoints[14].y<handpoints[13].y and
            handpoints[14].y<handpoints[15].y and
            
            handpoints[10].y<handpoints[9].y  and
            handpoints[10].y<handpoints[11].y and
            
            handpoints[6].y<handpoints[5].y and
            handpoints[6].y<handpoints[7].y and
            
            handpoints[1].y>handpoints[3].y and
            
            handpoints[4].y>handpoints[7].y and
            handpoints[4].y<handpoints[8].y):
        return 'O'

    if(handpoints[0].y<handpoints[1].y and
        
        handpoints[5].y<handpoints[7].y and
        handpoints[7].y<handpoints[8].y and

        handpoints[9].y<handpoints[11].y and
        handpoints[11].y<handpoints[12].y and

        handpoints[18].y>handpoints[19].y and
        handpoints[18].y>handpoints[17].y and
        handpoints[17].y<handpoints[20].y and

        handpoints[1].y<handpoints[3].y and
        handpoints[3].y<handpoints[4].y and
        handpoints[4].x>handpoints[10].x and
        handpoints[4].x<handpoints[6].x):
        return "P"

    if(handpoints[17].y<handpoints[18].y and
        handpoints[18].y>handpoints[20].y and
        
        handpoints[13].y<handpoints[14].y and
        handpoints[14].y>handpoints[16].y and
        
        handpoints[9].y<handpoints[10].y and
        handpoints[10].y>handpoints[12].y and
        
        handpoints[6].y<handpoints[8].y and
        
        handpoints[4].x>handpoints[8].x):
        return "Q"
    if(handpoints[19].y<handpoints[20].y and
        handpoints[19].y>handpoints[17].y and
        
        handpoints[15].y<handpoints[16].y and
        handpoints[15].y>handpoints[14].y and
        
        handpoints[12].y<handpoints[9].y and
        handpoints[8].y<handpoints[6].y and
        
        handpoints[8].x<handpoints[12].x and
        
        handpoints[4].x<handpoints[2].x):
        return "R"

    if (handpoints[4].x < handpoints[3].x and
                handpoints[3].y < handpoints[2].y and
                handpoints[2].x > handpoints[0].x and
                handpoints[19].y > handpoints[18].y and
                handpoints[15].y > handpoints[14].y and
                handpoints[20].y > handpoints[17].y and
                handpoints[16].y > handpoints[13].y and
                handpoints[12].y > handpoints[9].y and
                handpoints[8].y > handpoints[5].y and
                handpoints[4].y > handpoints[10].y and
                handpoints[11].y > handpoints[10].y and
                handpoints[4].x >  handpoints[14].x and
                handpoints[10].x > handpoints[4].x):
                return "S"

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
        return "T"

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
            return "V"
        else:
            return "U"

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
        return "W"

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
        return "X"
    
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
       return "Y"

    
def which_hand(results):
    for i in results.multi_handedness:
        return (str(i).split()[-2].strip(f'"'))


@app.route('/')
def index():
    return render_template('index2.html')

def hand_tracking():
    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            lt = ''
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
                    
                    if(which_hand(results)=='Left'):
                        lt = letter(handpoints, image)
            image = cv2.flip(image,1)
            cv2.putText(image,lt,(10,30), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 1)
            ret, jpeg = cv2.imencode('.jpg', image)
            frame_bytes = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()

@app.route('/video_feed')
def video_feed():
    return Response(hand_tracking(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
