out_file = open('final_constraining.txt', 'w')
with open('constraining.txt') as file:
    for line in file:
        if line != '\n':
            out_file.write(line)
