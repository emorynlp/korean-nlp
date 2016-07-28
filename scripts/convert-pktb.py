import re
import os
import sys
import glob

def breakMorhemes(morphemes):
    pos = list()
    tok = list()

    for morpheme in morphemes.split('+'):
        t = morpheme.split('/')
        pos.append(t[1])
        tok.append(t[0])

    return '('+'+'.join(pos)+' '+'+'.join(tok)+')'

IN_DIR = sys.argv[1]
MORPH  = re.compile('(\S+/[^\s\)]+)')

for filename in glob.glob(os.path.join(IN_DIR, '*.fid')):
    fin   = open(filename)
    raw   = open(filename+'.raw'  ,'w')
    parse = open(filename+'.parse','w')
    print filename
    first = True

    for line in fin:
        line = unicode(line, 'euc-kr').encode('utf-8')

        if line.startswith('<+'):
            continue
        elif line.startswith(';;'):
            raw.write(' '.join(line.split()[1:])+'\n')
            if first: first = False
            else: parse.write('\n')
        elif line.strip():
            for old in MORPH.findall(line):
                new = breakMorhemes(old)
                line = line.replace(old, new)
            parse.write(line)
