def yida(*argv):
    x,y,z = argv
    print "the first line is %s\n" %x
    print "the secod line is %s\n" %y
    print "the third line is %s\n" %z

first_line = raw_input("plsease input the first line :\n")
second_line = raw_input ("please input the second line: \n")
third_line = raw_input ("please input the third line: \n")

print "here comes the result you input:\n"
yida(first_line, second_line, third_line)
