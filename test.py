import numpy as np

def compute_score(W, L, P, R, S, PL):
    """ Compute the score based on the provided formula. """
    if P == 0:  # Prevent division by zero if total predictions is zero
        return 0
    
    term1 = 1 / (1 + np.exp(-((W - L) / P)))
    term2 = (R / 100) + 1
    term3 = (S / 10) + 1
    term4 = (P - L) / P if P != L else 0  # Avoid division by zero if losses equal total predictions
    term5 = 1 / (1 + np.exp(-(-PL / P)))
    
    score = term1 * term2 * term3 * term4 * term5 * 1000
    return score

# Example scenarios to test the formula
test_cases = [
    {'W': 10, 'L': 5, 'P': 15, 'R': 50, 'S': 3, 'PL': 200},  # General case
    {'W': 0, 'L': 10, 'P': 10, 'R': 0, 'S': 0, 'PL': 500},  # All lost
    {'W': 20, 'L': 0, 'P': 20, 'R': 70, 'S': 20, 'PL': 0},  # All won
    {'W': 5, 'L': 5, 'P': 10, 'R': 30, 'S': 5, 'PL': 150},  # Even win/loss
    {'W': 0, 'L': 0, 'P': 0, 'R': 0, 'S': 0, 'PL': 0},      # No predictions
]

# Compute scores for each test case
scores = [compute_score(**case) for case in test_cases]
print(scores)