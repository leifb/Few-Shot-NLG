import os
import sys
import csv
import nltk

# This script converts the e2e challange dataset into a format the can be processed
# with preprocess.py. It writes both the *


def start():
    if is_help():
        print("Convert e2e challenge data to data that can be processed by preprocess.py.\n" +
              "Usage: preprocess_e2e.py <source csc> <dest .box> <dest .summary>")
        sys.exit(0)

    if len(sys.argv) < 4:
        print("Missing arguments.")
        sys.exit(1)

    run(sys.argv[1], sys.argv[2], sys.argv[3])


def run(src_path, box_path, sum_path):
    with open(src_path, 'r') as src:
        with open(box_path, 'w') as box:
            with open(sum_path, 'w') as sum:
                src_reader = csv.reader(src, delimiter=',', quotechar='"')
                next(src_reader, None)
                for row in src_reader:
                    data_box, data_sum = parse_row(row)
                    box.write(data_box)
                    box.write('\n')
                    sum.write(data_sum)
                    sum.write('\n')


def parse_row(row):
    '''
    Parses a row of the e2e dataset csv and returns a  data for
    both the box file and the sumary file.
    '''

    if len(row) == 0:
        print("WARNING: column without any data")
        sys.exit(1)
        return "", ""

    mrs = parse_mr(row[0])
    mr_string = build_mr_line(mrs)

    if len(row) < 2:
        print("WARNING: input column without summary")
        return mr_string, ""
    
    tok_sum = " ".join(nltk.word_tokenize(row[1]))

    return mr_string, tok_sum


def parse_mr(data):
    '''
    Parses the meaning represenation of the e2e challange dataset (mr column in csv)
    returns a list of tupels, with the name of the property as the first value and
    the data as the second.

    A column like 

    "name[Alimentum], area[city centre], familyFriendly[no]"

    results in

    [
        ('name_1', 'Alimentrum'),
        ('area_1', 'city'),
        ('area_2', 'centre'),
        ('familyFriendly_1', 'no')
    ]
    '''
    ret = []
    for prop in data.split(","):
        #print(prop)
        name, values = prop.strip().strip(']').split('[')
        for index, value in enumerate(values.split(' '), start=1):
            ret.append((name + "_" + str(index), value))

    return ret


def build_mr_line(mrs):
    return '\t'.join(mr[0] + ":" + mr[1] for mr in mrs)


def is_help():
    return True in ("help" in arg for arg in sys.argv)


start()
