x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

print "I said : %r."% x
# single-quote is included by double-cuote
# why only single-quote is printed ?
print "I also said : '%s'." % y

hilarious = False
# how can I know this %r refersto hilarious? see next line
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e



