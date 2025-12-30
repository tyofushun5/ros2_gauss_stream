<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2025 shun -->

# mypkg

Execution memo:

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 run mypkg gauss_talker
ros2 run mypkg gauss_listener
```

Note: in a new terminal, run `source ~/ros2_ws/install/setup.bash` before
`ros2 run`.
