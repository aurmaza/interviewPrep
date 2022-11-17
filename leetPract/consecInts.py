def longestSequence(nums):
    longestSequence = 0
    numsToSet = set(nums)
    for number in nums:
        currentStreak = 1
        if number - 1 in numsToSet:
            continue
        while number + 1 in numsToSet:
            number += 1
            currentStreak += 1
        longestSequence = max(longestSequence, currentStreak)
    return longestSequence


if __name__ == "__main__":
    numbers = [1, 5, 2, 3, 4, 6, 7, 100, 2, 34, 5, 2]
    print(longestSequence(numbers))
