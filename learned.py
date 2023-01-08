-------------------
for str in 'string':
	print(str)
print("done")

for x in ["The", "rain", "in", "Spain"]:
	print(x)
print("Done")

----------------
import random
number = random.randint(1,999)

-----------------
counter = 0
while counter < 10:
counter += 1

----------------
import time
time.sleep(2)

-------------------
name = input("Enter your name:")

----------------------------------
class Member:
	def __init__(self, uname, fname):
		self.username = uname 
		self.fullname = fname
new_guy = Member('Rambo', 'Rocco Moe')
print(new_guy)
print(new_guy.username)
print(new_guy.fullname)
print(type(new_guy))

--------------------------------------------
Function 

def pickUp():
    backpack == empty
    if backpack = empty:
        print('picksUp')
    else:
        print('no space')

--------------------------------
Jan 7 practice

class Monster: 
	def __init__(self, paramatt, paramhp): #creates self obj and param att, hp
		self.attratt = paramatt  
		self.atthp = paramhp       
import random
vampire = Monster(random.randint(1,6), random.randint(10,20))
print(self.attratt)
print(self.atthp)

--------------------
Make 10 vamp
class Monster: 
	def __init__(self, paramatt, paramhp): #creates self obj and param att, hp
		self.attratt = paramatt  
		self.atthp = paramhp       
import random
counter = 0
while counter < 10:
    vampire = Monster(random.randint(1,6), random.randint(10,20))
    print(vampire.attratt)
    print(vampire.atthp)
    counter += 1
