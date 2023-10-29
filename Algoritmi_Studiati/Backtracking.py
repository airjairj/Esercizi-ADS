def subset_sum(nums, target):
    def backtrack(start, target, current_subset):
        if target == 0:
            result.append(current_subset[:])
            return
        for i in range(start, len(nums)):
            if nums[i] <= target:
                current_subset.append(nums[i])
                backtrack(i + 1, target - nums[i], current_subset)
                current_subset.pop()


    result = []
    backtrack(0, target, [])
    return result

# Esempio di utilizzo
numbers = [2, 4, 6, 8, 5, 7, 10, 1, 20, 3]
target_sum = 10

solutions = subset_sum(numbers, target_sum)

if solutions:
    for solution in solutions:
        print("Sottoinsieme con somma", target_sum, ":", solution)
else:
    print("Nessun sottoinsieme trovato con la somma desiderata.")
