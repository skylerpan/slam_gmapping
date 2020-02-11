from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    param_substitutions = {
    }
    return LaunchDescription([
        launch_ros.actions.Node(
            package='slam_gmapping', 
            node_executable='slam_gmapping', 
            parameters=[param_substitutions],
            output='screen'),
    ])
