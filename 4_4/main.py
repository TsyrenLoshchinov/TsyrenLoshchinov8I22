import itertools

def find_combinations(numbers, target_sum):
    combinations = []
    for i in range(1, len(numbers)+1):
        for combo in itertools.combinations(numbers, i):
            if sum(combo) == target_sum:
                combinations.append(combo)
    return set(combinations)

numbers = [1, 2, 3, 4, 5]
target_sum = 9
combinations = find_combinations(numbers, target_sum)
print("Уникальные комбинации чисел", numbers, "с суммой", target_sum, ":", combinations)