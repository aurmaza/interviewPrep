class ItemValue:
    def __init__(self, weight, val):
        self.weight = weight
        self.val = val
        self.cost = val//weight  # //rounds downp

    def __lt__(self, other):  # provide two objects and sorts it
        return self.cost < other.cost


class FractionalKnapsack:
    def getMaxValue(self, weight, val, capacity):
        unitCostVal = []
        for i in range(len(weight)):
            unitCostVal.append(ItemValue(weight[i], val[i]))
        unitCostVal.sort(reverse=True)
        print(unitCostVal)

        totalValue = 0
        for c in unitCostVal:
            currWeight = int(c.weight)
            currVal = int(c.val)
            if capacity - currWeight >= 0:  # if we can fit the whole item in knapsack, add who le item
                totalValue += currVal
            else:
                fraction = capacity / currWeight
                totalValue += currVal * fraction
                capacity = int(capacity - (currWeight*fraction))
                break
        return totalValue


if __name__ == "__main__":
    weight = [10, 20, 30]
    val = [60, 100, 120]
    frac = FractionalKnapsack()
    maxValue = frac.getMaxValue(weight, val, 50)

    print(maxValue)
