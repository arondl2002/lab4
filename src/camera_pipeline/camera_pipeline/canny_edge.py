import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from rcl_interfaces.msg import SetParametersResult
from cv_bridge import CvBridge
import cv2

class CannyEdgeNode(Node):
    """
    A node for apply the canny edge method on an image
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the node.
        """
        super().__init__('canny_edge')

        # Subscribe to a image topic
        self.subscription = self.create_subscription(
            Image,
            "image_raw",
            self.image_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Publish the canny edge detection image
        self.publisher = self.create_publisher(
            Image,
            'image_output',
            10)
  
        # Initialize CVBridge
        self.bridge = CvBridge()
    

    def image_callback(self, msg):
        """
        Callback function for input image topic.
        Applies the Canny Edge to the received image and publishes the edges as an image.
        """
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            self.get_logger().error('Failed to convert image: %s' % str(e))
            return
        # 
        # Legg koden din her
        # cv_image er bildet du skal bruke som input
        # cv_edge (en variabel du lager selv) skal være sluttresultatet etter å bruke Canny Edge.
        cv_edge = cv2.Canny(cv_image, 100, 200) 
        
        # Convert back to ROS Image message
        try:
            edge_msg = self.bridge.cv2_to_imgmsg(cv_edge, "bgr8")
        except Exception as e:
            self.get_logger().error('Failed to convert image: %s' % str(e))
            return
  
        # Publish the Canny Edge image
        self.publisher.publish(edge_msg)

# Initialize the node
def main(args=None):
    rclpy.init(args=args)
    canny_edge_node = CannyEdgeNode()
    rclpy.spin(canny_edge_node)
    canny_edge_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
