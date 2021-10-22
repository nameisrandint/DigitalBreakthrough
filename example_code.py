from qboard import Solver
import numpy as np


def example():
    # Access parameters
    PARAMS = {
        "remote_addr": "https://remote.qboard.tech",
        "access_key": "5e796313-093e-42f8-ad93-bf7eb52d7960"
    }

    # Solver initialization
    s = Solver(mode="remote:simcim", params=PARAMS)

    # QUBO matrix definition
    Q = np.random.randn(5, 5)

    # Getting results
    spins, energy = s.solve_qubo(Q, timeout=30)

    print(spins, energy, end='\n')
