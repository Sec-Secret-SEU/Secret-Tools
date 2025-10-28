'''
Autocorrelation_test.py:自相关
'''
import math
from main import alpha, generate_random_sequence

d = 1  # 规范设置d = 1
TAG = 'Autocorrelation_test'


# 自相关检测
def autocorrelation_test(bits):
    n = len(bits)
    success = False
    if n < 16:
        print(TAG, "位数小于16位，请重新输入")
        return -1

    Ad = 0
    for i in range(n - d):  # 0~n-d-1
        if i == 0:
            Ad += int(bits[i + d - 1])
            continue
        if bits[i - 1] != bits[i + d - 1]:  # -1是因为pdf中的下标从1开始，我们传入的数组从0开始
            Ad += 1

    V = 2 * (Ad - ((n - d) / 2)) / (math.sqrt(n - d))
    print(V)
    P_value = math.erfc(abs(V) / math.sqrt(2))
    if P_value >= alpha:
        success = True
    Q_value = math.erfc(V / math.sqrt(2)) / 2
    return success, P_value, Q_value


def for_UI(bits):
    is_success, P_value, Q_value = autocorrelation_test(bits)
    print("自相关检测结果:", is_success)
    print("自相关检测结果P_value:", P_value)
    print("自相关检测结果Q_value:", Q_value)
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
    # sequence_length = 1000000
    # random_list, random_str = generate_random_sequence(sequence_length)
    bit_str = list('11001100000101010110110001001100111000000000001001001101010100010001001111010110100000001101011111001100111001101101100010110010')
    # print("生成的随机序列为:", random_str)
    # is_success, P_value = autocorrelation_test(random_list)
    is_success, P_value, Q_value = autocorrelation_test(bit_str)
    print("自相关检测结果:", is_success)
    print("自相关检测结果P_value:", P_value)
    print("自相关检测结果Q_value:", Q_value)
