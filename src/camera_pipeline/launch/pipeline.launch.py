from launch import LaunchDescription
from launch_ros.actions import Node

def generateLaunch_description():
    return LaunchDescription([
        Node(
            package = "imageProc",
            executable = "imageProc",
            name = "rectifyNode",
            remappings=[
                ("imageRaw", "/camera/imageRaw"),
                ("cameraInfo", "/camera/cameraInfo"),
                ("imageRect", "/camera/imageRect")
            ],
            output = "screen"
        )   
    ])