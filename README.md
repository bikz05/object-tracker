# object-tracker
Real-Time Ojbect Tracker written in Python using dlib and OpenCV

# Table of Contents

* [Dependencies](#dependencies)
* [Starting the code](#starting-the-code)
* [How to perform tracking](#how-to-perform-tracking)

---

## Dependencies

* [Dlib with Python support](http://dlib.net/)
* [OpenCV with Python support](http://opencv.org)

---

## Starting the code

Tracking can either be done either using a live video from a webcam or using a video file.

### Video File

To run the code using a video file use the following command line argument --

```shell
python object-tracker-single.py -v <path-2-video-file>
```

For example, you can use the demo video provided with this code as --

```shell
#TODO
```

### Live Video

To run the code using live video use the following command line argument --

```shell
python object-tracker-single.py -d <device-id>
```

For example, on most systems device id 0 is the webcam attached.

```shell
python object-tracker-single.py -v <path-2-video-file>
```

---

If you want to do multi-tracking code use the file `object-tracker-multi.py` instead of `object-tracker-single.py`. This is a hack to do multi-object tracking and hence the code slows down.

## How to perform tracking

Once the code starts, it will start the video. To pause the video to select the object to be tracked press <kbd>p</kbd>.The next step is to create a bounding box around the object to be tracked. Press the mouse on the top-left pixel location of the object to be tracked and then release the mouse on the bottom-right location of the object to be tracked. Once, this is done press <kbd>p</kbd> to start the tracking. If you want to change the position of the project, press <kbd>d</kbd> to discard the object selected. In SINGLE OBJECT TRACKING MODE, you can only select one object but in MULTI OBJECTTRACKING MODE, you can select as many objects you want but at the cost of speed. Press <kbd>esc</kbd> anytime to gracefully quit the code.

---
