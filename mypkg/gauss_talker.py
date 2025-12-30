# SPDX-License-Identifier: MIT
# Copyright (c) 2025 shun

import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class GaussTalker(Node):
    def __init__(self) -> None:
        super().__init__('gauss_talker')
        self._publisher = self.create_publisher(Float32, 'gauss', 10)
        self._rng = random.Random(0)
        self._mu = 0.0
        self._sigma = 1.0
        self.create_timer(0.5, self._on_timer)

    def _on_timer(self) -> None:
        msg = Float32()
        msg.data = float(self._rng.gauss(self._mu, self._sigma))
        self._publisher.publish(msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = GaussTalker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
