# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2025 shun
"""Launch gauss_talker and gauss_listener together."""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """Create the launch description."""
    talker = Node(
        package='ros2_gauss_stream',
        executable='gauss_talker',
        name='gauss_talker',
        output='screen',
    )
    listener = Node(
        package='ros2_gauss_stream',
        executable='gauss_listener',
        name='gauss_listener',
        output='screen',
    )
    return LaunchDescription([talker, listener])
