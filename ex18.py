# this one is like your scripts with argv
def two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2:%r" % (arg1, arg2)

#ok, that *args is actually pointless, we can just do this
def two_again(arg1, arg2):
    print "arg1: %r, arg2:%r" % (arg1, arg2)

# this just takes one argument
def one(arg1):
   print "arg1: %r" %arg1

# this one takes no arguments
def none():
    print "I got nothing'."


two("Zed", "Shaw")
two_again("Zed","Shaw")
one("First!")
none()
