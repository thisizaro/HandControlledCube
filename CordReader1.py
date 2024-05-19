import cv2
import mediapipe
import numpy
import json

# Initialize the camera and MediaPipe Hands
cap = cv2.VideoCapture(0)
initHand = mediapipe.solutions.hands
mainHand = initHand.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
draw = mediapipe.solutions.drawing_utils

def handLandmarks(colorImg):
    landmarkList = []  # Default values if no landmarks are tracked
    landmarkPositions = mainHand.process(colorImg)  # Object for processing the video input
    landmarkCheck = landmarkPositions.multi_hand_landmarks  # Stores the output of the processing object
    if landmarkCheck:  # Checks if landmarks are tracked
        for hand in landmarkCheck:  # Landmarks for each hand
            for index, landmark in enumerate(hand.landmark):  # Loops through the 21 indexes and outputs their landmark coordinates
                draw.draw_landmarks(img, hand, initHand.HAND_CONNECTIONS)  # Draws each individual index on the hand with connections
                h, w, c = img.shape  # Height, width and channel on the image
                centerX, centerY = int(landmark.x * w), int(landmark.y * h)  # Converts the decimal coordinates relative to the image for each index
                landmarkList.append([index, centerX, centerY])  # Adding index and its coordinates to a list
                
    return landmarkList

# Get the width and height of the camera feed
w, h = int(cap.get(3)), int(cap.get(4))

while True:
    check, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    lmList = handLandmarks(imgRGB)
    
    # Calculate the mean position of all landmarks
    centerX = int(w / 2)
    centerY = int(h / 2)

    meanX = centerX
    meanY = centerY
    if len(lmList) != 0:
        meanX = lmList[0][1]
        meanY = lmList[0][2]
    #     for landmark in lmList:
    #         meanX += landmark[1]
    #         meanY += landmark[2]
    #     meanX /= len(lmList)
    #     meanY /= len(lmList)

    # Calculate the angle of the position vector with respect to the center of the screen
    
    angle = numpy.arctan2(meanY - centerY, meanX - centerX)

    angle_x = numpy.cos(angle)
    angle_y = numpy.sin(angle)
    # Print the angle
    print("Angle:", angle)

    # Save angle in a JSON file
    with open("angle.json", "w") as file:
        json.dump({"angle_x": angle_x, "angle_y": angle_y}, file)

    if lmList:
        # print(lmList)
        pass
        

    cv2.imshow("Hand Landmarks", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()