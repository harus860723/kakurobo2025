# SPDX-FileCopyrightText: 2025 Haruki Matsushita
# SPDX-License-Identifier: BSD-3-Clause
#シミュレーション
import numpy as np
from robot import Robot
from kalman_filter import KalmanFilter


def run_simulation(#カルマンフィルタの標準パラメータ
    steps,#ステップ数
    steps_move,#1ステップ当たりの移動量
    process_noise,#プロセスノイズQ
    observation_noise#観測ノイズR
):

    robot = Robot(#ロボット生成
        initial_position=0.0,#初期位置0.0
        steps_move=steps_move,
        process_noise=process_noise
    )

    kf = KalmanFilter(#カルマンフィルタ生成
        initial_estimate=0.0, #初期推定値
        initial_variance=1.0, #初期分散P0
        process_noise=process_noise, #プロセスノイズQ
        observation_noise=observation_noise, #観測ノイズR
        steps_move=steps_move
    )

    true_positions = []
    observations = []
    estimates = []

    for _ in range(steps):
        pos = robot.move()#位置
        obs = pos + np.random.normal(0.0, np.sqrt(observation_noise))#観測
        est = kf.step(obs)#カルマン推定

        true_positions.append(pos)
        observations.append(obs)
        estimates.append(est)

    return true_positions, observations, estimates
