from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    config_path = "/home/tahnt/T3_Repos/camera_packages/ros2_ws/src/stream_publisher_package/config/stream_config.yaml"
    
    return LaunchDescription([
        Node(
            package="stream_publisher_package",
            executable="start_stream",
            namespace="tri028s_cc",
            name="stream_publisher",
            output="screen",
            emulate_tty=True,
            parameters=[config_path]
        ),
    ])