import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from rcl_interfaces.msg import SetParametersResult
from cv_bridge import CvBridge
import cv2

class gaussianBlur_node(Node):
    "Node for blurring an image"
    def __init__(self):
        "Constructing necessary attributes for the gaussian blur node"
        super().__init__("Gaussian_blur")

        # Subscribe to image topic
        self.subscription = self.create_subscription(
            Image,
            "imageRaw",
            self.imageCallback,
            10)
        self.subscription   #Preventing unused variable warnings

        # Publisher for filtered image
        self.publisher = self.create_publisher(
            Image,
            "outputImage",
        10)

        # Initializing CV Bridge
        self.bridge = CvBridge()

    def imageCallback(self, msg):
        "Callback for inoout image topic"
        "Applies gaussian blur to thre reciving image and publishing the edges as an image"
        try:
            blurMSG =self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            self.get_logger().error("Failed to convert image: %s" % str(e))
            return
        
        # Applying Gaussian blur consisting of a 5x5 kernel
        cvBlurred = cv2.gaussianBlur(cvImage, (5, 5), 0)

        # Convert back to ROS image message
        try:
            blurMSG = self.bridge.cv2_to_imgmsg(cvBlurred, "bgr8")
        except Exception as e:
            self.get_logger().error("Failed to convert image: %s" % str(e))
            return
        
        #P ublish the filtered image
        self.publisher.publish(blurMSG)

# Initializing the node
def main(args = None):
    rclpy.init(args = args)
    imageBlur_node = gaussianBlur_node()
    rclpy.spin(imageBlur_node)
    imageBlur_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()