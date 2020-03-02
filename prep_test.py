import argparse

"""
This script removes duplicates from a given .box file and creates a .summary file 
with multiple reference sentences per line in the format required by the e2e-metrics evaluation script
(see https://github.com/tuetschek/e2e-metrics)
"""


def prep(box, summary, new_box, new_summary):
    """
    Remove duplicates from box file and write multiple summary options in summary file
    (used by e2e-metrics script for evaluation)
    .box and .summary file have to be created WITHOUT -d option (see preprocess_e2e.py)
    """
    with open(box) as in_box, open(summary) as in_summary, open(new_box, "w") as box_out, open(new_summary, "w") as summary_out:
        prev_mr = ""
        for x, y in zip(in_box, in_summary):
            if x == prev_mr:
                summary_out.write(y)
            else:
                if prev_mr != "":
                    summary_out.write("\n")
                box_out.write(x)
                summary_out.write(y)
                prev_mr = x


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create input format (box and summary) from csv file')
    parser.add_argument('box', type=str, help='the .box test file with duplicates')
    parser.add_argument('summary', type=str, help='the .summary test file with duplicates')
    parser.add_argument('new_box', type=str, help='the output .box test file')
    parser.add_argument('new_summary', type=str, help='the output .summary test file')
    args = parser.parse_args()

    prep(args.box, args.summary, args.new_box, args.new_summary)
