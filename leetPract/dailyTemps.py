def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    answer = [0] * len(temperatures)
    stack = []
    for count, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            curr = stack.pop()
            answer[curr] = count - curr
        stack.append(count)
    return answer
if __name__ =="__main__":
    temps1=[73,74,75,71,69,72,76,73]
    temps2=[30,40,50,60]
    print(dailyTemperatures(temps1))
    print(dailyTemperatures(temps2))