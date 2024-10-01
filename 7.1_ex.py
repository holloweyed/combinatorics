import itertools
numstr = '12345678'
word_elem = ''
word = set()
for n1 in numstr:
    for n2 in numstr:
        for n3 in numstr:
            for n4 in numstr:
                for n5 in numstr:
                    word_elem += n1 + n2 + n3 + n4 + n5
                    for i in set(itertools.permutations(word_elem, 5)):
                        word.add(''.join(i))
                        word_elem = ''

k = 0
f = open('file1.txt','w')
for i in word:
    f.write(i + '\n')
    k += 1
f.write("Количество слов: " + str(k))
f.close()