import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class PerceptionNode(Node):
    def __init__(self):
        super().__init__('perception_node')
        self.publisher = self.create_publisher(
            PoseStamped, '/object_pose_camera', 10)
        self.timer = self.create_timer(1.0, self.publish_pose)

    def publish_pose(self):
        pose = PoseStamped()
        pose.header.frame_id = "camera_link"
        pose.pose.position.x = 0.4
        pose.pose.position.y = 0.0
        pose.pose.position.z = 0.2
        pose.pose.orientation.w = 1.0
        self.publisher.publish(pose)
        self.get_logger().info("Published object pose in camera frame")

def main():
    rclpy.init()
    rclpy.spin(PerceptionNode())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
