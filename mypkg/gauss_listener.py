# SPDX-License-Identifier: MIT
# Copyright (c) 2025 shun
"""Gaussian listener node."""

import math

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class GaussListener(Node):
    """Subscribe to Gaussian samples and log running statistics."""

    def __init__(self) -> None:
        """Initialize the listener node."""
        super().__init__('gauss_listener')
        self._n = 0
        self._mean = 0.0
        self._m2 = 0.0
        self._subscription = self.create_subscription(
            Float32,
            'gauss',
            self._on_message,
            10,
        )

    def _on_message(self, msg: Float32) -> None:
        """Update statistics from a new sample and log it."""
        x = msg.data
        self._n += 1
        delta = x - self._mean
        self._mean += delta / self._n
        delta2 = x - self._mean
        self._m2 += delta * delta2
        var = self._m2 / self._n
        std = math.sqrt(var)
        self.get_logger().info(
            f"n={self._n} x={x:.3f} mean={self._mean:.3f} std={std:.3f}"
        )


def main(args=None) -> None:
    """Entry point for the gauss_listener node."""
    rclpy.init(args=args)
    node = GaussListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
