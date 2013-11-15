out_file = raw_input("Input your file name: \n")
txt = open(out_file, 'w')

data = raw_input ("Input your file content: \n")

txt.write(data+'\n')

txt.close()
