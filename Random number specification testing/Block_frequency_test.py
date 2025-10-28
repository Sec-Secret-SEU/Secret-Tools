'''
Block_frequency_test.py:块内频数检测
'''

import math
from main import alpha, generate_random_sequence
from scipy.special import gammaincc

TAG = "Block_frequency_test"
M = 10  # 规范定义m=10


# 块内频数检测
def block_frequency_test(bits):
    n = len(bits)
    success = False  # 判断是否成功
    m = M

    if n == 0:
        print(TAG, "请输入有效值")
        return -1
    if n < m:
        m = n  # 如果序列长度小于100，修改块分组为序列长度（分一组）

    N = n // m
    V = 0

    for i in range(1, N + 1):  # 1~N
        PI = 0
        for j in range(1, m + 1):  # 1~m
            PI += bits[(i - 1) * m + j - 1]
        PI = PI / m
        V += pow(PI - 0.5, 2)

    V = 4 * m * V
    P_value = gammaincc(N / 2, V / 2)
    if P_value >= alpha:
        success = True

    Q_value = P_value
    return success, P_value, Q_value

def for_UI(bits):
    b = list(map(int, bits))
    is_success, P_value, Q_value = block_frequency_test(b)
    print("块内频数检测结果:", is_success)
    print("块内频数检测结果P_value:", P_value)
    print("块内频数检测结果Q_value:", Q_value)
    return is_success, P_value, Q_value

if __name__ == '__main__':
    sequence_length = 1000000
    random_list, random_str = generate_random_sequence(sequence_length)
    bits = ['1', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '1', '1', '1', '0', '1', '1', '1', '1',
            '1', '0', '1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '0', '0', '1', '1', '0', '1', '0', '1', '0',
            '1', '1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '0', '1', '1', '1', '0', '0', '0', '1',
            '1', '0', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1',
            '1', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '1', '0',
            '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '1', '0', '0', '1',
            '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '1', '1', '0', '1', '1',
            '0', '1', '1', '0', '0', '1', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1',
            '1', '0', '1', '1', '0', '0', '0', '1', '0', '0', '1', '1', '1', '1', '1', '1', '0', '0', '1', '1', '0',
            '0',
            '0', '1', '0', '1', '0', '0', '1', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '1', '0', '0', '0',
            '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '1',
            '1', '1', '0', '0', '1', '0', '1', '0', '1', '1', '0', '0', '0', '1', '0', '1', '1', '0', '1', '1', '1',
            '1', '0']
    b = list(map(int, bits))
    # print("生成的随机序列为:", random_str)
    # is_success, P_value = block_frequency_test(random_list)
    is_success, P_value, Q_value = block_frequency_test(b)

    print("块内频数检测结果:", is_success)
    print("块内频数检测结果P_value:", P_value)
    print("块内频数检测结果Q_value:", Q_value)
