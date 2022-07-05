mylist = [1,2,3]
myString ="my string"

print(len(mylist))
print(len( myString))

class Movie():
    def __init__(self, title, directory, duraction):
        self.title = title
        self.directory = directory
        self.duraction = duraction
        print("movie objesi olusturuldu")
    
    def __str__(self):
        return f"{ self.title } by {  self.directory } "

    def __len__(self):
        return self.duraction 

    def __del__(self):
        print("film silindi")

m = Movie("film adi", "yonetmen adi", 100)
print (str(mylist))
print( str( m ))

print(len(mylist))
print( len( m ) )

del m
print(m)