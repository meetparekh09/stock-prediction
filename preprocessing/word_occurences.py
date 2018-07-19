import os
import load_dictionary
import corenlp

cons_words_count = 0
lit_words_count = 0
neg_words_count = 0
pos_words_count = 0
uncer_words_count = 0
hrvd_neg_words_count = 0
hrvd_pos_words_count = 0

with corenlp.CoreNLPClient(annotators="tokenize ssplit".split()) as client:
    with open('microsoft-sentence-split.txt') as file:
        for line in file:
            if line == '\n':
                continue
            ann = client.annotate(line)
            for i in range(len(ann.sentence[0].token)):
                word = ann.sentence[0].token[i].word.upper()
                if word in load_dictionary.cons_words_set:
                    load_dictionary.cons_words[word] += 1
                    cons_words_count += 1
                if word in load_dictionary.lit_words_set:
                    load_dictionary.lit_words[word] += 1
                    lit_words_count += 1
                if word in load_dictionary.neg_words_set:
                    load_dictionary.neg_words[word] += 1
                    neg_words_count += 1
                if word in load_dictionary.pos_words_set:
                    load_dictionary.pos_words[word] += 1
                    pos_words_count += 1
                if word in load_dictionary.uncer_words_set:
                    load_dictionary.uncer_words[word] += 1
                    uncer_words_count += 1
                if word in load_dictionary.hrvd_neg_words_set:
                    load_dictionary.hrvd_neg_words[word] += 1
                    hrvd_neg_words_count += 1
                if word in load_dictionary.hrvd_pos_words_set:
                    load_dictionary.hrvd_pos_words[word] += 1
                    hrvd_pos_words_count += 1


print('Constraining Word Count :: ' + str(cons_words_count))
print('Litiguous Word Count :: ' + str(lit_words_count))
print('Negative Word Count :: ' + str(neg_words_count))
print('Positive Word Count :: ' + str(pos_words_count))
print('Uncertain Word Count :: ' + str(uncer_words_count))
print('Hrvd Positive Word Count :: ' + str(hrvd_pos_words_count))
print('Hrvd Negative Word Count :: ' + str(hrvd_neg_words_count))
