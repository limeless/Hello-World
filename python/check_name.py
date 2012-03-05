# -*- coding: utf-8 -*-

intro = '''
#Simple Input Output Python Practice
#2012/01/20
#limelight.wang@gmail.com
'''

#this is checking code aera.
check_name = False

print intro

#program start.
print 'Please enter your name, so I can know your name.\n'

#Start Detect User name.
last_name = raw_input('Last Name: ')
first_name = raw_input('First Name: ')

#Start ask What Kind of name 
print 'Now, What Kind of name display would you like??'
print '1. Last First'
print '2. First Last\n'

#Start Checking Code.
while check_name == False:

	choose = int(input('Please Enter what you prefer: '))
	
	if choose == 1:
		print 'So this is what your name is: ',last_name ,first_name
		print '\n'
		check_name = True
	elif choose == 2:
		print 'So this is what your name is: ',first_name ,last_name
		print '\n'
		check_name = True
	else:
		print 'You are enter a wrong number, please choose again.\n'