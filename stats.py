import argparse
from collections import defaultdict

"""
This script calculates the distribution of different MR orders in the triaining data
"""


def calc_stats(src_path):
    stats = defaultdict(int)
    with open(src_path, 'r') as src:
        #with open(sum_path, 'w') as sum:
        for row in src:
            tags = collapse_row(row)
            stats[tags] += 1

    final = collapse_stats(stats)
    d_view = [(v, k) for k, v in final.items()]
    d_view.sort(reverse=True)  # natively sort tuples by first element
    for v, k in d_view:
        print("{}: {}".format(k,v))


def collapse_stats(stats):
    collapsed_dict = {}
    sorted_stats = sorted(stats, key=len, reverse=True)
    #for k in sorted_stats:
    #    print("{}: {}".format(k,stats[k]))
    for k in sorted_stats:
        k_list = k.split(",")
        if len(k_list) == 8:
            collapsed_dict[k] = stats[k]
        else:
            for long in collapsed_dict:
                if is_sublist(k_list, long):
                    collapsed_dict[long] += stats[k]
                    break
            else:
                collapsed_dict[k] = stats[k]

    return collapsed_dict


def is_sublist(short, long):
    long_list = long.split(",")
    if not all(x in long_list for x in short):
        return False
    i = 0
    while i < len(short) - 1:
        i_1 = long_list.index(short[i])
        i_2 = long_list.index(short[i + 1])
        if i_1 > i_2:
            return False
        i += 1
    return True


def collapse_row(row):
    collapsed_list = []
    prev = ""
    for item in row.strip().split():
        if item == prev:
            continue
        collapsed_list.append(item)
        prev = item

    return ", ".join(collapsed_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create input format (box and summary) from csv file')
    parser.add_argument('input', type=str, help='the .box.lab training file')
    args = parser.parse_args()

    calc_stats(args.input)
