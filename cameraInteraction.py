import cv2
import datetime;
import os;
import numpy

changeCamera = False;
drawRectangle = False;
setExit = False;
typeOfCamera = numpy.array([cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2RGB, cv2.IMREAD_COLOR, cv2.COLOR_RGB2YUV, cv2.COLOR_RGB2HLS ])
# cameraModes = numpy.array([i for i in dir(cv2) if i.startswith('COLOR')])
rectPoints = [];

def clickAndSetRectPoints(event, x, y, flags, param):
    print "Click Event Occured"
    global rectPoints, drawRectangle;
    if(event == cv2.EVENT_LBUTTONDOWN):
        # rectPoints = [(x,y)];
        rectPoints.append((x,y))
    elif(event == cv2.EVENT_LBUTTONUP):
        rectPoints.append((x,y));
        drawRectangle = True;


def internalDrawRectangle(image, startIndex, endIndex):
    global rectPoints;
    for i in range(startIndex, endIndex, 2):
        cv2.rectangle(image, rectPoints[i], rectPoints[i + 1], (0, 255, 0), 2)
    return image;

def drawRectangles(image):
    global drawRectangle, rectPoints;
    print rectPoints;
    if drawRectangle:
        if len(rectPoints)%2 == 0:
            return internalDrawRectangle(image, 0, len(rectPoints));
        else:
            return internalDrawRectangle(image, 0, len(rectPoints)-1);

def resetRectPoint():
    global drawRectangle, rectPoints;
    rectPoints = [];
    drawRectangle = False;

def cameraInteraction(cameraName, cameraIndex):

    global changeCamera, drawRectangle, setExit, typeOfCamera, cameraModes, rectPoints;
    cv2.namedWindow(cameraName)
    camera = cv2.VideoCapture(0)
    while True:
        return_value, image = camera.read()
        cv2.setMouseCallback(cameraName, clickAndSetRectPoints)
        capturedFrame = cv2.cvtColor(image,typeOfCamera[cameraIndex])
        # capturedFrame = cv2.cvtColor(image,int(cv2.col+cameraModes[index]))

        capturedFrame = cv2.flip(capturedFrame, 1)

        if drawRectangle:
            capturedFrame = drawRectangles(capturedFrame);
            print "Drawing Rectangles with points"
            print rectPoints

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
            changeCamera=True;
            break;
        elif k==ord('l') or k == ord('L'):
            #Remove last rectangle Drawn
            if(len(rectPoints)%2==0):
                rectPoints.pop();
                rectPoints.pop();
                if(len(rectPoints)==0):
                    drawRectangle = False;

    camera.release()
    cv2.destroyAllWindows()



def call_camera(cameraIndex):
    cameraInteraction('Capture Image', cameraIndex)

index = 0;
while True:
    print "Current Camera Index :", index
    call_camera(index);
    if changeCamera:
        print "Request for change in Camera"
        changeCamera = False;
        index+=1;
    if(index==typeOfCamera.size):
        index=0
    if(setExit):
        break