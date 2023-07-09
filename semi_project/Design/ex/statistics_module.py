import statistics

x_values = list(range(1, 6))

a = 0.45

if len(x_values) % 2 == 0: # 리스트의 길이가 짝수일 경우
    for x in x_values:
        if statistics.median(x_values) > x:
            b = int(statistics.median(x_values)) - x + 1
            print(-(b * a))
        else:
            c = x - int(statistics.median(x_values))
            print(c * a)
else: # 리스트의 길이가 홀수일 경우
    for x in x_values:
        if statistics.median(x_values) > x:
            b = int(statistics.median(x_values)) - x
            print(-(b * a))
        elif x == statistics.median(x_values):
            c = 0
        else:
            d = x - int(statistics.median(x_values))
            print(d * a)