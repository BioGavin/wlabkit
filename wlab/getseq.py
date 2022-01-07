#!/usr/bin/env python


def get_target_seq(input, list, output, local_matching=False):
    with open(list, 'r') as f1:
        acc_ls = f1.readlines()
    with open(input, 'r') as f2:
        rna_db_ls = f2.readlines()
    new_rna_db_ls = []
    flag = 0
    for line in rna_db_ls:
        if line.startswith(">"):
            if local_matching:
                seqacc = line[1:].split(' ', 1)[0] + '\n'
            else:
                seqacc = line[1:]

            if seqacc in acc_ls:
                flag = 1  # target seq
            else:
                flag = 0  # not target seq
        if flag == 1:
            new_rna_db_ls.append(line)
    with open(output, 'w') as f3:
        f3.writelines(new_rna_db_ls)


def test(i):
    print(i)