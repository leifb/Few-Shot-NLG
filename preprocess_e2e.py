import os
import csv
import nltk
import argparse
import random

"""
This script converts the e2e challange dataset into a format the can be processed
with preprocess.py. It writes the Meaning Representations (MRs) to the specified .box file and 
the corresponding human language representations to the .summary file and creates a 
field_vocab.txt in the parent folder. 
Has to be called separately for train dev and test files, the vocab will be augmented accordingly.
"""

vocab = set()
cnt = 0

def run(src_path, box_path, sum_path, shuf, dup):
    # uncomment if vocab file does not exists yet
    # read in field vocab (if it exists)
    # global vocab, cnt
    # if os.path.exists("field_vocab.txt"):
    #     with open("field_vocab.txt", "r") as vocab_file:
    #         for line in vocab_file:
    #             word, id = line.strip().split()
    #             vocab.add(word)
    #             cnt = int(id)

    with open(src_path, 'r') as src:
        with open(box_path, 'w') as box:
            with open(sum_path, 'w') as sum:
                src_reader = csv.reader(src, delimiter=',', quotechar='"')
                next(src_reader, None)
                for row in src_reader:
                    if len(row) == 0:
                        print("WARNING: column without any data, ignoring line")
                        continue
                    if len(row) < 2:
                        print("WARNING: input column without summary, ignoring line")
                        continue
                    # TODO keep track of MRs to remove duplicates if dup (ideally before shuf)
                    data_box, data_sum = parse_row(row, shuf)
                    box.write(data_box)
                    box.write('\n')
                    sum.write(data_sum)
                    sum.write('\n')


def parse_row(row, shuf):
    """
    Parses a row of the e2e dataset csv and returns a  data for
    both the box file and the sumary file.
    """
    # convert meaning representation format
    mr_string = parse_mr(row[0], shuf)
    # tokenize summary string
    tok_sum = " ".join(nltk.word_tokenize(row[1]))

    return mr_string, tok_sum


def parse_mr(data, shuf):
    """
    Parses the meaning represenation of the e2e challange dataset (mr column in csv)
    returns a list of tupels, with the name of the property as the first value and
    the data as the second.

    A column like
    "name[Alimentum], area[city centre], familyFriendly[no]"

    results in
    name:Alimentum    area_1:city    area_2:centre    familyFriendly:no

    Also updates the field vocab file if new fields are encountered.

    :param data: the input MR (see above)
    :param shuf: whether to shuffle the fields of the meaning representation
    :return: tab separated line of : separated name value pairs
    """
    # uncomment if vocab file does not exists yet
    #global vocab, cnt
    mr = []
    old_mr = data.split(",")

    # shuffle MRs if required
    if shuf:
        random.shuffle(old_mr)

    for prop in old_mr:
        name, value = prop.strip().strip(']').split('[')
        name = name.strip().replace(" ", "_")

        # uncomment if vocab file does not exists yet
        # if name not in vocab:
        #     with open("field_vocab.txt", "a") as vocab_file:
        #         vocab_file.write("{} {}\n".format(name.replace(" ", "_"), cnt))
        #     vocab.add(name)
        #     cnt += 1

        # if multiple words in value, split and enumerate name tag
        if " " in value:
            for index, v in enumerate(value.split(' '), start=1):
                mr.append("{}_{}:{}".format(name, str(index), v))
        else:
            mr.append("{}:{}".format(name, value))

    return '\t'.join(mr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create input format (box and summary) from csv file')
    parser.add_argument('csv', type=str, help='the original csv file with MRs in the first and sentences in the second column')
    parser.add_argument('box', type=str, help='the .box output file')
    parser.add_argument('summary', type=str, help='the .summary output file')
    parser.add_argument('-s', '--shuffle', dest='shuf', default=False, action='store_true', help='shuffle order within MRs')
    parser.add_argument('-d', '--duplicates', dest='dup', default=True, action='store_false', help='allow duplicate MRs, if false, select one sentence randomly')
    args = parser.parse_args()

    run(args.csv, args.box, args.summary, args.shuf, args.dup)
