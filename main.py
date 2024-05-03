import numpy as np

def formula(W, L, P, R, S, PL):
    if not P:
        return 0
    
    terms = [
        # Add or remove your terms here, code will dynamically update the formula
        1 / (1 + np.exp(-((W - L) / P))),
        (R / 100) + 1,
        (S / 10) + 1,
        (P - L) / P,
        1 / (1 + np.exp(PL / P)),
    ]
    
    score = 1
    for term in terms:
        score *= term
    return score



if __name__ == '__main__':
    print("Enter ranges separated by space/tab/whatever.")
    W_i, W_f = [int(num or 0) for num in input('W_i, W_f = ').split()]
    L_i, L_f = [int(num or 0) for num in input('L_i, L_f = ').split()]
    P_i, P_f = [int(num or 0) for num in input('P_i, P_f = ').split()]
    R_i, R_f = [int(num or 0) for num in input('R_i, R_f = ').split()]
    S_i, S_f = [int(num or 0) for num in input('S_i, S_f = ').split()]
    PL_i, PL_f = [int(num or 0) for num in input('PL_i, PL_f = ').split()]

    input_ranges = []
    for param in ('W', 'L', 'P', 'R', 'S', 'PL',):
        _i, _f = [int(num or 0) for num in input('W_i, W_f = ').split()]
        input_ranges.append((_i, _f))