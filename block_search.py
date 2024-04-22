def get_block_by_index_linear(blocks, index):

    counter = 0
    for block in blocks:
        counter += 1
        if block['index'] == index:
            return block, counter
    return None, counter


def get_block_by_index_binary(blocks, index):

    counter = 0
    left = 0  # левая граница поиска
    right = len(blocks) - 1  # правая граница поиска
    while left <= right:
        counter += 1
        mid = (left + right) // 2
        if blocks[mid]['index'] == index:
            return blocks[mid], counter
        elif blocks[mid]['index'] < index:
            left = mid + 1
        else:
            right = mid - 1
    return None, counter

