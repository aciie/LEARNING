#import argument variables from system
from sys import argv

script, height, weight, hair = argv

print "Let's talk about Mrs. Li."
print "She's %r inches tall." % height
print "She's %r pounds heavy." % weight


age = raw_input("Oh! And how old is she? ")
print "OK, and Mrs. Li is %r years old with beautiful %r hair." % (age, hair)
