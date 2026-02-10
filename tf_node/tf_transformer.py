import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class TFTransformer(Node):
    def __init__(self):
        super().__init__('tf_transformer')
        self.sub = self.create_subscription(
            PoseStamped, '/object_pose_camera',
            self.callback, 10)

    def callback(self, msg):
        # Mock transform: camera → base_link
        msg.header.frame_id = "base_link"
        self.get_logger().info("Transformed object pose to base_link")

def main():
    rclpy.init()
    rclpy.spin(TFTransformer())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
