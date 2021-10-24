import numpy as np
import pandas as pd
from IPython import display


def init_q_mat(n: int):
    """
        Creates list for Q matrix, where Q_ij will be submatrix of n x n vertices.
    Args:
        n: number of vertices

    Returns:

    """
    return np.zeros((n, n), dtype=int).tolist()


def q_diag_submat(alpha, n) -> np.array:
    diag_mat = np.zeros((n, n))
    diag_mat[np.triu_indices(n, 1)] = alpha
    return diag_mat


def q_common_submat(alpha, beta, adjacency, v_i, v_j):
    n = len(adjacency)

    # 1 VARIANT:
    # common_mat = adjacency.copy() * beta
    # common_mat[np.diag_indices(n)] = alpha  # filling diagonal values with alpha value

    # 2 VARIANT:
    common_mat = np.zeros((n, n))
    common_mat[np.triu_indices(n, 1)] = beta * adjacency[v_i, v_j]
    common_mat[np.tril_indices(n, -1)] = beta * adjacency[v_j, v_i]
    common_mat[np.diag_indices(n)] = alpha  # filling diagonal values with alpha value

    return common_mat


def define_q_mat(adjacency, alpha: int, beta: int):
    adjacency = np.array([
        [0, 14, 16, 13, 14],
        [14, 0, 3, 3, 15],
        [16, 3, 0, 4, 17],
        [13, 3, 4, 0, 12],
        [14, 15, 17, 12, 0],
    ])
    # adjacency = np.random.randint(10, size=(n, n))

    n = len(adjacency)

    diag_e = 0
    display(pd.DataFrame(adjacency))

    qubo_mat = init_q_mat(n)
    for i_row in range(len(adjacency)):
        for j_col in range(len(adjacency[i_row])):
            if j_col > i_row:
                continue
            elif i_row == j_col:
                res_block = q_diag_submat(alpha, n)
            else:
                res_block = q_common_submat(alpha, beta, adjacency, i_row, j_col)
            qubo_mat[i_row][j_col] = res_block
            # qubo_mat[j_col][i_row] = res_block
            
    qubo_mat = np.array(qubo_mat, dtype=object)
    prep_qubo_mat = np.vstack(tuple([np.hstack(i_row) for i_row in qubo_mat]))
    prep_qubo_mat[np.diag_indices(n ** 2)] = diag_e
    prep_qubo_mat[np.tril_indices(n ** 2, -1)] = 0
    return qubo_mat


def symmetric_qubo_mat(triu_qubo_mat):
    return triu_qubo_mat + triu_qubo_mat.T - np.diag(np.diag(triu_qubo_mat))


if __name__ == '__main__':
    n = 5
    alpha = 1
    beta = 2
    

    # display(np.matrix(QUBO_mat))
    # QUBO_mat = np.random.randint(10, size=(16,16))

    df = pd.DataFrame(QUBO_mat)
    display(df)

    # spins, energy = solver.solve_qubo(QUBO_mat, timeout=None, target=None, callback=None)
    # display("spins: ", spins)
    # display("energy: ", energy)
