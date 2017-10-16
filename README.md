# Python---CameraCaptureToolForMac

Developed a tool to capture images using integrated camera of Mac. Tool provides the flexibility to draw rectangles on the image. Moreover, it allows user to remove all drawn rectangles at once or remove the last drawn rectangle. Tool also allows user to save the image currently showing in the window. Further, it incorporates the ability to change the mode of the camera.

Tool provides several features using the keyobard shortcuts, which are as follows:

1. 'c' or 'C': Pressing 'c' or 'C' provides the flexibility to change the mode of camera. Like from black and white to colorful image.
2. 's' or 'S': Pressing the key 's' or 'S' will save the image displaying on the window on user's desktop with the name "CCT" followed by current date and time of the capture of image.
3. 'q' or 'Q' or esc: Pressing 'q' or 'Q' or Esc key will help user to close the window.
4.  Pressing and Releasing Left Mouse Button: Pressing down the left click on the mouse will and releasing it at some other location will draw a rectangle shape on the image.
5. 'l' or 'L': Pressing 'l' or 'L' will remove the last drawn rectangle. Pressing this key continuously will remove each rectangle one by one.
6. 'r' or 'R': If user would like to remove all the rectangles at once, (s)he could press the key 'r' or 'R' and it will remove all the rectangles drawn on the window.

Dependecies:

1. OpenCV 3.x library is required in order to run the file.
2. Numpy Library.
3. Python 2.7 is needed.

Tool is tested on Mac machines only.

In order to test the tool, type the following command from terminal:
python ~LocationToFolder/cameraInteraction.py