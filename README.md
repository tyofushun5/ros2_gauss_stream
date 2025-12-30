<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2025 shun -->

# mypkg (ros2-gauss-stream)

## Overview
A ROS 2 (rclpy) package that publishes Gaussian samples and logs running
statistics. Suggested GitHub repository name: `ros2-gauss-stream`.

## Contents
- `mypkg/gauss_talker.py`: Gaussian publisher node
- `mypkg/gauss_listener.py`: Running statistics subscriber node
- `test/test.bash`: Shell-based test script

## Environment
- ROS 2 Humble / Jazzy
- Python 3

## Installation
```bash
source /opt/ros/<distro>/setup.bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

## Usage
### gauss_talker
- Node name: `gauss_talker`
- Publishes `std_msgs/msg/Float32` on topic `gauss` (queue size 10)
- Uses `random.Random(0).gauss(mu=0.0, sigma=1.0)`
- Timer period: 0.5 s

```bash
ros2 run mypkg gauss_talker
```

### gauss_listener
- Node name: `gauss_listener`
- Subscribes to `gauss` (queue size 10)
- Welford algorithm (n, mean, M2) and logs:
  `n=... x=... mean=... std=...`

```bash
ros2 run mypkg gauss_listener
```

Note: In a new terminal, run `source ~/ros2_ws/install/setup.bash` first.

## Test
```bash
cd ~/ros2_ws/src/mypkg
chmod +x test/test.bash
./test/test.bash
```

The script builds the package, runs the nodes briefly, and checks that
samples are published and the listener logs statistics.

## License and Copyright
MIT License. See `LICENSE`.
Copyright (c) 2025 shun
