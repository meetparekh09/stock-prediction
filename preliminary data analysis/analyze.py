import os

count = 0
microsoftHeadlineCount = 0
associatedHeadlineCount = 0
yearCount = {}
microsoftYearCount = {}
writeFile = open('./merged-file.txt', 'w')

filelist = os.listdir("../../Microsoft/The Wall Street Journal")
filelist.sort()
for filename in filelist:
    if filename.endswith(".txt"):
        print(os.path.join("../../Microsoft/The Wall Street Journal", filename))
        filepath = os.path.join("../../Microsoft/The Wall Street Journal", filename)

        startOfArticle = False
        bodyStart = False
        bodyEnd = True
        endOfArticle = True
        headline = ''
        body = ''
        date = ''

        with open(filepath) as file:
            # file.readline()
            for line in file:
                if line == '____________________________________________________________\n':
                    startOfArticle = not startOfArticle
                    endOfArticle = not endOfArticle
                if line == '\n':
                    continue
                if endOfArticle:
                    count += 1
                    writeFile.write(headline)
                    writeFile.write(date)
                    writeFile.write(body)
                    writeFile.write('\n\n')
                    # print(headline)
                    if 'Microsoft' in headline:
                        microsoftHeadlineCount += 1

                    if 'Microsoft' in headline or 'Skype' in headline or 'Xbox' in headline or 'Outlook' in headline or 'Windows' in headline:
                        associatedHeadlineCount += 1
                        if date != '':
                            year = int(date[-6:].replace(" ", ""))
                            if year in microsoftYearCount.keys():
                                microsoftYearCount[year] += 1
                            else:
                                microsoftYearCount[year] = 1
                            # print(year)
                    # print(body)
                    # print(date)

                    if date != '':
                        year = int(date[-6:].replace(" ", ""))
                        if year in yearCount.keys():
                            yearCount[year] += 1
                        else:
                            yearCount[year] = 1
                        # print(year)

                    headline = ''
                    body = ''
                    date = ''
                    endOfArticle = False
                    startOfArticle = True

                    # try:
                    #     year = int(s.split(',')[-1].replace(" ", ""))
                    #     print(year)
                    # except:
                    #     continue

                    continue

                if startOfArticle and line != '\n' and line != '____________________________________________________________\n' and headline == '':
                    headline = line
                if startOfArticle and line.startswith('Full text:'):
                    bodyStart = True
                    bodyEnd = False
                if startOfArticle and (line.startswith('Credit:') or line.startswith('Title:')) or line.startswith('Subject:'):
                     bodyStart = False
                     bodyEnd = True

                if startOfArticle and line.startswith('Publication date:'):
                    date = line

                if startOfArticle and bodyStart:
                    body += line

print(count)
print(microsoftHeadlineCount)
print(associatedHeadlineCount)

print(yearCount)
print(microsoftYearCount)
writeFile.close()
# count = 0
# microsoftHeadlineCount = 0
# associatedHeadlineCount = 0
# yearCount = {}
# microsoftYearCount = {}
#
# for filename in os.listdir("../../Microsoft/The Wall Street Journal Factiva"):
#     if filename.endswith(".txt"):
#         # print(os.path.join("../../Microsoft/The Wall Street Journal", filename))
#         filepath = os.path.join("../../Microsoft/The Wall Street Journal Factiva", filename)
#
#         startOfArticle = False
#         bodyStart = False
#         bodyEnd = True
#         endOfArticle = True
#         headline = ''
#         body = ''
#         date = ''
#
#         with open(filepath) as file:
#             for line in file:
#                 if line == '____________________________________________________________\n':
#                     startOfArticle = not startOfArticle
#                     endOfArticle = not endOfArticle
#                 if line == '\n':
#                     continue
#                 if endOfArticle:
#                     count += 1
#                     # print(headline)
#                     if 'Microsoft' in headline:
#                         microsoftHeadlineCount += 1
#
#                     if 'Microsoft' in headline or 'Skype' in headline or 'Xbox' in headline or 'Outlook' in headline or 'Windows' in headline:
#                         associatedHeadlineCount += 1
#                         if date != '':
#                             year = int(date[-6:].replace(" ", ""))
#                             if year in microsoftYearCount.keys():
#                                 microsoftYearCount[year] += 1
#                             else:
#                                 microsoftYearCount[year] = 1
#                             # print(year)
#                     # print(body)
#                     print(date)
#
#                     if date != '':
#                         year = int(date[-6:].replace(" ", ""))
#                         if year in yearCount.keys():
#                             yearCount[year] += 1
#                         else:
#                             yearCount[year] = 1
#                         print(year)
#
#                     headline = ''
#                     body = ''
#                     date = ''
#                     endOfArticle = False
#                     startOfArticle = True
#
#                     # try:
#                     #     year = int(s.split(',')[-1].replace(" ", ""))
#                     #     print(year)
#                     # except:
#                     #     continue
#
#                     continue
#
#                 if startOfArticle and line != '\n' and headline == '':
#                     headline = line
#                 if startOfArticle and line.startswith('Full text:'):
#                     bodyStart = True
#                     bodyEnd = False
#                 if startOfArticle and (line.startswith('Credit:') or line.startswith('Title:')):
#                      bodyStart = False
#                      bodyEnd = True
#
#                 if startOfArticle and line.startswith('Publication date:'):
#                     date = line
#
#                 if startOfArticle and bodyStart:
#                     body += line
