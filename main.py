# SPDX-FileCopyrightText: 2025 Haruki Matsushita
# SPDX-License-Identifier: BSD-3-Clause
# 実行用スクリプト
from simulation import run_simulation
from visualize import plot_results


def main():
    true_positions, observations, estimates = run_simulation(
        steps=50,#ステップ数
        steps_move=1.0,#1ステップ移動量
        process_noise=1.0,#プロセスノイズ分散
        observation_noise=25.0#観測ノイズ分散
    )

    plot_results(true_positions, observations, estimates)


if __name__ == "__main__":
    main()
