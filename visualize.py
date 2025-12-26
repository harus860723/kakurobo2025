# SPDX-FileCopyrightText: 2025 Haruki Matsushita
# SPDX-License-Identifier: BSD-3-Clause
# 結果の可視化
import matplotlib.pyplot as plt


def plot_results(true_positions, observations, estimates, save_path="image/result.png"):
    plt.figure(figsize=(10, 5))

    plt.plot(
        true_positions,
        label="True Position",
        color="blue",
        linewidth=2,
        zorder=1
    )

    plt.scatter(
        range(len(observations)),
        observations,
        label="Observation",
        color="red",
        s=20,
        alpha=0.6,
        zorder=2
    )

    plt.plot(
        estimates,
        label="Kalman Estimate",
        color="green",
        linewidth=2.5,
        linestyle="--",
        zorder=3
    )

    plt.xlabel("Time Step")
    plt.ylabel("Position")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()
