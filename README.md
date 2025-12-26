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
* 実行環境を整える．
	* Python3
	* Numpy
	* Matplotlib
* cloneコマンドを使用しリポジトリをインストールする．
```
$ git clone https://github.com/harus860723/kakurobo2025.git
```

#### 実行
* 実行用のスクリプトを実行する．
```
$ python3 main.py
```

#### 実行結果
* 以下の3つがグラフ上に表示される．
	* ノイズを含みロボットの位置(True Position)
	* 観測ノイズを含んだ観測値(Observation)
	* カルマンフィルタによる推定位置(Kalman Estimate)

### システム構成
* システムの構成を以下に示す．
```
├── main.py             # 実行用スクリプト
├── robot.py            # 1次元ロボットモデル(ロボットの状態)
├── kalman_filter.py    # カルマンフィルタ実装
├── simulation.py       # シミュレーション制御
└── visualize.py        # 結果の可視化
```

### モデルの説明
#### 1次元ロボットモデル
* ロボットの状態はスカラーのみ．
* ロボットの状態方程式を下に示す．
	* xk : 時刻kにおけるロボットの位置
	* v  : 1ステップ当たりの移動量
	* wk : プロセスノイズ(分散Q)
```math
\begin{align}
x_k = x_{k-1} + v + w_k,&
w_k \sim \mathcal {N}(0,Q)
\end{align}
```
* robot.pyで実装．

#### 観測
* ロボットの位置はノイズを含んだ形で観測される．
	* zk : 観測値
	* vk : 観測ノイズ(分散R)
```math
\begin{align}
z_k = x_k + v_k,&
v_k \sim \mathcal {N}(0,R)
\end{align}
```

#### カルマンフィルタ
* 状態推定には1次元カルマンフィルタを用いる．
* 予測ステップ
```math
\begin{align}
\hat{x}_{k|k-1} = \hat{x}_{k-1} + v
\end{align}
```
```math
\begin{align}
P_{k|k-1} = P_{k-1} + Q
\end{align}
```
frac{1}{2}
* 更新ステップ
```math
\begin{align}
K_k = \frac{P_{k|k-1}}{P_{k|k-1}+R}
\end{align}
```
```math
\begin{align}
\hat{x} = \hat{x}_{k|k-1} + K_k(z_k - {x|k-1})
\end{align}
```
```math
\begin{align}
P_k = (1 - K_k)P_{k|k-1}
\end{align}
```
* kalman_filter.pyで実装される

#### シミュレーション制御
* シミュレーションの流れを下に示す．
	* ロボットを生成し位置を更新する．
	* 位置に観測ノイズを加えて観測値を生成する．
	* 観測値を用いてカルマンフィルタで位置を推定する．
	* 時系列で可視化を行う．

### シミュレーション結果
* 
* 
* 


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