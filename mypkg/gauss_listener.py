# SPDX-FileCopyrightText: 2025 shun
# SPDX-License-Identifier: MIT
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math

rclpy.init()
node = Node("gauss_listener")

n = 0
mean = 0.0
M2 = 0.0

def cb(msg):
    global n, mean, M2
    x = msg.data

    # Welford法（平均と分散を逐次更新）
    n += 1
    delta = x - mean
    mean += delta / n
    delta2 = x - mean
    M2 += delta * delta2

    var = M2 / n
    std = math.sqrt(var)

    node.get_logger().info(f"n={n} x={x:.3f} mean={mean:.3f} std={std:.3f}")

sub = node.create_subscription(Float32, "gauss", cb, 10)

def main():
    rclpy.spin(node)

