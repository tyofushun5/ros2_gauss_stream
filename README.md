<!-- SPDX-License-Identifier: MIT -->
<!-- SPDX-FileCopyrightText: 2025 shun -->

# ros2_gauss_stream

[![test](https://github.com/tyofushun5/ros2-gauss-stream/actions/workflows/test.yml/badge.svg)](https://github.com/tyofushun5/ros2-gauss-stream/actions/workflows/test.yml)

正規分布 N(0, 1) のサンプルを publish し、受信側で逐次統計（n/mean/std）を計算してログ表示する ROS 2 (rclpy) パッケージです。

## ノード

### gauss_talker

正規分布サンプルを一定周期で publish。

- 乱数: `random.Random(0).gauss(mu=0.0, sigma=1.0)`
- 周期: 0.5 秒

| トピック | 型 | 説明 |
|---------|-----|------|
| `/gauss` | `std_msgs/msg/Float32` | 正規分布サンプル |

### gauss_listener

`/gauss` を subscribe し、Welford 法で統計量を更新してログ出力。

| トピック | 型 | 説明 |
|---------|-----|------|
| `/gauss` | `std_msgs/msg/Float32` | 正規分布サンプル |

ログ出力例:
```
n=25 x=-0.232 mean=-0.041 std=0.915
```

## Launch

### gauss.launch.py

talker/listener を同時に起動。

```bash
ros2 launch ros2_gauss_stream gauss.launch.py
```

## 使用例

### 送信ノードの実行

```bash
ros2 run ros2_gauss_stream gauss_talker
```

### 受信ノードの実行

```bash
ros2 run ros2_gauss_stream gauss_listener
```

### トピック確認

```bash
ros2 topic echo /gauss --once
data: 0.02832544
---
```

- 出力値は例です。

## テスト環境

- Ubuntu 22.04
- ROS 2 Humble

## ライセンスおよびコピーライト

このプロジェクトは MIT ライセンスの下で公開されています。詳細は `LICENSE` を参照してください。

```
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2025 shun
```
