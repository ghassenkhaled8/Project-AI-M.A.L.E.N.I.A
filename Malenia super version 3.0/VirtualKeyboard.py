import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller, Key


cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=int(0.8))
keys =[["Q","W","E","R","T","Y","U","I","O","P"],
       ["A","S","D","F","G","H","J","K","L",";"],
       ["Z","X","C","V","B","N","M",",",".","/"]]
finalText =""

keyboard = Controller()

def drawAll(img, buttonList):
    
    for button in buttonList :
        x,y =button.pos
        w,h =button.size
        cvzone.cornerRect(img,(button.pos[0],button.pos[1],button.size[0],button.size[1]),20,rt=0)
        cv2.rectangle(img,button.pos,(x+w,y+h),(252,237,218), cv2.FILLED)
        cv2.putText(img, button.text , (x+20,y+65),
        cv2.FONT_HERSHEY_PLAIN,4,(238,78,52),4)
        
        # Add title
        cv2.putText(img, "Keyboard", (350, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, lineType=cv2.LINE_AA)
        
        # Add author's name
        cv2.putText(img, "Realized by Ghassen Khaled", (250, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, lineType=cv2.LINE_AA)
        
        # Add LinkedIn information
        cv2.putText(img, "LinkedIn: Ghassen-Khaled", (180, 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, lineType=cv2.LINE_AA)

    return img

class Button():
    def __init__(self, pos,text, size=[85,85]):
        self.pos = pos
        self.size = size
        self.text = text
        

buttonList = []
for i in range(len(keys)) :
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([j*100+50,100*i+50+200],key))
        
# Add delete button
deleteButton = Button([10*100+50,100*2+50+200],"DEL",size=[150,85]) # create a delete button instance
buttonList.append(deleteButton) # add the delete button to the button list

while True :
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    img = drawAll(img, buttonList)

    if lmList :
        for button in buttonList :
            x,y = button.pos
            w,h = button.size
            
            if x < lmList[8][0] < x+w and y<lmList[8][1]<y+h:
                cv2.rectangle(img,button.pos,(x+w,y+h),(175,0,175), cv2.FILLED)
                cv2.putText(img, button.text , (x+20,y+65),
                cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)

                l,_,_ = detector.findDistance(8, 12, img, draw=False)
                print(l)
                
                ##when clicked
                if button.text == "DEL" and l < 60: # if the delete button is clicked
                                keyboard.press(Key.backspace) # simulate a backspace key press
                                cv2.rectangle(img,button.pos,(x+w,y+h),(0,255,0), cv2.FILLED)
                                cv2.putText(img, button.text , (x+20,y+65),
                                cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
                                finalText = finalText[:-1] # remove the last character from the finalText variable
                                sleep(0.3)
                elif l < 30:    
                    keyboard.press(button.text)
                    cv2.rectangle(img,button.pos,(x+w,y+h),(0,255,0), cv2.FILLED)
                    cv2.putText(img, button.text , (x+20,y+65),
                    cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
                    finalText += button.text
                    sleep(0.3)
                    
                    
    cv2.rectangle(img,(50,550),(700,650),(252,237,218), cv2.FILLED)
    cv2.putText(img, finalText , (60,630),
    cv2.FONT_HERSHEY_PLAIN,5,(238,78,52),5)

    cv2.imshow("Image",img)
    if cv2.waitKey(1) == ord('q') :
        break
    
cap.release()
cv2.destroyAllWindows()