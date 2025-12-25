import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import math
from robot import Robot


def test_robot_move_no_noise():
    robot = Robot(
        initial_position=0.0,
        steps_move=1.5,
        process_noise=0.0
    )

    pos = robot.move()
    assert math.isclose(pos, 1.5)

def test_robot_move_returns_float():
    robot = Robot(
        initial_position=0.0,
        steps_move=1.0,
        process_noise=1.0
    )

    pos = robot.move()
    assert isinstance(pos, float)
