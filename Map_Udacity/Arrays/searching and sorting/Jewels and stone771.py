def jewel_count(jewels , stones):
    count = 0
    jewels = set(jewels)
    for stone in stones:
        if stone in jewels:
            count = count + 1
    return count

jewels= "aA"
stones = "aAAbbbb"
print(jewel_count(jewels , stones))


