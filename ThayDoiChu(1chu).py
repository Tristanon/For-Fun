with open('New.txt') as tri:
    data = tri.readlines()
    length = len(data)
    new_write = ''
    for i in range(length):
        linedata = data[i].split()
        lenofline = len(linedata)
        idxofword = 0
        while idxofword < lenofline:
            if linedata[idxofword] == 'Kteam' and idxofword != 0:
                linedata[idxofword - 1] = 'How'
            idxofword +=1
        new_write = new_write + ' '.join(linedata) + '\n'

with open('New.txt','w') as new_tri:
    new_tri.write(new_write)


