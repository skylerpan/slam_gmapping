from launch import LaunchDescription
import launch.substitutions
import launch_ros.actions
import launch.condition


def generate_launch_description():
    config_vars = [["use_sim_time", 'false'],
                   ["maxUrange", '80.0'],
                   ["maxRange", '0.0'],
                   ["minimum_score", '0'],
                   ["sigma", '0.05'],
                   ["kernelSize", '1'],
                   ["lstep", '0.05'],
                   ["astep", '0.05'],
                   ["iterations", '5'],
                   ["lsigma", '0.075'],
                   ["ogain", '3.0'],
                   ["lskip", '0'],
                   ["srr", '0.1'],
                   ["srt", '0.2'],
                   ["str", '0.1'],
                   ["stt", '0.2'],
                   ["linearUpdate", '1.0'],
                   ["angularUpdate", '0.5'],
                   ["temporalUpdate", '1.0'],
                   ["resampleThreshold", '0.5'],
                   ["particles", '30'],
                   ["xmin", '-10.0'],
                   ["ymin", '-10.0'],
                   ["xmax", '10.0'],
                   ["ymax", '10.0'],
                   ["delta", '0.05'],
                   ["occ_thresh", '0.25'],
                   ["llsamplerange", '0.01'],
                   ["llsamplestep", '0.01'],
                   ["lasamplerange", '0.005'],
                   ["lasamplestep", '0.005'],
                   ]


    launch_args = [
        launch.actions.DeclareLaunchArgument(
            name=k,
            default_value=v,
            description="Modify the [{}] gmapping parameter".format(k))
        for k, v in config_vars ]
    return LaunchDescription([
        *launch_args,
        launch.actions.DeclareLaunchArgument(name="pose_topic",
                                             default_value="/pose"),
        launch.actions.DeclareLaunchArgument(name="map_topic",
                                             default_value="/map"),
        launch_ros.actions.Node(
            package='slam_gmapping',
            node_executable='slam_gmapping',
            node_name='slam_gmapping', output='screen',
            parameters=[{k: launch.substitutions.LaunchConfiguration(k)
                         for k, _ in config_vars }],
            remappings=[("/pose",
                         launch.substitutions.LaunchConfiguration("pose_topic")),
                        ("/map",
                         launch.substitutions.LaunchConfiguration("map_topic"))]
        ),
    ])
