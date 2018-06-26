import corenlp

text = '''This intense ratings war means that folks at every network snipe at their competitors so that it's often hard to sort fact from spin. I've defended CNN against charges it was the Clinton News Network, although insiders there admit the network is now less biased since it let Rick Kaplan (a friend of Bill) go as president last summer. I've dismissed complaints that MSNBC is putting celebrity profiles and crime stories in its prime-time hours. Why let the vast film archives of NBC go to waste, and who says each network has to have the same type of programming during slow news cycles?'''

with corenlp.CoreNLPClient(annotators="tokenize ssplit".split()) as client:
    ann = client.annotate(text)

    for i in range(len(ann.sentence)):
        print(corenlp.to_text(ann.sentence[i]))
