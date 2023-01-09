import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Call remote procedure 1
x = 10
result = proxy.procedure1(x)
print(result)

# Call remote procedure 2
x = 5
y = "Hello"
result = proxy.procedure2(x, y)
print(result)

# Call remote procedure 3
x = 3
result = proxy.procedure3(x)
print(result)