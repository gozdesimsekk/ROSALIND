class Node:
    def __init__(self):
        self.s = {}

    def __repr__(self):
        return 'Node (q=%s)' % self.s

def parameter1(e, z):
    for x in e.s:
        data1[z] = x
        parameter1(e.s[x], z + 1)
        data1[z] = ''

    if z >= 20 and len(e.s) >= 2:
        new1.append(''.join(data1))

def parameter2(e, z):
    for x in e.s:
        data2[z] = x
        parameter2(e.s[x], z + 1)
        data2[z] = ''

    if z >= 20 and len(e.s) >= 2:
        new2.append(''.join(data2))

if __name__ == "__main__":
    with open('mrep.txt') as f:
        seq_str = f.readline().strip()
    
    s = seq_str + '$'
    root = Node()
    
    for i in range(len(s)):
        r = root
        for c in s[i:]:
            if not c in r.s:
                r.s[c] = Node()
            r = r.s[c]
    
    data1 = [''] * len(s)
    new1 = []
    
    s2 = seq_str[::-1] + '$'
    root2 = Node()
    
    for i in range(len(s2)):
        r = root2
        for c in s2[i:]:
            if not c in r.s:
                r.s[c] = Node()
            r = r.s[c]
    
    data2 = [''] * len(s)
    new2 = []
    
    parameter1(root, 0)
    parameter2(root2, 0)
    snew2 = set(new2)
    
    for i in new1:
        if i[::-1] in snew2:
            print(i)
