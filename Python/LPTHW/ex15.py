from sys import argv

# we get a filename, here it is ex15_example.txt
script, filename = argv

# open(name[mode[,buffering]])
# examples: x=open('c:\text\a.txt','r')
# you will awlays need a variable equals to open()
# notice "" or '' in your open()

# r=read w=write others:w, a, b, +
# we firstly open a file,then we can read,write and close this file
txt = open(filename)

print "Here's is your file %r:" % filename
# . dot means now you want this file to do (sth after dot)
print txt.read()
# we can also do some similar stuff
# txt.write('Hello,')
# txt.close()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
