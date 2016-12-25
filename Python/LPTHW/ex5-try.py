name = 'Aciie'
age = 24 # that's also real
height_cm = 168.0 # centimeters 
weight_kg= 55.0 # kilograms
eyes = 'black'
teeth = 'White'
hair = 'dark-brown'

height_ins = height_cm * 0.394
weight_lbs = weight_kg * 2.205
# here,  TypeErrot said that ^ is unsupported operand type(s) for 'float' and 'int'
IBM = weight_kg / ((height_cm ** 2) / 10000)

print "Let's talk about %s." % name
print "She's %d inches tall." % height_ins
print "She's %d pounds heavy." % weight_lbs
print "Actually that's not too heavy :P"
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s because she likes to clean her teeth everyday." % teeth

# Try to calculate my BMI
print "If my weight is %d kg and my height is %d cm" % (weight_kg, height_cm)
# If I use %d(which means integer) here it will print 0
# If I use %r it will print 1.9486961451247164e-07
print "Then my BMI is %.2f ."% IBM

