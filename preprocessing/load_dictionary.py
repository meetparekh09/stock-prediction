cons_words = {}
cons_words_set = set()

lit_words = {}
lit_words_set = set()

neg_words = {}
neg_words_set = set()

pos_words = {}
pos_words_set = set()

uncer_words = {}
uncer_words_set = set()

hrvd_pos_words = {}
hrvd_pos_words_set = set()

hrvd_neg_words = {}
hrvd_neg_words_set = set()

with open('../Harvard IV Psychological Dictionary/positiv.txt') as file:
    for line in file:
        line = line[:-1]
        if line not in hrvd_pos_words.keys():
            hrvd_pos_words[line] = 0
            hrvd_pos_words_set.add(line)

with open('../Harvard IV Psychological Dictionary/negativ.txt') as file:
    for line in file:
        line = line[:-1]
        if line not in hrvd_neg_words.keys():
            hrvd_neg_words[line] = 0
            hrvd_neg_words_set.add(line)

with open('../Loughran-McDonald Dictionary/final_constraining.txt') as file:
    for line in file:
        line = line[:-1]
        if line not in cons_words.keys():
            cons_words[line] = 0
            cons_words_set.add(line)

with open('../Loughran-McDonald Dictionary/final_litiguous.txt') as file:
    for line in file:
        line = line[:-1]
        if line not in lit_words.keys():
            lit_words[line] = 0
            lit_words_set.add(line)


with open('../Loughran-McDonald Dictionary/final_negative.txt') as file:
    for line in file:
        line = line[:-1]
        if line not in neg_words.keys():
            neg_words[line] = 0
            neg_words_set.add(line)


with open('../Loughran-McDonald Dictionary/final_positive.txt') as file:
    for line in file:
        line = line[:-1]
        if line not in pos_words.keys():
            pos_words[line] = 0
            pos_words_set.add(line)


with open('../Loughran-McDonald Dictionary/final_uncertain.txt') as file:
    for line in file:
        line = line[:-1]
        if line not in uncer_words.keys():
            uncer_words[line] = 0
            uncer_words_set.add(line)


# print(pos_words)
