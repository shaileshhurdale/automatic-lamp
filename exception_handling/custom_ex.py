class IllegalAgeForVote(RuntimeError):
   def __init__(self, arg):
      self.args = arg
	  
	  
age=15;

try:
	if age<18:
		raise IllegalAgeForVote("Illegal age for voting");
	else:
		print("you are illigible for voting");
except IllegalAgeForVote as e:
	print("Exception in code: "+''.join(e.args));
finally:
	print("cleaning up!");