#!/bin/bash
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 shun

ng () {
	echo "line ${1} mismatch"
	res=1
}

show_logs () {
	if [ -n "${talker_log}" ] && [ -f "${talker_log}" ]; then
		echo "--- gauss_talker log ---"
		tail -n 50 "${talker_log}"
	fi
	if [ -n "${listener_log}" ] && [ -f "${listener_log}" ]; then
		echo "--- gauss_listener log ---"
		tail -n 50 "${listener_log}"
	fi
}

res=0

talker_pid=""
listener_pid=""
talker_log=""
listener_log=""

cleanup () {
	if [ -n "${talker_pid}" ]; then
		kill "${talker_pid}" 2>/dev/null
	fi
	if [ -n "${listener_pid}" ]; then
		kill "${listener_pid}" 2>/dev/null
	fi
	wait ${talker_pid} ${listener_pid} 2>/dev/null
	if [ -n "${talker_log}" ]; then
		rm -f "${talker_log}"
	fi
	if [ -n "${listener_log}" ]; then
		rm -f "${listener_log}"
	fi
}
trap cleanup EXIT

if ! command -v ros2 >/dev/null 2>&1; then
	echo "ros2 command not found. Source your ROS 2 setup.bash."
	exit 1
fi

if ! command -v colcon >/dev/null 2>&1; then
	echo "colcon command not found. Install colcon and source ROS 2 env."
	exit 1
fi

ros2_ws_dir="${ROS2_WS:-$HOME/ros2_ws}"
if [ ! -d "${ros2_ws_dir}" ]; then
	echo "Workspace not found: ${ros2_ws_dir}"
	exit 1
fi
cd "${ros2_ws_dir}" || exit 1

if ! colcon build --packages-select mypkg; then
	exit 1
fi

# shellcheck source=/dev/null
source install/setup.bash

if ros2 run mypkg no_such_node >/dev/null 2>&1; then
	echo "invalid command should fail."
	ng "$LINENO"
fi
talker_log=$(mktemp)
listener_log=$(mktemp)

ros2 run mypkg gauss_talker > "${talker_log}" 2>&1 &
talker_pid=$!
sleep 0.5

if ! kill -0 "${talker_pid}" 2>/dev/null; then
	echo "gauss_talker exited early."
	show_logs
	ng "$LINENO"
fi

stdbuf -oL -eL ros2 run mypkg gauss_listener > "${listener_log}" 2>&1 &
listener_pid=$!
received=0
count=0
while [ "${count}" -lt 50 ]; do
	if grep -q "n=" "${listener_log}"; then
		received=1
		break
	fi
	sleep 0.1
	count=$((count + 1))
done

if [ "${received}" -ne 1 ]; then
	echo "gauss_listener did not receive messages."
	show_logs
	ng "$LINENO"
fi

[ "${res}" = 0 ] && echo OK
exit ${res}
