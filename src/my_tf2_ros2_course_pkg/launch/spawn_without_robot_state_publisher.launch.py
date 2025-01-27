import os 
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node 

def generate_launch_description():
    urdf_file='unicycle.urdf'
    package_description='unicycle_robot_pkg'
    urdf= os.path.join(get_package_share_directory(package_description), 'urdf', urdf_file)
    xml=open(urdf, 'r').read()
    xml=xml.replace('"', '\\"')
    spawn_args='{name: \"my_robot\", xml:\"'+ xml +'\"}'
    spawn_robot=ExecuteProcess(
        cmd=['ros2', 'service', ]

    )