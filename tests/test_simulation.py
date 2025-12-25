import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import math
from simulation import run_simulation


def test_simulation_length():
    steps = 10
    true_pos, obs, est = run_simulation(
        steps=steps,
        steps_move=1.0,
        process_noise=1e-6,
        observation_noise=1e-6
    )

    assert len(true_pos) == steps
    assert len(obs) == steps
    assert len(est) == steps


def test_simulation_values_are_finite():
    true_pos, obs, est = run_simulation(
        steps=20,
        steps_move=1.0,
        process_noise=1.0,
        observation_noise=1.0
    )

    for v in true_pos + obs + est:
        assert math.isfinite(v)
