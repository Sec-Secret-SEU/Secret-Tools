'''
Monobit_frequency.py:单比特频数检测
'''
import math
from main import alpha, generate_random_sequence

TAG = "Monobit_frequency_test"


# 单比特频数检测
def monobit_frequency_test(bits):
    '''
    :param bits:随机比特列表
    :return: success是否检测通过，P_value检测中计算得到的P值
    '''
    b = list(map(int, bits))
    n = len(b)
    success = False  # 盘点是否成功

    if n == 0:
        print(TAG, "请输入有效值")
        return -1
    Sn = 0  # 累加求和
    for i in b:
        if i == 1:
            Sn += 1
        elif i == 0:
            Sn -= 1
    V = Sn / math.sqrt(n)  # 统计值V
    P_value = math.erfc(abs(V) / math.sqrt(2))

    if P_value >= alpha:
        success = True

    Q_value = math.erfc(V / math.sqrt(2)) / 2
    return success, P_value, Q_value


def for_UI(bits):
    is_success, P_value, Q_value = monobit_frequency_test(bits)
    print("单比特频数检测结果:", is_success)
    print("单比特频数检测结果P_value:", P_value)
    print("单比特频数检测结果Q_value:", Q_value)
    return is_success, P_value, Q_value


if __name__ == '__main__':
    # sequence_length = 1000000
    # random_list, random_str = generate_random_sequence(sequence_length)
    # print("生成的随机序列为:", random_str)
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
    # is_success, P_value = monobit_frequency_test(random_list)
    is_success, P_value, Q_value = monobit_frequency_test(bits)
    print("单比特频数检测结果:", is_success)
    print("单比特频数检测结果P_value:", P_value)

    # print("生成的随机数序列为:", random_list)
    # print("生成的随机数序列为:", random_str)
