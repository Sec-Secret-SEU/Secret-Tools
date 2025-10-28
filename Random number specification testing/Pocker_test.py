'''
Pocker_test.py:扑克检测
'''

import math
from main import alpha, generate_random_sequence
from scipy.special import gammaincc

TAG = "Pocker_test"
M = 4  # 规范定义m=4


# # 扑克检测
# def pocker_test(bits):
#     n = len(bits)
#     success = False  # 盘点是否成功
#     m = M
#
#     if n == 0:
#         print(TAG, "请输入有效值")
#         return -1
#     if n < m:
#         m = n  # 如果序列长度小于8，修改块分组为序列长度（分一组）
#
#     N = n // m
#
#     ni_sum = 0
#     for i in range(1, 2 ** m + 1):  # 1~2^m
def poker_test(bits):
    n = len(bits)
    success = False  # 盘点是否成功
    m = M

    if n == 0:
        print(TAG, "请输入有效值")
        return -1
    if n < m:
        m = n  # 如果序列长度小于100，修改块分组为序列长度（分一组）

    N = n // m

    Child_Sequence = list()
    # 每组M位，分割成子序列
    for i in range(N):
        child = bits[i * (M):((i + 1) * (M))]
        s = "".join(child)
        Child_Sequence.append(s)

    ni_list = [0] * (1 << M)  # 统计i类子序列出现了的频数,使用移位操作加快速度
    for j in range(1 << M):
        r = bin(j).replace('0b', '').rjust(M, '0')
        ni_list[j] = Child_Sequence.count(r)

    ni_sum = 0
    for m in range(1 << M):
        ni_sum += ni_list[m] ** 2

    V = float(1 << M) / float(N) * ni_sum - N
    # print(V)
    P_value = gammaincc(((1 << M) - 1) / 2.0, V / 2.0)
    # print(p)
    if P_value >= alpha:
        success = True

    Q_value = P_value
    return success, P_value, Q_value


def for_UI(bits):
    is_success, P_value, Q_value = poker_test(bits)
    print("扑克检测结果:", is_success)
    print("扑克检测结果P_value:", P_value)
    print("扑克检测结果Q_value:", Q_value)
    return is_success, P_value, Q_value


if __name__ == '__main__':
    sequence_length = 1000000
    random_list, random_str = generate_random_sequence(sequence_length)
    # bits = ['1', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '1', '1', '1', '0', '1', '1', '1', '1',
    #         '1', '0', '1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '0', '0', '1', '1', '0', '1', '0', '1', '0',
    #         '1', '1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '0', '1', '1', '1', '0', '0', '0', '1',
    #         '1', '0', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1',
    #         '1', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '1', '0',
    #         '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '1', '0', '0', '1',
    #         '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '1', '1', '0', '1', '1',
    #         '0', '1', '1', '0', '0', '1', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1',
    #         '1', '0', '1', '1', '0', '0', '0', '1', '0', '0', '1', '1', '1', '1', '1', '1', '0', '0', '1', '1', '0',
    #         '0',
    #         '0', '1', '0', '1', '0', '0', '1', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '1', '0', '0', '0',
    #         '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '1',
    #         '1', '1', '0', '0', '1', '0', '1', '0', '1', '1', '0', '0', '0', '1', '0', '1', '1', '0', '1', '1', '1',
    #         '1', '0']
    bits = list('11001100000101010110110001001100111000000000001001001101010100010001001111010110100000001101011111001100111001101101100010110010')
    # b = list(map(int, bits))
    # print("生成的随机序列为:", random_str)
    # is_success, P_value = block_frequency_test(random_list)
    is_success, P_value, Q_value = poker_test(bits)

    # print("单比特频数检测结果:", is_success)
    print("扑克检测结果P_value:", is_success, P_value)
    # print("单比特频数检测结果Q_value:", Q_value)
