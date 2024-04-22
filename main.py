import os
import json

import block_search
import sorting


path = "transactions"
array_dir = os.listdir(path=path)  #получаю список

rez = [] #пустой список
for i in array_dir:
    file = open(f"{path}\\{i}")
    rez.append(json.loads(file.read()))

rez = sorted(rez, key=lambda item: item['index']) #сортирую по индексу
rez_search_hash = None

# 4 практическая
print(block_search.get_block_by_index_linear(rez, 5))
sorting.bubble_sort(rez)

print(block_search.get_block_by_index_binary(rez, 7))
sorting.selection_sort(rez)

for rez_dict in rez:#нахожу хэш
    if rez_dict['hash'].startswith("000") and rez_dict['hash'].endswith("000"):
        rez_search_hash = rez_dict
        break

author = rez_search_hash['transactions'][-1]
print("1.", author['to'], rez_search_hash['index'])

s = []

for i in rez:#информация о блоке с номером 71
    if i['index'] == 71:
        print("7.", i['transactions'][-1]['value'])

rez_for_1 = []#последовательные блоки с одинаковыми значениями
for i in range(len(rez) - 1):
    if rez[i]['index'] == rez[i + 1]['index'] - 1:
        rez_for_1.append(rez[i])
rez_for_1.append((rez[-1]))


counter = 0
summ = 0
rewards = [reward["transactions"][-1]["value"] for reward in rez_for_1]
reward_cnt = {}
for reward in rewards:
    if reward in reward_cnt.keys():
        reward_cnt[reward] += 1
    else:
        reward_cnt[reward] = 1
print(reward_cnt)
for i in range(len(rez_for_1) - 1):#наибольшая длина
    value = rez_for_1[i]['transactions'][-1]['value']
    value2 = rez_for_1[i + 1]['transactions'][-1]['value']
    if value == value2:
        counter += 1
    else:
        if counter > summ:
            summ = counter
        counter = 0
print(f"8. {summ + 1}")

rez_for_2 = [] #блоки, в которых значение изменится
for i in range(len(rez_for_1) - 1):
    value = rez_for_1[i]['transactions'][-1]['value']
    value2 = rez_for_1[i + 1]['transactions'][-1]['value']
    if value != value2:
        rez_for_2.append(rez_for_1[i])
rez_for_2.append(rez_for_1[-1])
rez_for_2.pop(0)

values = []#получение значения
for i in range(len(rez_for_2)):
    values.append(rez_for_2[i]['transactions'][-1]['value'])

summa = 0
last_number = None #средний коэффициент
for i in range(len(values) - 1):
    summa += values[i + 1] / values[i]
    last_number = values[i + 1]
summa = round(summa / (len(values) - 1), 2)

print(f"9. {summa}")

count = 0
difference = 0 #блоки с доп инф
for i in range(len(rez_for_1)):
    if rez_for_1[i]['transactions'][-1]['value'] == last_number:
        count += 1
        if count != (summ + 1):
            difference = (summ + 1) - count

counter = 0
coeff = summa
number = 0.09
while round(last_number, 2) != number:
    last_number = last_number * coeff
    counter += 1
quantity_of_blocks = (counter * 17 - 17) + 99 + difference + 1
print(f"10. {quantity_of_blocks}")

indexes_with_secret_info = [
    (block["index"], block["secret_info"])
    for block in rez_for_1
    if block["secret_info"] != '']
print(indexes_with_secret_info)
secret_info = []
for i in range(len(rez_for_1)):
    if rez_for_1[i]['secret_info'] != '':
        block = rez_for_1[i]
        indexes_with_secret_info.append((block['index'], block['secret_info']))
        # indexes_with_secret_info.append(rez_for_1[i]['index'])
        secret_info.append(rez_for_1[i]['secret_info'])

print(f"11. {indexes_with_secret_info}")

print(f"12. {secret_info}")

answer = bytes.fromhex("".join(secret_info)).decode()
print(f"13. {answer}")
