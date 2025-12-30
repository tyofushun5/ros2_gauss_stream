<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2025 shun -->

# mypkg

[![test](https://github.com/tyofushun5/ros2-gauss-stream/actions/workflows/test.yml/badge.svg)](https://github.com/tyofushun5/ros2-gauss-stream/actions/workflows/test.yml)

## 概要
正規分布のサンプルを publish（送信）し、受信側で平均と標準偏差を
計算してログ表示する ROS 2 (rclpy) パッケージです。

## 内容
- `mypkg/gauss_talker.py`: 正規分布サンプルを送信するノード
- `mypkg/gauss_listener.py`: 逐次統計を表示するノード
- `launch/gauss.launch.py`: 2 ノード起動用の launch
- `test/test.bash`: シェルテスト

## 実行環境
- Ubuntu 22.04
- ROS 2 Humble
- Python 3

## 使い方
### ビルド
```bash
$ source /opt/ros/humble/setup.bash
$ cd ~/ros2_ws
$ colcon build --packages-select mypkg
$ source install/setup.bash
```

### gauss_talker
```bash
$ ros2 run mypkg gauss_talker
```
- 正規分布 N(0, 1) から 0.5 秒周期で `/gauss` に publish します。

### gauss_listener
```bash
$ source ~/ros2_ws/install/setup.bash
$ ros2 run mypkg gauss_listener
```
- `/gauss` を受信し、`n / mean / std` をログ出力します。

### launch
```bash
$ ros2 launch mypkg gauss.launch.py
```
- 2 つのノードを同時に起動します。

### 確認
```bash
$ ros2 topic echo /gauss
```
- `gauss_talker` 実行中に別ターミナルで確認します。

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

## テスト
```bash
$ cd ~/ros2_ws/src/mypkg
$ ./test/test.bash
```

このスクリプトはパッケージをビルドし、以下を確認します。
- 不正なノード名の実行が失敗すること
- `gauss_talker` の publish が行われること
- `gauss_listener` の統計ログが出力されること
- launch で両ノードが動作し、トピックが流れること

### テスト環境
- Ubuntu 22.04
- ROS 2 Humble

## ライセンスおよびコピーライト
本リポジトリは MIT ライセンスです。詳細は `LICENSE` を参照してください。  
Copyright (c) 2025 shun
