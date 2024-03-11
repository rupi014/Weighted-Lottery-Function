import numpy as np

def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weights.items():
        for _ in range(weight):
            container_list.append(name)

    return np.random.choice(container_list)

other_weights = {
    'winning': 1,
    'break_even': 2,
    'losing': 3
}

print(weighted_lottery(other_weights))

# #MY OPTION
# import random

# weighted_lottery = ["winning", "break_even", "losing"]

# random_lottery = random.choices(weighted_lottery, weights=(1, 2, 3), k=1)

# print(random_lottery)
    