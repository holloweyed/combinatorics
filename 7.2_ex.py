import itertools
numstr = '12345678'
word_elem = ''
word = set()
for n1 in numstr:
    for n2 in numstr:
        if n1 != n2:
            for other in numstr:
                if other != n1 and other != n2:
                    for other2 in numstr:
                        if other2 != n1 and other2 != n2 and other2 != other:
                            word_elem += n1*3 + n2*2 + other + other2
                            for i in set(itertools.permutations(word_elem, 7)):
                                word.add(''.join(i))
                                word_elem = ''

k = 0
f = open('file1.txt','w')
for i in word:
    f.write(i + '\n')
    k += 1
f.write("Количество слов: " + str(k))
f.close()
