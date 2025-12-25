import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import matplotlib
matplotlib.use("Agg")

from visualize import plot_results


def test_plot_results_runs():
    true_positions = [0, 1, 2, 3]
    observations = [0.1, 0.9, 2.1, 3.0]
    estimates = [0.0, 1.0, 2.0, 3.0]

    plot_results(true_positions, observations, estimates)
