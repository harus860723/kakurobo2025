import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import math
from kalman_filter import KalmanFilter


def test_predict_step():
    kf = KalmanFilter(
        initial_estimate=0.0,
        initial_variance=1.0,
        process_noise=0.5,
        observation_noise=1.0,
        steps_move=2.0
    )

    kf.predict()

    assert math.isclose(kf.x, 2.0)
    assert math.isclose(kf.P, 1.5)

def test_update_step():
    kf = KalmanFilter(
        initial_estimate=0.0,
        initial_variance=1.0,
        process_noise=2.0,
        observation_noise=1.0,
        steps_move=2.0
    )

    kf.update(z=1.0)

    assert isinstance(kf.x, float)
    assert kf.P > 0.0


def test_step_returns_estimate():
    kf = KalmanFilter(
        initial_estimate=0.0,
        initial_variance=1.0,
        process_noise=0.1,
        observation_noise=1.0,
        steps_move=1.0
    )

    est = kf.step(z=1.2)
    assert isinstance(est, float)
