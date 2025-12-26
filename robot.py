# SPDX-FileCopyrightText: 2025 Haruki Matsushita
# SPDX-License-Identifier: BSD-3-Clause
# 1次元のロボットモデル
# ロボットの状態
import numpy as np


class Robot:                                                            #1次元のロボットを表すクラス，状態は位置のみ
    def __init__(self, initial_position, steps_move, process_noise):
        self.position = initial_position                                #initial_position:初期位置
        self.steps_move = steps_move                                    #steps_move:1ステップ当たりの移動量
        self.process_noise = process_noise                              #process_noise:プロセスノイズ分散Q

    def move(self):                                                     #1ステップ進んだ後の位置
        noise = np.random.normal(0.0, np.sqrt(self.process_noise))      #ノイズ生成
        self.position += self.steps_move + noise
        return self.position                                            #位置を返す
