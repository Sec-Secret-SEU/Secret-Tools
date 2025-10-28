import numpy as np

alpha = 0.01  # 显著性水平。随机性P值应该要超过的值，超过该值即代表检测成功


# 使用numpy的随机数生成器
def generate_random_sequence(length):
    random = np.random.randint(2, size=length)
    random_string = ''.join(map(str, random))
    return random.tolist(), random_string

# print(generate_random_sequence(100000.txt)[1])