luckeynum_dict = {}
with open("luckey_nums.csv") as f:
    for line in f:
        num = [int(n) for n in line.split(",")]
        luckeynum_dict[num[0]] = num[1]
        
def getUnsei (family_name , first_name):
    # 一字の場合、1を足す（霊数というらしい）
    tenkaku = sum(family_name) + 1 if len(family_name) == 1 else sum(family_name)
    jinkaku = family_name[-1] + first_name[0]
    # 一字の場合、1を足す（霊数というらしい）
    chikaku = sum(first_name) + 1 if len(first_name) == 1 else sum(first_name)
    gaikaku = tenkaku + chikaku - jinkaku
    soukaku = sum(family_name) + sum(first_name)
    katei = soukaku - family_name[0]
    shigoto = soukaku - first_name[-1]
    return [tenkaku, jinkaku, chikaku, gaikaku, soukaku, katei, shigoto]

def getRank (unsei_list):
    result = []
    for unsei in unsei_list:
        if unsei in luckeynum_dict:
            result.append(luckeynum_dict[unsei])
        else:
            result.append(4)
    return result

from itertools import product

def getTrylist(input_name):
    determined = []
    undetermined = []
    for i, kakusu in enumerate(input_name):
        if kakusu < 0:
            undetermined.append(i)
        else:
            determined.append(i)

    element_list = []
    for index in undetermined:
        single_list = []
        for i in range(1,31):
            single_list.append([index, i])
        element_list.append(single_list)
    
    try_list = [combination for combination in product(*element_list)]

    result_list = []
    for single_try in try_list:
        result = list(range(len(input_name)))
        for element in single_try:
            result[element[0]] = element[1]
        for index in determined:
            result[index] = input_name[index]
        result_list.append(result)
    return result_list

# 使用例
if __name__ == "__main__":
    # 名前の画数のリスト。-1は未決定を表す。
    family_name = [4]
    first_name = [-1]

    try_list = getTrylist(first_name) # 名字は決まっているため、名前のみを探索

    name_list = []
    for single_try in try_list:
        unsei = getUnsei(family_name, single_try)
        unsei_rank = getRank(unsei)
        name_list.append([family_name,single_try,unsei,unsei_rank])

    result = sorted(name_list, key=lambda data: sum(data[3]))

    for line in result[0:10]: 
        print(line, sum(line[3]))
