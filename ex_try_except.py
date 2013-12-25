import sys

try:
    s = raw_input('pls enter something')
except EOFError:
    print '\nWhy did you do an EOF on me?'
    sys.exit()
except:
    print '\nSome error occurs'

print 'Done'
