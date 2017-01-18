# Decorators
## A walk through a park of decorators

# Note to reader: un-comment function calls to see results

# Functions are objects (decorators later)
# 1
def basic_function():
	print 'howdy'

howdy = basic_function

# howdy()    # Function call, so uncomment it to see what it does.

# prints: 
# howdy

# Nested functions :: aka: higher-order functions (decorators later)
# Closure magic (Yes I know it\'s not really magic!)

def outer(parameter):
	def inner():
		print parameter
	return inner # We return the inner inside the outer. Wowza.
# Now we have 'closure'
# Access inner namespace from global namespace
inner_access = outer("I am inside a function which is itself inside a function.")
#Lets tap into inner()
#inner_access() # Function call, here!
#prints: I am inside a function which is itself inside a function.


# NOW DECORATORS

def decorator_one(virtual_function):
	def inner(*args, **kwargs):
		print "One"
		let_in = virtual_function(*args, **kwargs)
		print "Three"
		return let_in
	return inner

@decorator_one
def my_dec_func():
	print "Two"

# NOW we access and invade inner() by calling my_dec_func()
my_dec_func()		 # Function call, here!    

# Prints:
# One, Two, Three

























