# object-tracker
Ojbect Tracker written in Python using dlib and OpenCV

## Dependencies

* [Dlib with Python support](http://dlib.net/)
* [OpenCV with Python support](http://opencv.org)

## Running the code

Tracking can either be done either using a live video from a webcam or using a video file.

### VIDEO FILE

To run the code using a video file use the following command line argument --

```shell
python object-tracker.py -v <path-2-video-file>
```

For example, you can use the demo video provided with this code as --

### LIVE VIDEO

To run the code using live video use the following command line argument --

```shell
python object-tracker.py -d <device-id>
```

For example, on most systems device id 0 is the webcam attached.

```shell
python object-tracker.py -v <path-2-video-file>
```

## How to perform tracking.

Once the code starts, it will start the video. To pause the video to select the object to be tracked press <kbd>p</kbd>. The key <kbd>p</kbd> can be used to toggle play and pause. The next step is to create a bounding box around the object to be tracked. Press the mouse on the top-left pixel location of the object to be tracked and then release the mouse on the bottom-right location of the object to be tracked. Once, this is done press <kbd>enter</kbd> to start the tracking. Press <kbd>esc</kbd> anytime to gracefully quit the code.
