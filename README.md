<!-- SPDX-License-Identifier: MIT -->
<!-- SPDX-FileCopyrightText: 2025 shun -->

# ros2_gauss_stream

[![test](https://github.com/tyofushun5/ros2-gauss-stream/actions/workflows/test.yml/badge.svg)](https://github.com/tyofushun5/ros2-gauss-stream/actions/workflows/test.yml)

## 概要
`gauss_talker` が正規分布 N(0, 1) のサンプルを 0.5 秒周期で `/gauss` に publish します。  
`gauss_listener` が `/gauss` を subscribe し、Welford 法で `n / mean / std` を逐次更新してログ出力します。

## ノードとトピック
### gauss_talker
- ノード名: `gauss_talker`
- publish: `/gauss` (`std_msgs/msg/Float32`, キュー 10)
- 乱数: `random.Random(0).gauss(mu=0.0, sigma=1.0)`
- タイマ周期: 0.5 秒

### gauss_listener
- ノード名: `gauss_listener`
- subscribe: `/gauss` (`std_msgs/msg/Float32`, キュー 10)
- 出力: `n=... x=... mean=... std=...` をログ表示

## 実行例
ROS 2 環境とワークスペースを source 済みの状態で実行します。
```bash
$ ros2 run ros2_gauss_stream gauss_talker
$ ros2 run ros2_gauss_stream gauss_listener
$ ros2 launch ros2_gauss_stream gauss.launch.py
```

## 確認
```bash
$ ros2 topic echo /gauss --once
data: 0.02832544
---
```
- 出力値は例です。

## テスト
```bash
$ cd /path/to/ros2_gauss_stream
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
SPDX-FileCopyrightText: 2025 shun
