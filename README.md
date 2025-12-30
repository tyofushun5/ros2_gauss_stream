<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2025 shun -->

# mypkg (ros2-gauss-stream)

## 概要
正規分布のサンプルを送信し、受信側で逐次統計を表示する
ROS 2 (rclpy) パッケージです。GitHub リポジトリ名の案:
`ros2-gauss-stream`

## 内容
- `mypkg/gauss_talker.py`: 正規分布サンプルを送信するノード
- `mypkg/gauss_listener.py`: 逐次統計を表示するノード
- `test/test.bash`: シェルによる簡易テスト

## 実行環境
- ROS 2 Humble / Jazzy
- Python 3

## インストール
```bash
source /opt/ros/<distro>/setup.bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

## 使い方
### gauss_talker
- ノード名: `gauss_talker`
- `std_msgs/msg/Float32` を `gauss` に publish（キュー 10）
- `random.Random(0).gauss(mu=0.0, sigma=1.0)` を使用
- タイマ周期: 0.5 秒

```bash
ros2 run mypkg gauss_talker
```

### gauss_listener
- ノード名: `gauss_listener`
- `gauss` を subscribe（キュー 10）
- Welford 法（n, mean, M2）で逐次統計を更新し、以下をログ出力:
  `n=... x=... mean=... std=...`

```bash
ros2 run mypkg gauss_listener
```

注: 新しいターミナルでは `source ~/ros2_ws/install/setup.bash` を先に実行してください。

## テスト
```bash
cd ~/ros2_ws/src/mypkg
chmod +x test/test.bash
./test/test.bash
```

このスクリプトはパッケージをビルドし、ノードを短時間実行して
メッセージが流れていることを確認します。

## ライセンスと著作権
MIT License. 詳細は `LICENSE` を参照してください。
Copyright (c) 2025 shun
