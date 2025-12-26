# kakurobo2025
* 2025年確率ロボティクスの課題作成に使用したリポジトリ．

## 1次元ロボットに対するカルマンフィルタのシミュレーション

[![test](https://github.com/harus860723/kakurobo2025/actions/workflows/test.yml/badge.svg)](https://github.com/harus860723/kakurobo2025/actions/workflows/test.yml)

### 概要
* 本実験では，ノイズを含む観測からカルマンフィルタがどのように状態推定を行うかを調査することを目的としている．
* 実験では，1次元空間を移動するロボットを対象として，カルマンフィルタによる状態推定をシミュレーションする．
* シミュレーションするロボットは，1ステップごとに一定距離移動する．
* プロセスノイズと観測ノイズを加えて実験を行う．
* 位置，観測値，カルマンフィルタによる推定値，の3つの関係をグラフとして可視化する．

### 実行方法
#### 準備
* 使用ライブラリの環境を整える．
* cloneコマンドを使用しリポジトリをインストールする．
```
$ git clone https://github.com/harus860723/kakurobo2025.git
```

####　実行

```
$ python3 main.py
```
### システム構成

```
├── main.py             # 実行用スクリプト
├── robot.py            # 1次元ロボットモデル
├── kalman_filter.py    # カルマンフィルタ実装
├── simulation.py       # シミュレーション全体の流れ
└── visualize.py        # 結果の可視化
```

### モデルの説明

### シミュレーションの流れ

## 使用ライブラリ
* Python3
	* テスト済み: 3.9~3.11
* Numpy
* Matplotlib

## テスト環境
* Ubuntu 


## ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再領布および使用が許可される。

* このコードは、ロボットシステム学の授業で使用したスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものである。
	* [ryuichiueda/slides_marp/robosys_2025/](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)

© 2025 Haruki Matsushita