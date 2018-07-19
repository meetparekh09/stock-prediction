import pandas as pd

sheet_name = 'BigDict1a'
file_name = '../inquirerbasic.xls'

df = pd.read_excel(io=file_name)

positiv = df[df['Positiv'] == 'Positiv']
negativ = df[df['Negativ'] == 'Negativ']

neg = []
pos = []

for i in range(negativ.shape[0]):
    word = str(negativ.iloc[i]['Entry'])
    word = word.split('#')[0]
    if len(neg) > 0 and neg[-1] != word:
        neg.append(word)
    elif len(neg) == 0:
        neg.append(word)


for i in range(positiv.shape[0]):
    word = str(positiv.iloc[i]['Entry'])
    word = word.split('#')[0]
    if len(pos) > 0 and pos[-1] != word:
        pos.append(word)
    elif len(pos) == 0:
        pos.append(word)

with open('../Harvard IV Psychological Dictionary/negativ.txt', 'w') as file:
    for word in neg:
        file.write(word+'\n')

with open('../Harvard IV Psychological Dictionary/positiv.txt', 'w') as file:
    for word in pos:
        file.write(word+'\n')
