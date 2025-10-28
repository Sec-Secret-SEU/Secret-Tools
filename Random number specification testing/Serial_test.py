'''
Serial_test.py:重叠子序列检测
'''
import math

from main import alpha, generate_random_sequence
from scipy.special import gammaincc,gammainc

TAG = 'Serial_test'


# 生成伽马(m,m-1,m-2)
def generate_gama(bits, m, n):
    # 第一步
    cut_list = bits[:m - 1]  # 切片前m-1位数据
    new_bits = bits + cut_list
    # print("新序列长度为:", len(new_bits))
    # 第二步 计算m位子序列出现频数
    vi_dic = dict()  # 定义一个长度为2^m的字典存放vi 与扑克检测不同，这里的子序列不是严格由序列产生的非重叠子序列 故用字典方便计算
    for i in range(n):  # 遍历整个序列,统计长度m的子序列的个数
        bit_m = ''.join(new_bits[i:i + m])
        # 不满足m位的序列不考虑
        if len(bit_m) >= m:
            if bit_m in vi_dic:
                vi_dic[bit_m] += 1
            else:
                vi_dic[bit_m] = 1

    return vi_dic


# 第三步 计算平方
def cal_gama_2(gama_m, m, n):
    sum = 0  # m位子序列的和
    for key, value in gama_m.items():
        sum += pow(value, 2)

    res = (pow(2, m) / n) * sum - n  # 最终计算结果
    return res


def serial_test(bits, m):
    n = len(bits)
    success = False
    if n == 0:
        print(TAG, "请输入有效值")
        return -1
    # ——————————————————————————
    gama_m = generate_gama(bits, m, n)
    gama_m_1 = generate_gama(bits, m - 1, n)
    gama_m_2 = generate_gama(bits, m - 2, n)
    value_1 = cal_gama_2(gama_m, m, n)
    value_2 = cal_gama_2(gama_m_1, m - 1, n)
    value_3 = cal_gama_2(gama_m_2, m - 2, n)
    # 第四步
    dela_value_1 = value_1 - value_2
    dela_value_2 = value_1 - 2 * value_2 + value_3
    # print(dela_value_1)
    # print(dela_value_2)
    # ———————————————————————————
    P_value_1 = gammaincc(pow(2, m - 2), dela_value_1 / 2)
    P_value_2 = gammaincc(pow(2, m - 3), dela_value_2 / 2)
    if P_value_1 >= alpha and P_value_2 >= alpha:
        success = True
    Q_value_1 = P_value_1
    Q_value_2 = P_value_2
    return success, P_value_1, P_value_2, Q_value_1, Q_value_2


def for_UI(bits):
    is_success, P1_value, P2_value, Q1_value, Q2_value = serial_test(bits, m=2)
    print("重叠子序列检测结果:", is_success)
    print("重叠子序列检测结果P1_value:", P1_value)
    print("重叠子序列检测结果P2_value:", P2_value)
    return is_success, P1_value, P2_value, Q1_value, Q2_value


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
    is_success, P1_value, P2_value, Q1_value, Q2_value, = serial_test(bit_str, m=2)
    print("重叠子序列检测结果:", is_success)
    print("重叠子序列检测结果P1_value:", P1_value)
    print("重叠子序列检测结果P2_value:", P2_value)
