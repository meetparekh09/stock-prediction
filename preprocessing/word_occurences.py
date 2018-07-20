import os
import load_dictionary
import corenlp
import re

cons_words_count = 0
lit_words_count = 0
neg_words_count = 0
pos_words_count = 0
uncer_words_count = 0
hrvd_neg_words_count = 0
hrvd_pos_words_count = 0

date_regex = re.compile('\d{4}-\d{2}-\d{2}')
data = {}

with corenlp.CoreNLPClient(annotators="tokenize ssplit".split()) as client:
    with open('microsoft-sentence-split-new.txt') as file:
        date = ''
        for line in file:
            print(line)
            if line == '\n':
                date = ''
                continue
            elif date_regex.fullmatch(line[:-1]) is not None:
                if line[:-1] not in data.keys():
                    data[line[:-1]] = {'cons': 0, 'lit': 0, 'neg': 0, 'pos': 0, 'uncer': 0, 'hrvd_neg': 0, 'hrvd_pos': 0}
                    print('\n\n\n'+ line[:-1])
                    print(data[line[:-1]])
                    print('\n\n\n')
                date = line[:-1]
                continue
            ann = client.annotate(line)
            for i in range(len(ann.sentence[0].token)):
                word = ann.sentence[0].token[i].word.upper()
                if word in load_dictionary.cons_words_set:
                    load_dictionary.cons_words[word] += 1
                    data[date]['cons'] += 1
                    cons_words_count += 1
                if word in load_dictionary.lit_words_set:
                    load_dictionary.lit_words[word] += 1
                    data[date]['lit'] += 1
                    lit_words_count += 1
                if word in load_dictionary.neg_words_set:
                    load_dictionary.neg_words[word] += 1
                    data[date]['neg'] += 1
                    neg_words_count += 1
                if word in load_dictionary.pos_words_set:
                    load_dictionary.pos_words[word] += 1
                    data[date]['pos'] += 1
                    pos_words_count += 1
                if word in load_dictionary.uncer_words_set:
                    load_dictionary.uncer_words[word] += 1
                    data[date]['uncer'] += 1
                    uncer_words_count += 1
                if word in load_dictionary.hrvd_neg_words_set:
                    load_dictionary.hrvd_neg_words[word] += 1
                    data[date]['hrvd_neg'] += 1
                    hrvd_neg_words_count += 1
                if word in load_dictionary.hrvd_pos_words_set:
                    load_dictionary.hrvd_pos_words[word] += 1
                    data[date]['hrvd_pos'] += 1
                    hrvd_pos_words_count += 1


print('Constraining Word Count :: ' + str(cons_words_count))
print('Litiguous Word Count :: ' + str(lit_words_count))
print('Negative Word Count :: ' + str(neg_words_count))
print('Positive Word Count :: ' + str(pos_words_count))
print('Uncertain Word Count :: ' + str(uncer_words_count))
print('Hrvd Positive Word Count :: ' + str(hrvd_pos_words_count))
print('Hrvd Negative Word Count :: ' + str(hrvd_neg_words_count))


with open('data.csv', 'w') as file:
    file.write('date, cons, lit, neg, pos, uncer, hrvd_neg, hrvd_pos\n')
    dates = data.keys()
    dates.sort()
    for date in dates:
        file.write(date + ',' \
        + str(data[date]['cons']) + ',' \
        + str(data[date]['lit']) + ',' \
        + str(data[date]['neg']) + ',' \
        + str(data[date]['pos']) + ',' \
        + str(data[date]['uncer']) + ',' \
        + str(data[date]['hrvd_neg']) + ',' \
        + str(data[date]['hrvd_pos']) + '\n')
