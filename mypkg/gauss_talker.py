# SPDX-FileCopyrightText: 2025 shun
# SPDX-License-Identifier: MIT

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

rclpy.init()
node = Node("gauss_talker")
pub = node.create_publisher(Float32, "gauss", 10)

rng = random.Random(0)  # seed固定（再現性）
mu = 0.0
sigma = 1.0

def cb():
    msg = Float32()
    msg.data = rng.gauss(mu, sigma)  # 正規分布からサンプル
    pub.publish(msg)

def main():
    node.create_timer(0.5, cb)  # 周期固定（0.5秒）
    rclpy.spin(node)
