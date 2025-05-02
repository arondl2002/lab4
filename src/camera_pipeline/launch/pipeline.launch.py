from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    usb_cam = Node(
        package = "usb_cam",
        executable = "usb_cam_node_exe",
        name = "camera",
        #remappings=[
        #    ("image_raw", "image"),
        #],
        output = "screen"
    )
    rectify = Node(
        package = "image_proc",
        executable = "rectify_node",
        name = "rectify_node",
        remappings=[
            ("image", "image_raw"),
        ],
        output = "screen"
    )
    gaussian_blur = Node(
        package = "camera_pipeline",
        executable = "gaussian_blur",
        name = "gaussian_blur",
        remappings=[
            ("image_raw", "image_rect"),
            ("image_output", "image_blurred")
        ],
        output = "screen"
    )
    canny_edge = Node(
        package = "camera_pipeline",
        executable = "canny_edge",
        name = "canny_edge",
        remappings=[
            ("image_raw", "image_rect")
        ],
        output = "screen"
    )

    nodes_to_start = [
        usb_cam,
        rectify,
        gaussian_blur,
        canny_edge
    ]

    return LaunchDescription(nodes_to_start)
