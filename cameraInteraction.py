import cv2
import datetime;
import os;
import numpy

changeCameraModeRequest = False;
drawRectangle = False;
modesOfCamera = numpy.array([cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2RGB, cv2.IMREAD_COLOR, cv2.COLOR_RGB2YUV, cv2.COLOR_RGB2HLS])
pointsOfRecatangle = [];

def clickAndSetRectPoints(event, x, y, flags, param):
    """This fuction is called when a mouse click event is occured"""
    print "Click Event Occured"
    global pointsOfRecatangle, drawRectangle;
    if(event == cv2.EVENT_LBUTTONDOWN):
        # rectPoints = [(x,y)];
        pointsOfRecatangle.append((x, y))
    elif(event == cv2.EVENT_LBUTTONUP):
        pointsOfRecatangle.append((x, y));
        drawRectangle = True;


def internalDrawRectangle(image, startIndex, endIndex):
    """This function actually draws the rectangle on the image based on all the points"""
    global pointsOfRecatangle;
    for i in range(startIndex, endIndex, 2):
        cv2.rectangle(image, pointsOfRecatangle[i], pointsOfRecatangle[i + 1], (0, 255, 0), 2)
    return image;

def drawRectangles(image):
    """This function is called when there are rectangle points present, it takes the image and drawn rectangle points as per the points that were taken"""
    global drawRectangle, pointsOfRecatangle;
    print pointsOfRecatangle;
    if drawRectangle:
        if len(pointsOfRecatangle)%2 == 0:
            return internalDrawRectangle(image, 0, len(pointsOfRecatangle));
        else:
            return internalDrawRectangle(image, 0, len(pointsOfRecatangle) - 1);

def resetRectPoint():
    """This function helps in removing all the rectangles drawn from the image"""
    global drawRectangle, pointsOfRecatangle;
    pointsOfRecatangle = [];
    drawRectangle = False;

def removeLastDrawnRectangle():
    """This function helps in removing the last drawn rectangle from captured Image"""
    global pointsOfRecatangle, drawRectangle;
    if (len(pointsOfRecatangle) % 2 == 0):
        pointsOfRecatangle.pop();
        pointsOfRecatangle.pop();
        if (len(pointsOfRecatangle) == 0):
            drawRectangle = False;

def cameraInteraction(cameraName, cameraIndex):
    """Camera Interaction is the main function which interacts with the camera and shows the captured frame along with the rectangles"""
    global changeCameraModeRequest, drawRectangle, setExit, modesOfCamera, cameraModes, pointsOfRecatangle;
    cv2.namedWindow(cameraName)
    camera = cv2.VideoCapture(0)
    while True:
        return_value, image = camera.read()
        cv2.setMouseCallback(cameraName, clickAndSetRectPoints)
        capturedFrame = cv2.cvtColor(image, modesOfCamera[cameraIndex])
        # capturedFrame = cv2.cvtColor(image,int(cv2.col+cameraModes[index]))

        capturedFrame = cv2.flip(capturedFrame, 1)

        if drawRectangle:
            capturedFrame = drawRectangles(capturedFrame);
            print "Drawing Rectangles with points"
            print pointsOfRecatangle

        cv2.imshow(cameraName, capturedFrame)
        k = cv2.waitKey(15) & 0xFF

        if (k == 27 or k== ord('q') or k== ord('Q')):  # ESC
            # this argument helps in quiting the application
            setExit = True;
            cv2.destroyAllWindows()
            break

        elif k == ord('s') or k == ord('S'):
            # saves the captured frame, if rectangles were present they would be added as well
            print numpy.size(image)
            now = datetime.datetime.now()
            filename = str(os.path.expanduser('~'))+"/Desktop/test_"+ str(now)+".png";
            cv2.imwrite(filename, capturedFrame)

        elif k == ord('r') or k==ord('R'):
            # Removes all the recatangle drawn
            print "Reseting the rectangle points"
            resetRectPoint()

        elif k == ord('c') or k== ord('C'):
            #change of camera
            changeCameraModeRequest=True;
            break;
        elif k==ord('l') or k == ord('L'):
            #Remove last rectangle Drawn
            removeLastDrawnRectangle();

    camera.release()
    cv2.destroyAllWindows()



def call_camera(cameraIndex):
    cameraInteraction('Capture Image', cameraIndex)

index = 0;
while True:
    print "Current Camera Index :", index
    call_camera(index);
    if changeCameraModeRequest:
        print "Request for change in Camera"
        changeCameraModeRequest = False;
        index+=1;
    if(index==modesOfCamera.size):
        index=0
    if(setExit):
        break