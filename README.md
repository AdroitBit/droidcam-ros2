# droidcam-ros2
This ROS package is simply inspired by this python code.
```python
import cv2

cap = cv2.VideoCapture('http://<DROIDCAM_IP>/mjpegfeed')

while True:
    ret, frame = cap.read()
    if ret && frame is not None:
        cv2.imshow("frame", frame)
    cv2.waitKey(1)
```

After `git clone` and `colcon build` you can run

```bash
$ ros2 run droidcam_ros publisher -ros-args -p ip:=<DROIDCAM_IP>
```
Which will launch the node that publish the image from droidcam to ROS topic named `camera_image` constantly.


View the published image by open rqt image viewer.
```bash
$ ros2 run rqt_image_view rqt_image_view
```
