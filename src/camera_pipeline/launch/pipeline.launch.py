from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package = "image_proc",
            executable = "rectify_node",
            name = "rectify_node",
            output = "screen"
        ),
        Node(
            package = "camera_pipeline",
            executable = "gaussian_blur",
            name = "gaussian_blur",
            remappings=[
                ("image_raw", "image_rect"),
                ("image_output", "image_blurred")
            ],
            output = "screen"
        ),
        Node(
            package = "camera_pipeline",
            executable = "canny_edge",
            name = "canny_edge",
            remappings=[
                ("image_raw", "image_blurred")
            ],
            output = "screen"
        ),
    ])
