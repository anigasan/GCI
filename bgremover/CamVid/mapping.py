import numpy as np

def parse_code(text):
    if len(text.strip().split("\t")) == 2:
        a, b = text.strip().split("\t")
        return tuple(int(i) for i in a.split(' ')), b
    else:
        a, b, c = text.strip().split("\t")
        return tuple(int(i) for i in a.split(' ')), c


def convert_one_label(i, failed_code, rows, cols, labels, code2id):
    res = np.zeros((rows, cols), 'uint8')

    for j in range(rows):
        for k in range(cols):
            try: res[j, k] = code2id[tuple(labels[i, j, k])]
            except: res[j, k] = failed_code
    return res


def decode(path_to_labels_list):
    label_codes, label_names = zip(*[parse_code(l) for l in open(path_to_labels_list)])
    label_codes, label_names = list(label_codes), list(label_names)  # combine into a list

    code2id = {v: k for k, v in enumerate(label_codes)}

    return label_codes, label_names, code2id


def map_labels(path_to_labels_list, labels, rows, cols):
    label_codes, label_names, code2id = decode(path_to_labels_list)
    n = len(labels)
    failed_code = len(label_codes) + 1
    labels_int = np.stack([convert_one_label(x, failed_code, rows, cols, labels, code2id) for x in range(n)])
    labels_int[labels_int == failed_code] = 0

    return labels_int





