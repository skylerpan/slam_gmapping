from launch import LaunchDescription
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    use_sim_time = launch.substitutions.LaunchConfiguration('use_sim_time', default='false')

    return LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            'use_sim_time', default_value='false', description='Use simulation clock if true'),

        launch_ros.actions.Node(
            package='slam_gmapping',
            node_executable='slam_gmapping',
            node_name='slam_gmapping', output='screen',
            parameters=[{ 'use_sim_time': use_sim_time}, ]),
    ])
