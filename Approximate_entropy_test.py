'''
Approximate_entropy_test.py:近似熵检测
'''
import math
from main import alpha, generate_random_sequence
from scipy.special import gammaincc

TAG = 'Approximate_entropy_test'


# 生成第五步的两个fai
def generate_fai(bits, m, n):
    fai = 0
    # 第一步
    cut_list = bits[:m - 1]  # 切片前m-1位数据
    new_bits = bits + cut_list
    # print("新序列为:", new_bits, len(new_bits))
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
    # 第三步 第四步
    for key, value in vi_dic.items():
        Cmj = value / n
        fai_i = Cmj * math.log(Cmj)
        if Cmj == 0:
            fai_i = 0
        fai += fai_i
    # print(vi_dic)
    return fai


# 近似熵检测
def approximate_entropy_test(bits, m):
    n = len(bits)
    success = False
    if n == 0:
        print(TAG, "请输入有效值")
        return -1
    # ——————————————————————————
    fai_m = generate_fai(bits, m, n)
    # 第五步
    fai_m1 = generate_fai(bits, m + 1, n)
    # 第六步
    ApEn_m = fai_m - fai_m1
    V = 2 * n * (math.log(2) - ApEn_m)
    # print(V)
    # ———————————————————————————
    P_value = gammaincc(pow(2, m - 1), V / 2)
    if P_value >= alpha:
        success = True
    Q_value = P_value
    return success, P_value, Q_value


def for_UI(bits):
    is_success, P_value, Q_value = approximate_entropy_test(bits, m=2)
    print("近似熵检测结果:", is_success)
    print("近似熵检测结果P_value:", P_value)
    print("近似熵检测结果Q_value:", Q_value)
    return is_success, P_value, Q_value


if __name__ == '__main__':
    bit_str = list('1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000')
    print(bit_str)
    # sequence_length = 1000000
    # random_list, random_str = generate_random_sequence(sequence_length)
    # print("生成的随机序列为:", random_str)
    # is_success, P_value = autocorrelation_test(random_list)
    is_success, P_value, Q_value = approximate_entropy_test(bit_str, m=2)
    print("近似熵检测结果:", is_success)
    print("近似熵检测结果P_value:", P_value)
    print("近似熵检测结果Q_value:", Q_value)
