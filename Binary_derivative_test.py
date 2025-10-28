'''
Binary_derivative_test.py:二元推导检测
'''
import copy
import math

from main import alpha, generate_random_sequence
from scipy.special import gammaincc

TAG = 'Binary_derivative_test'


def binary_derivatiev_test(bits, k):
    n = len(bits)
    success = False
    if n == 0:
        print(TAG, "请输入有效值")
        return -1
    # ——————————————————————————
    # 第一步 第二步
    new_bits = copy.deepcopy(bits)
    # 重复k次
    for i in range(k):
        for j in range(n):
            # 最后一位直接添加
            if j == (n - 1):
                break
            if new_bits[j] == new_bits[j + 1]:
                new_bits[j] = '0'
            else:
                new_bits[j] = '1'

    # 第三步
    S_nk = 0
    for i in range(n - k):
        S_nk += 2 * int(new_bits[i]) - 1

    # 第四步,计算K
    V = S_nk / math.sqrt(n - k)
    # print(V)
    # ———————————————————————————
    P_value = math.erfc(abs(V) / math.sqrt(2))
    Q_value = math.erfc(V / math.sqrt(2)) / 2
    if P_value >= alpha:
        success = True
    return success, P_value, Q_value


def for_UI(bits):
    is_success, P_value, Q_value = binary_derivatiev_test(bits, 3)
    print("二元推导检测结果:", is_success)
    print("二元推导检测结果P_value:", P_value)
    print("二元推导检测结果Q_value:", Q_value)
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
    is_success, P_value, Q_value = binary_derivatiev_test(bit_str, 3)
    print("二元推导检测结果:", is_success)
    print("二元推导检测结果P_value:", P_value)
    print("二元推导检测结果Q_value:", Q_value)
