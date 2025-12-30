# SPDX-License-Identifier: MIT
# Copyright (c) 2025 shun
"""Setuptools package definition for mypkg."""

from setuptools import find_packages, setup

package_name = 'mypkg'

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
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shun',
    maintainer_email='zenshun10@gmail.com',
    description='Gaussian talker/listener example.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gauss_talker = mypkg.gauss_talker:main',
            'gauss_listener = mypkg.gauss_listener:main',
        ],
    },
)
