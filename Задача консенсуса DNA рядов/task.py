from collections import Counter

from typing import List


def get_consensus_str(list_: List[str]) -> str:

    consensus_str = ''

    for j in range(len(list_[0])):
        str_ = ''
        for i in range(len(list_)):
            str_ += list_[i][j]
        letters = Counter(str_)
        consensus_str += letters.most_common(1)[0][0]
    return consensus_str


if __name__ == '__main__':
    list_1 = ['ATTA', 'ACTA', 'AGCA', 'ACAA']
    print(get_consensus_str(list_1))    # ACTA
