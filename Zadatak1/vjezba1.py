import numpy as np
from scipy.optimize import linear_sum_assignment

# Definiraj troškove proizvodnje dobara na strojevima
costs = np.array([
    [25, 9, 15, 20],
    [28, 25, 9, 11],
    [17, 20, 14, 16],
    [26, 19, 17, 20]
])

# Rješavanje problema asignacije pomoću linear_sum_assignment
row_ind, col_ind = linear_sum_assignment(costs)

# Ispisivanje asignacija (koje dobro se proizvodi na kojem stroju)
for i, j in zip(row_ind, col_ind):
    print(f"Dobro {i + 1} proizvodi se na stroju {j + 1}")

# Izračun ukupnih minimalnih troškova proizvodnje
min_costs = costs[row_ind, col_ind].sum()

print(f"Ukupni minimalni troškovi proizvodnje: {min_costs}")
