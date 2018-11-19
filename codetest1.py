import sys

def check_indent(s1, cur, prev, laststr):
    ind = str(cur)
    prev = len(s1)
    ls1 = len(laststr)
    #print cur, prev, ls1
    cnt = i = 1
    while(cnt<prev):
        if(ls1>prev):
            i += 1
        ind += '.'+str(i)
        cnt += 1
    return ind

def read_lines_from_file(filename):
    data = open(filename, 'r')
    lst = data.readlines()
    return lst

def format_text(lst):
    n = len(lst)
    cur = prev = 0
    laststr = 0
    c = l = 0
    for line in lst:
       c += 1
       if line == '\n':
            continue
       else:
        tmp = line.split(' ')
        checkstr = tmp[0]
        if checkstr.startswith('*'):
            if (len(checkstr) == 1):
                cur += 1
                print str(cur) +' '+ ' '.join(tmp[1:])
            else:
                prev = cur
                ind = check_indent(checkstr, cur, prev, laststr)
                print ind +' '+' '.join(tmp[1:])
            laststr = checkstr

        elif checkstr.startswith("."):
            cl = 0
            text1 = ""
            l = len(checkstr)
            if(c < n-1):
                nchs = lst[c+1].split(' ')[0]
                if(nchs.startswith('.')):
                    cl = len(nchs)
                    #print nchs
            #print cl,l
            if(l<cl):
                text1 += '+'
            else:
                text1 += '-'

            text1 += ' '+' '.join(tmp[1:])
            print "".ljust(l)+text1
        else:
            line = '  '+line.strip('\n')
            print "".ljust(l)+line

if __name__ == '__main__':
    #filen = "C:\Users\mns1\Documents\codetest.txt"
    filen = sys.argv[1]
    res = read_lines_from_file(filen)
    format_text(res)
