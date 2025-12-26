# SPDX-FileCopyrightText: 2025 Haruki Matsushita
# SPDX-License-Identifier: BSD-3-Clause
# カルマンフィルタ実装
# 推定アルゴリズム
import numpy as np


class KalmanFilter:
    def __init__(
        self,
        initial_estimate,                   #初期推定位置 ^xk
        initial_variance,                   #初期分散 P0
        process_noise,                      #プロセスノイズ分散 Q
        observation_noise,                  #観測ノイズ分散 R
        steps_move                          #1ステップ当たりの移動量
        ):

        self.x = initial_estimate           #状態推定位置^xk
        self.P = initial_variance           #推定誤差分散Pk
        self.Q = process_noise              #プロセスノイズ Q
        self.R = observation_noise          #観測ノイズ R
        self.steps_move = steps_move        #制御入力 vk

    def predict(self):                      #予測
        self.x = self.x + self.steps_move   #状態予測
        self.P = self.P + self.Q            #分散予測

    def update(self, z):                    #観測更新
        K = self.P / (self.P + self.R)      #カルマンゲイン
        self.x = self.x + K * (z - self.x)  #状態更新
        self.P = (1 - K) * self.P           #分散更新

    def step(self, z):                      #統合
        self.predict()
        self.update(z)
        return self.x
