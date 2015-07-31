# Import the required modules
import dlib
import cv2
import argparse as ap

# Parse command line arguments
parser = ap.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-d', "--deviceID", help="Device ID")
group.add_argument('-v', "--videoFile", help="Path to Video File")
args = vars(parser.parse_args())

# Get the source of video
if args["videoFile"]:
    source = args["videoFile"]
else:
    source = int(args["deviceID"])

# Initial co-ordinates of the object to be tracked 
# will be stored in a list named `points`
points = []
mouse_press = False

# Create the VideoCapture object
cam = cv2.VideoCapture(source)

# If Camera Device is not opened, exit the program
if not cam.isOpened():
    print "Video device or file couldn't be opened"
    exit()

# Retrieve an image and Display it.
retval, img = cam.read()
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)

def select_points(event, x, y, flags, param):
    """
    Callback function to select the object to be tracked.
    """
    global points, mouse_press

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append(x)
        points.append(y)
        mouse_press = True
    elif event == cv2.EVENT_LBUTTONUP:
        points.append(x)
        points.append(y)
        mouse_press = False
    elif event == cv2.EVENT_MOUSEMOVE and mouse_press == True:
        im_draw = img.copy()
        cv2.rectangle(im_draw, (points[0], points[1]), (x, y), (255,255,255), 3)
        cv2.imshow("Image", im_draw)

cv2.setMouseCallback("Image", select_points)

# This loop will update the image window until
# we select the object to be tracked
# Once the object has been selected, press Enter.
while(1):
    if len(points) == 2:
        key = cv2.waitKey(0)
    retval, img = cam.read()
    if not retval:
        exit()
    if len(points) == 4:
        break
    key = cv2.waitKey(30)
    # Press key `p` to pause the stream
    if key == ord('p'):
        cv2.waitKey(0)
    # Press `ESC` key to quit the program
    elif key == 27:
        exit()
    cv2.imshow("Image", img)

# Create the tracker object
tracker = dlib.correlation_tracker()
# Provide the tracker the initial position of the object
tracker.start_track(img, dlib.rectangle(*points))

while True:
    # Read frame from device or file
    retval, img = cam.read()
    if not retval:
        print "Cannot capture frame device"
    # Update the tracker    
    tracker.update(img)
    # Get the position of th object, draw a 
    # bounding box around it and display it.
    rect = tracker.get_position()
    pt1 = (int(rect.left()), int(rect.top()))
    pt2 = (int(rect.right()), int(rect.bottom()))
    cv2.rectangle(img, pt1, pt2, (255, 255, 255), 3)
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Image", img)
    # Continue until the user presses ESC key
    if cv2.waitKey(1) == 27:
        break

# Relase the VideoCapture object
vid.release()
