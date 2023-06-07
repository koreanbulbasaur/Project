import matplotlib.pyplot as plt
import pandas as pd

def df_plot(a, b, x, y):
    axes[a, b].bar(x, y)
    axes[a, b].set_xlabel ('X축')
    axes[a, b].set_ylabel('Y축')
    axes[a, b].set_title('간단한 그래프')
a_n, b_n = 2, 3

# 그래프를 그릴 서브플롯 생성
fig, axes = plt.subplots(nrows=a_n, ncols=b_n, figsize=(10, 10))

a, b = 0, 0

# 데이터
x = ['A', 'B', 'C', 'D']
y = [10, 15, 7, 12]

for i in range(5):
    df_plot(a, b, x, y)

    if b < b_n - 1:
        b += 1
    else:
        b = 0
        a += 1

plt.tight_layout()
plt.show()