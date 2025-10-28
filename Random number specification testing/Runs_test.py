'''
Runs_test.py:游程检测
'''
import math

from main import alpha, generate_random_sequence
from scipy.special import gammaincc

TAG = 'Runs_test'


# 游程总数检测
def runs_count_test(bits):
    n = len(bits)
    success = False

    if n == 0:
        print(TAG, "请输入有效值")
        return -1

    Vn_obs = 1  # 统计值Vn_obs
    PI = bits.count(1)  # Π 计算序列中 1的比例
    for i in range(n):
        if i == n - 1:
            # PI += bits[i]  # 最后一位判断01
            break
        if bits[i] != bits[i + 1]:
            Vn_obs += 1
            # PI += bits[i]

    PI /= n  # 得到序列中 1的比例
    # print(PI)
    P_value = math.erfc((abs(Vn_obs - 2 * n * PI * (1 - PI))) / (2 * math.sqrt(2 * n) * PI * (1 - PI)))
    if P_value >= alpha:
        success = True

    Q_value = math.erfc((abs(Vn_obs - 2 * n * PI * (1 - PI))) / (2 * math.sqrt(n) * PI * (1 - PI)) / math.sqrt(2)) / 2
    # print("游程总数检测P_value:", P_value)
    return success, P_value, Q_value


# 游程分布检测(2021版)
def runs_distribution_test2021(bits):
    n = len(bits)
    success = False
    if n <= 0:
        print(TAG, "请输入有效值")
        return -1

    e_list = list()  # 存放ei的列表
    new_e_list = [0] * n  # 存放ei'的列表
    k = 0  # 满足ei>=5的最大整数k
    for i in range(1, n + 1):
        e = (n - i + 3) / (pow(2, i + 2))
        if e >= 5:
            k = i
            e_list.append(e)
        else:
            break  # e为i的单调递减函数，一旦发现小于即可停止遍历

    # print(k)
    b_list = [0] * (k + 1)  # 存放bi的列表，记录长度为i的1游程数目
    g_list = [0] * (k + 1)  # 存放gi的列表，记录长度为i的0游程数目
    count = 0
    V1 = V2 = 0
    T = 0
    now_bit = bits[0]  # 由bits首位确定一开始是找0还是1的游程
    # 统计长度为i的游程的数量
    for i in range(n):
        if bits[i] == now_bit:
            count += 1
        else:
            if count <= k:
                if now_bit == 1:
                    b_list[count] += 1
                else:
                    g_list[count] += 1
            else:
                if now_bit == 1:
                    b_list[k] += 1
                else:
                    g_list[k] += 1
            now_bit = bits[i]
            count = 1

        # 不然最后一位没有计算进去
        if i == n - 1:
            if bits[n - 1] == 0:
                g_list[count] += 1
            else:
                b_list[count] += 1

    # print("b_list:", b_list)
    # print("g_list:", g_list)
    # 计算T
    for i in range(1, k + 1):
        T += b_list[i] + g_list[i]
    # print("T:", T)
    # 计算e'
    for i in range(1, k + 1):
        if i == k:
            new_e_list[i] = T / pow(2, i)
        else:
            new_e_list[i] = T / pow(2, i + 1)
    for i in range(1, k + 1):
        V1 += pow((b_list[i] - new_e_list[i]), 2) / new_e_list[i]
        V2 += pow((g_list[i] - new_e_list[i]), 2) / new_e_list[i]
    V = V1 + V2
    # print(V)
    Q_value = P_value = gammaincc(k - 1, V / 2)
    if P_value >= alpha:
        success = True

    # print("游程分布检测P_value:", P_value)
    return success, P_value, Q_value


# 游程分布检测(2012版)
def runs_distribution_test2012(bits):
    n = len(bits)
    success = False
    if n < 100:
        print(TAG, "请输入有效值")
        return -1

    e_list = list()  # 存放ei的列表
    b_list = [0] * n  # 存放bi的列表，记录长度为i的1游程数目
    g_list = [0] * n  # 存放gi的列表，记录长度为i的0游程数目
    k = 0  # 满足ei>=5的最大整数k
    for i in range(1, n + 1):
        e = (n - i + 3) / (pow(2, i + 2))
        if e >= 5:
            k = i
            e_list.append(e)
        else:
            break  # e为i的单调递减函数，一旦发现小于即可停止遍历

    # print(k)
    count = 0
    V1 = V2 = 0
    now_bit = bits[0]  # 由bits首位确定一开始是找0还是1的游程
    # 统计长度为i的游程的数量
    # for i in range(n):
    #     if bits[i] == now_bit:
    #         count += 1
    #     else:
    #         if count <= k:
    #             if now_bit == 1:
    #                 b_list[count] += 1
    #             else:
    #                 g_list[count] += 1
    #         now_bit = bits[i]
    #         count = 1
    # print(b_list, g_list)
    # j = 1
    # for l in range(1, n):
    #     if bits[l] != now_bit:
    #         if now_bit == '0':
    #             g[j - 1] += 1
    #         elif now_bit == '1':
    #             b[j - 1] += 1
    #         no = bits[l]
    #         j = 1
    #     else:
    #         j += 1

    for i in range(k):
        V1 += pow((b_list[i + 1] - e_list[i]), 2) / e_list[i]
        V2 += pow((g_list[i + 1] - e_list[i]), 2) / e_list[i]
    V = V1 + V2

    Q_value = P_value = gammaincc(k - 1, V / 2)
    if P_value >= alpha:
        success = True

    # print("游程分布检测P_value:", P_value)
    return success, P_value, Q_value


# 游程检测包括两个子检测算法
def runs_test(bits):
    b = list(map(int, bits))
    success1, P1_value, Q1_value = runs_count_test(b)
    success2, P2_value, Q2_value = runs_distribution_test2021(b)
    return success1 and success2, P1_value, P2_value


def for_UI(bits):
    is_success, P1_value, P2_value = runs_test(bits)
    print("游程检测结果:", is_success)
    print("游程总数检测结果P1_value:", P1_value)
    print("游程分布检测结果P2_value:", P2_value)
    return is_success, P1_value, P2_value


if __name__ == '__main__':
    sequence_length = 1000000
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
    bits = list(
        "11001100000101010110110001001100111000000000001001001101010100010001001111010110100000001101011111001100111001101101100010110010")
    # b = list(map(int, bits))
    random_list, random_str = generate_random_sequence(sequence_length)
    # print("生成的随机序列为:", random_str)
    # is_success = runs_test(random_list)
    is_success = runs_test(bits)
    print("游程检测结果:", is_success)
    # print("单比特频数检测结果P_value:", P_value)
