<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2025 shun -->

# mypkg (ros2-gauss-stream)

## 概要
正規分布のサンプルを publish し、受信側で平均・標準偏差を
計算してログ表示する ROS 2 (rclpy) パッケージです。

## 動作確認環境
- ROS 2 Humble (Ubuntu 22.04)
- Python 3

## ノードとトピック
### gauss_talker
- ノード名: `gauss_talker`
- publish: `/gauss` (`std_msgs/msg/Float32`, キュー 10)
- 乱数: `random.Random(0).gauss(mu=0.0, sigma=1.0)`
- タイマ周期: 0.5 秒

### gauss_listener
- ノード名: `gauss_listener`
- subscribe: `/gauss` (`std_msgs/msg/Float32`, キュー 10)
- Welford 法（n, mean, M2）で逐次統計を更新し、以下をログ出力:
  `n=... x=... mean=... std=...`

## 使い方
### ビルド
```bash
$ source /opt/ros/humble/setup.bash
$ cd ~/ros2_ws
$ colcon build --packages-select mypkg
$ source install/setup.bash
```

### 実行
```bash
$ ros2 run mypkg gauss_talker
```

別ターミナル:
```bash
$ source ~/ros2_ws/install/setup.bash
$ ros2 run mypkg gauss_listener
```

### launch
```bash
$ ros2 launch mypkg gauss.launch.py
```

## テスト
```bash
$ cd ~/ros2_ws/src/mypkg
$ ./test/test.bash
```

このスクリプトはパッケージをビルドし、ノードを短時間実行して
メッセージが流れていることを確認します。

## ライセンスと著作権
MIT License. 詳細は `LICENSE` を参照してください。
Copyright (c) 2025 shun
