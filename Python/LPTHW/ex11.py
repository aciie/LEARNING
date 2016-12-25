print "How old are you?",
age = raw_input()
# we put comma at the end of the line, so print will not end in that line
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

# the output of height is a little strange
# 6'5 will be output like 6\'5"
print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# how can I avoid to show this \ in my output?
