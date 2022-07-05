import  requests    

result = requests.get( "https://jsonplaceholder.typicode.com/todos" )
geriBildirim = requests.get("https://jsonplaceholder.typicode.com/todos")
# result= result.text
print(geriBildirim)
# print(result)
# print(type(result))
print("deneneme")