#！/usr/bin/python
# -*- coding:utf8 
import copy
init = [
    [2,0,3],
    [1,8,4],
    [7,6,5]
]
target = [
    [1,2,3],
    [8,0,4],
    [7,6,5]]
i,j = 0,1
a = copy.deepcopy(init)
def up():
    global a,i,j
    if i >= 1:
        a[i][j],a[i-1][j] = a[i-1][j],a[i][j]
        i -= 1

def down():
    global a,i,j
    if i <= 1:
        a[i][j],a[i+1][j] = a[i+1][j],a[i][j]
        i += 1

def left():
    global a,i,j
    if j >= 1:
        a[i][j],a[i][j - 1] = a[i][j - 1],a[i][j]
        j -= 1

def right():
    global a,i,j
    if j <= 1:
        a[i][j],a[i][j+1] = a[i][j+1],a[i][j]
        j += 1

def h():
    jj = 0
    for row in [0,1,2]:
        for col in [0,1,2]:
            if a[row][col] != target[row][col]:jj += 1
    return jj

def mini(*arg):
    return reduce(min,arg)

opened = [[a,None,0,h(),h(),i,j]]
# closed = []
step = 0
while opened:
    p = opened[0]
    del opened[0]
    a = p[0]
    i = p[5]
    j = p[6]
    print "this move a :" ,a,"last move is ",p[1],"h,g,f:",p[3],p[2],p[4]
    step = p[2] + 1
    dspend,uspend,lspend,rspend = 999999,999999,999999,999999
    if p[3] == 0:
        print "solved "
        print "========== no move ============"
        continue
    print "analysis"
    if i >= 1 and p[1]!= "down":
        up()
        uspend = h()+step
        print "up is ok, a is:",a,"h,g,f is:",h(),step,uspend
        down()
    if i <= 1 and p[1]!="up":
        down()
        dspend = h()+step
        print "down is ok, a is:",a,"h,g,f is:",h(),step,dspend
        up()
    if j >= 1 and p[1]!="right":
        left()
        lspend = h()+step
        print "left is ok, a is:",a,"h,g,f is:",h(),step,lspend
        right()
    if j <= 1 and p[1]!="left":
        right()
        rspend = h()+step
        print "right is ok, a is:",a,"h,g,f is:",h(),step,rspend
        left()
    minii = mini(uspend,lspend,dspend,rspend)
    print "analysis end"
    if uspend == minii:
        up()
        print a,"up"
        opened.append([copy.deepcopy(a),"up",step,h(),uspend,i,j])
        down()
    if dspend == minii:
        down()
        print a,"down"
        opened.append([copy.deepcopy(a),"down",step,h(),dspend,i,j])
        up()
    if lspend == minii:
        left()
        print a,"left"
        opened.append([copy.deepcopy(a),"left",step,h(),lspend,i,j])
        right()
    if rspend == minii:
        right()
        print a,"right"
        opened.append([copy.deepcopy(a),"right",step,h(),rspend,i,j])
        left()
    print "==================== one move ==================="
    print 
