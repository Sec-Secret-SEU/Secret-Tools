'''
Longest_run_of_ones_in_a_block.py:块内最大1游程检测
'''
import math

from main import alpha, generate_random_sequence
from scipy.special import gammaincc, gammainc

TAG = 'Longest_run_of_ones_in_a_block'


# 根据规则修改参数值
def rule(bits, n):
    set_list = list()  # 存放几个集合的列表
    pi_list = [0]*7  # 存放pai的值
    # 初始定义m，k，即位数长度小于128时对应的值
    m = 8
    K = 3
    if n >= 750000:
        m = 10000
        K = 6
        pi_list[0] = 0.086632
        pi_list[1] = 0.208201
        pi_list[2] = 0.248419
        pi_list[3] = 0.193913
        pi_list[4] = 0.121458
        pi_list[5] = 0.068011
        pi_list[6] = 0.073366
    elif n >= 6272:
        m = 128
        K = 5
        pi_list[0] = 0.1174
        pi_list[1] = 0.2430
        pi_list[2] = 0.2493
        pi_list[3] = 0.1752
        pi_list[4] = 0.1027
        pi_list[5] = 0.1124
    elif n >= 128:
        m = 8
        K = 3
        pi_list[0] = 0.2148
        pi_list[1] = 0.3672
        pi_list[2] = 0.2305
        pi_list[3] = 0.1875

    for i in range(K + 1):
        set_temp = list()
        set_list.append(set_temp)
    return m, K, set_list, pi_list


def longest_run_test(bits):
    n = len(bits)
    success = False
    if n < 0:
        print(TAG, "请输入有效值")
        return -1
    # ——————————————————————————
    m, K, set_list, pi_list = rule(bits, n)
    # print(m, K, set_list)

    N = n // m
    Child_Sequence = list()
    # 每组M位，分割成子序列
    for i in range(N):
        child = bits[i * (m):((i + 1) * (m))]
        s = "".join(child)
        Child_Sequence.append(s)

    if m == 8:
        for i in range(len(Child_Sequence)):
            # 计算每个序列的最大1游程长度
            max_run = 0  # 最大游程长度
            current_run = 0  # 当前游程长度
            for digit in Child_Sequence[i]:
                if digit == '1':  # 最大1游程长度
                    current_run += 1
                    if current_run > max_run:
                        max_run = current_run
                else:
                    current_run = 0
            # 放入集合中
            if max_run <= 1:
                set_list[0].append(max_run)
            elif max_run == 2:
                set_list[1].append(max_run)
            elif max_run == 3:
                set_list[2].append(max_run)
            elif max_run >= 4:
                set_list[3].append(max_run)
    elif m == 128:
        for i in range(len(Child_Sequence)):
            # 计算每个序列的最大1游程长度
            max_run = 0  # 最大游程长度
            current_run = 0  # 当前游程长度
            for digit in Child_Sequence[i]:
                if digit == 1:  # 最大1游程长度
                    current_run += 1
                    if current_run > max_run:
                        max_run = current_run
                else:
                    current_run = 0
            # 放入集合中
            if max_run <= 4:
                set_list[0].append(max_run)
            elif max_run == 5:
                set_list[1].append(max_run)
            elif max_run == 6:
                set_list[2].append(max_run)
            elif max_run == 7:
                set_list[3].append(max_run)
            elif max_run == 8:
                set_list[4].append(max_run)
            elif max_run >= 9:
                set_list[5].append(max_run)
    elif m == 10000:
        for i in range(len(Child_Sequence)):
            # 计算每个序列的最大1游程长度
            max_run = 0  # 最大游程长度
            current_run = 0  # 当前游程长度
            for digit in Child_Sequence[i]:
                if digit == 1:  # 最大1游程长度
                    current_run += 1
                    if current_run > max_run:
                        max_run = current_run
                else:
                    current_run = 0
            # 放入集合中
            if max_run <= 10:
                set_list[0].append(max_run)
            elif max_run == 11:
                set_list[1].append(max_run)
            elif max_run == 12:
                set_list[2].append(max_run)
            elif max_run == 13:
                set_list[3].append(max_run)
            elif max_run == 14:
                set_list[4].append(max_run)
            elif max_run == 15:
                set_list[5].append(max_run)
            elif max_run >= 16:
                set_list[6].append(max_run)
    # 计算V
    V = 0
    for i in range(K + 1):
        fen_zi = pow((len(set_list[i]) - N * pi_list[i]), 2)
        fen_mu = N * pi_list[i]
        V += fen_zi / fen_mu
    print("中间值V:", V)
    # ———————————————————————————
    P_value = gammaincc(K / 2, V / 2)
    if P_value >= alpha:
        success = True
    Q_value = P_value
    return success, P_value, Q_value


def for_UI(bits):
    is_success, P_value, Q_value = longest_run_test(bits)
    print("重叠子序列检测结果:", is_success)
    print("重叠子序列检测结果P1_value:", P_value)
    print("重叠子序列检测结果P2_value:", Q_value)
    return is_success, P_value, Q_value


if __name__ == '__main__':
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
    bit_str = list(
        '11001100000101010110110001001100111000000000001001001101010100010001001111010110100000001101011111001100111001101101100010110010')
    # print(bit_str)
    # sequence_length = 1000000
    # random_list, random_str = generate_random_sequence(sequence_length)
    # print("生成的随机序列为:", random_str)
    # is_success, P_value = autocorrelation_test(random_list)
    # longest_run_test(bit_str)
    is_success, P_value, Q_value = longest_run_test(bit_str)
    print("重叠子序列检测结果:", is_success)
    print("重叠子序列检测结果P1_value:", P_value)
    print("重叠子序列检测结果P2_value:", Q_value)
