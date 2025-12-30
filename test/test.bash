#!/bin/bash
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 shun

dir=~
[ "$1" != "" ] && dir="$1"
ros2_ws_dir="${ROS2_WS:-$dir/ros2_ws}"

cd "${ros2_ws_dir}"
if ! colcon build --packages-select mypkg; then
	exit 1
fi
if ! source install/setup.bash; then
	exit 1
fi

echo "=== Test 1: Invalid command ==="
if ros2 run mypkg no_such_node >/dev/null 2>&1; then
	echo "invalid command should fail."
	exit 1
fi

echo "=== Test 2: Talker publishes ==="
timeout 15 ros2 run mypkg gauss_talker > /tmp/gauss_talker.log 2>&1 &
talker_pid=$!
sleep 1
if ! kill -0 "${talker_pid}" 2>/dev/null; then
	echo "talker not running."
	exit 1
fi

if ! timeout 5 ros2 topic echo /gauss --once > /tmp/gauss_test1.log 2>&1; then
	echo "no message on /gauss."
	exit 1
fi
if ! grep 'data:' /tmp/gauss_test1.log; then
	exit 1
fi

echo "=== Test 3: Listener logs stats ==="
timeout 5 ros2 run mypkg gauss_listener > /tmp/gauss_listener.log 2>&1 || true
if ! grep -m 1 'n=' /tmp/gauss_listener.log; then
	exit 1
fi

kill "${talker_pid}" 2>/dev/null || true
wait "${talker_pid}" 2>/dev/null || true

echo "=== Test 4: Launch ==="
timeout 15 ros2 launch mypkg gauss.launch.py > /tmp/gauss_launch.log 2>&1 &
launch_pid=$!
sleep 2
if ! kill -0 "${launch_pid}" 2>/dev/null; then
	echo "launch not running."
	exit 1
fi

if ! timeout 5 ros2 topic echo /gauss --once > /tmp/gauss_test2.log 2>&1; then
	echo "no message on /gauss."
	exit 1
fi
if ! grep 'data:' /tmp/gauss_test2.log; then
	exit 1
fi

kill "${launch_pid}" 2>/dev/null || true
wait "${launch_pid}" 2>/dev/null || true

echo "=== All tests completed ==="
