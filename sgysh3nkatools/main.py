from os import *


print("Using sgysh3nkatools.")

class Roleplay():
	def hate(who, howmany):
		if howmany >= 2:
			for i in range(howmany):
				print("I hate", who, "!")
		else:
			print("I hate", who, "!")
	def love(who, howmany):
		if howmany >= 2:
			for i in range(howmany):
				print("I love", who, "!")
			else:
				print("I love", who, "!")
	def kiss(who, howmany, whodoingit):
			if howmany >= 2:
				for i in range(howmany):
					print(whodoingit, "kissed", who)
				else:
					print(whodoingit, "kissed", who)
	def kill(who, howmany, whodoingit, secret):
		if howmany >= 2:
			for i in range(howmany):
				print(whodoingit, "killed", who)
		if howmany >= 2 and secret == "no":
			for i in range(howmany):
				print("Someone killed", who)
		if secret == "no":
			print("Someone killed", who)
		else:
			print(whodoingit, "killed", who)
	def lastwords(who, *, message):
		print(who, "last words is:", message)
	def dance(who):
		print(who, "dancing")

class System():
	def runc(*, command):
		system(command)
