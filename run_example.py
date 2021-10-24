import argparse
import logging
import proj_logger

import numpy as np
from qboard import Solver


logger = logging.getLogger(__name__)


def get_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        """
        Example of usage: 
        $ python run_example.py -h  # to see this help
        $ python run_example.py --access_key "123example456-of78-the9-qboard0key1"
        """)
    parser.add_argument("-akey", "--access_key", type=str, required=True,
                        help="Access key for connecting to remote quantum computer. "
                             "Example: like '********-****-****-****-************'")
    return parser


def example(access_key: str):
    # Access parameters
    PARAMS = {
        "remote_addr": "https://remote.qboard.tech",
        "access_key": access_key
    }

    # Solver initialization
    solver = Solver(mode="remote:gurobi", params=PARAMS)

    # QUBO matrix definition
    QUBOmatrix = (-1) * np.matrix([
        [0, 13, 14, 16, 14],
        [13, 0,  3,  4, 12],
        [14, 3, 0,  3, 15],
        [16, 4,  3,  0, 16],
        [14, 12, 15, 16, 0]
    ])

    testMatrix = np.matrix([
        [-5, 2, 4, 0],
        [2, -3, 1, 0],
        [4, 1, -8, 5],
        [0, 0, 5, -6]
    ])

    randomMatrix = np.random.randn(5, 5)

    def trycall(*args):
        for elem in args:
            print("elem =", elem)
        return None

    # Getting results
    spins, energy = solver.solve_qubo(QUBOmatrix, timeout=None, target=None, callback=trycall)
    logger.info(f"QUBOmatrix: \n{QUBOmatrix}")
    logger.info(f"spins: {spins}")
    logger.info(f"energy: {energy}")
    return spins, energy


if __name__ == '__main__':
    args = get_argument_parser().parse_args()
    example(access_key=args.access_key)
