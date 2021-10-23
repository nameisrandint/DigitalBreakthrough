from qboard import Solver
import numpy as np


def example():
    # Access parameters
    PARAMS = {
        "remote_addr": "https://remote.qboard.tech",
        "access_key": "5e796313-093e-42f8-ad93-bf7eb52d7960"
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
        return 123

    # Getting results
    spins, energy = solver.solve_qubo(QUBOmatrix, timeout=15, target=None, callback=trycall)
    print(QUBOmatrix, spins, energy, sep='\n')

