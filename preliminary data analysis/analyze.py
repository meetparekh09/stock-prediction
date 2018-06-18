import os

count = 0
microsoftHeadlineCount = 0
associatedHeadlineCount = 0

for filename in os.listdir("../../Microsoft/The Wall Street Journal"):
    if filename.endswith(".txt"):
        # print(os.path.join("../../Microsoft/The Wall Street Journal", filename))
        filepath = os.path.join("../../Microsoft/The Wall Street Journal", filename)

        startOfArticle = False
        bodyStart = False
        bodyEnd = True
        endOfArticle = True
        headline = ''
        body = ''
        date = ''
        with open(filepath) as file:
            for line in file:
                if line == '____________________________________________________________\n':
                    startOfArticle = not startOfArticle
                    endOfArticle = not endOfArticle
                if line == '\n':
                    continue
                if endOfArticle:
                    count += 1
                    print(headline)
                    if 'Microsoft' in headline:
                        microsoftHeadlineCount += 1

                    if 'Microsoft' in headline or 'Skype' in headline or 'Xbox' in headline or 'Outlook' in headline or 'Windows' in headline:
                        associatedHeadlineCount += 1
                    # print(body)
                    # print(date)
                    headline = ''
                    body = ''
                    date = ''
                    endOfArticle = False
                    startOfArticle = True
                    continue

                if startOfArticle and line != '\n' and headline == '':
                    headline = line
                if startOfArticle and line.startswith('Full text:'):
                    bodyStart = True
                    bodyEnd = False
                if startOfArticle and (line.startswith('Credit:') or line.startswith('Title:')):
                     bodyStart = False
                     bodyEnd = True

                if startOfArticle and line.startswith('Publication date:'):
                    date = line

                if startOfArticle and bodyStart:
                    body += line

print(count)
print(microsoftHeadlineCount)
print(associatedHeadlineCount)
