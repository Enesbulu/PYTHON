"""x = 'global x'

def function():
    x = 'local x'
    print(x)
function()
print(x)"""

"""name = "Cinaar"
def changeName(new_name):
    #local
    name= new_name
    print(name)

changeName("Ada")
print(name)"""


"""name = "global string"
def greeting():
    #name = "Cinar"
    
    def hello():
        #name = "Ada"
        print("hello " + name )

    hello()
greeting()"""


x = 50
def test():
   global x
   print(f"x : {x}")
    
   x = 100
   print(f"change x to {x}")

test()
print(x)
