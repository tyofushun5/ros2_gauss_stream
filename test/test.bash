#!/bin/bash
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 shun

set -e

dir=~
[ "$1" != "" ] && dir="$1"
ros2_ws_dir="${ROS2_WS:-$dir/ros2_ws}"

cd "${ros2_ws_dir}"
colcon build --packages-select mypkg
source install/setup.bash

echo "=== Test 1: Invalid command ==="
if ros2 run mypkg no_such_node >/dev/null 2>&1; then
	echo "invalid command should fail."
	exit 1
fi

echo "=== Test 2: Talker publishes ==="
timeout 15 ros2 run mypkg gauss_talker > /tmp/gauss_talker.log 2>&1 &
talker_pid=$!
sleep 1

timeout 5 ros2 topic echo /gauss --once > /tmp/gauss_test1.log 2>&1
grep 'data:' /tmp/gauss_test1.log

echo "=== Test 3: Listener logs stats ==="
timeout 5 ros2 run mypkg gauss_listener > /tmp/gauss_listener.log 2>&1
grep -m 1 'n=' /tmp/gauss_listener.log

kill "${talker_pid}" 2>/dev/null || true
wait "${talker_pid}" 2>/dev/null || true

echo "=== Test 4: Launch ==="
timeout 15 ros2 launch mypkg gauss.launch.py > /tmp/gauss_launch.log 2>&1 &
launch_pid=$!
sleep 2

timeout 5 ros2 topic echo /gauss --once > /tmp/gauss_test2.log 2>&1
grep 'data:' /tmp/gauss_test2.log

kill "${launch_pid}" 2>/dev/null || true
wait "${launch_pid}" 2>/dev/null || true

echo "=== All tests completed ==="
