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
    QUBOmatrix = np.matrix([
        [0, 13, 14, 16, 14],
        [13, 0,  3,  4, 12],
        [14, 3,  0,  3, 15],
        [16, 4,  3,  0, 16],
        [14, 12, 15, 16, 0]
    ])

    def trycallback(*args):
        for elem in args:
            print(elem)

    randomMatrix = np.random.randn(5, 5)

    # Getting results
    spins, energy = solver.solve_qubo(QUBOmatrix, timeout=600, target=1000, callback=trycallback(), enable_cache=False)

    print(QUBOmatrix, spins, energy, sep='\n')
