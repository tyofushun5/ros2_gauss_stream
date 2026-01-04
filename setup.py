# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2025 shun
"""Setuptools package definition for ros2_gauss_stream."""

from setuptools import find_packages, setup

package_name = 'ros2_gauss_stream'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/gauss.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shun',
    maintainer_email='zenshun10@gmail.com',
    description='Publishes Gaussian samples and logs streaming statistics.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gauss_talker = ros2_gauss_stream.gauss_talker:main',
            'gauss_listener = ros2_gauss_stream.gauss_listener:main',
        ],
    },
)
