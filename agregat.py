import os
import json

path = "transactions"
array_dir = os.listdir(path=path)

rez = []
for i in array_dir:
    file = open(f"{path}\\{i}")
    rez.append(json.loads(file.read()))

rez = sorted(rez, key=lambda item: item['index'])
rez_search_hash = None

transaction_count_per_block = {}
for block in rez:
    block_index = block['index']
    transaction_count = len(block['transactions'])
    transaction_count_per_block[block_index] = transaction_count

print("Кол-во транзакций в каждом блоке:", transaction_count_per_block)

miner_rewards = {}
total_rewards = 0

for block in rez:
    miner = block['transactions'][-1]['to']
    reward = block['transactions'][-1]['value']

    if miner in miner_rewards:
        miner_rewards[miner] += reward
    else:
        miner_rewards[miner] = reward

    total_rewards += reward

print("Суммарное кол-во награждений для каждого майнера:", miner_rewards)
print("Мин сумма награждения:", min(miner_rewards.values()))
print("Макс сумма награждения:", max(miner_rewards.values()))

transaction_values = [transaction['value'] for block in rez for transaction in block['transactions'][:-1]]
average_transaction_value = sum(transaction_values) / len(transaction_values)

print("Ср знач перевода в транзакциях:", average_transaction_value)

from collections import defaultdict

block_count_per_time = defaultdict(int)

for block in rez:
    timestamp = block['timestamp']
    hour_minute = (timestamp // 3600, (timestamp % 3600) // 60)
    block_count_per_time[hour_minute] += 1

print("Кол-во блоков в каждой группе (час, минута):", block_count_per_time)
