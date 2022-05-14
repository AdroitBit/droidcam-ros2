import rclpy
from rclpy.node import Node
import cv2

from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class DroidCam_engine():
    def __init__(self,node,ip,port=4747):
        url='http://'+ip+':'+str(port)+'/mjpegfeed?1280x720'
        self.cap=cv2.VideoCapture(url)
    def get_img(self):
        ret, frame = self.cap.read()
        if ret:
            return frame
        else:
            return None
    def display(self):
        img=self.get_img()
        if img is not None:
            cv2.imshow('frame',img)
            cv2.waitKey(1)



class CameraNode(Node):
    def __init__(self):
        super().__init__('droidcam_publisher_node')
        self.declare_parameter('ip')
        self.declare_parameter('port',4747)
        self.publisher = self.create_publisher(Image, 'camera/image', 10)
        ip=self.get_parameter('ip')._value
        port=self.get_parameter('port')._value
        self.get_logger().info(f'Connect to ip={ip} with port={port}')
        self.engine=DroidCam_engine(self,ip=ip,port=port)
        self.timer = self.create_timer(1/30, self.timer_callback)

    def timer_callback(self):
        img=self.engine.get_img()
        if img is not None:
            msg = CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
            self.publisher.publish(msg)
        #self.engine.display()


def main(args=None):
    rclpy.init(args=args)
    node = CameraNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()