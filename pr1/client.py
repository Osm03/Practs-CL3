# Design a distributed application using RPC for remote computation where client submits an
# integer value to the server and server calculates factorial and returns the result to the client
# program

import xmlrpc.client
server = xmlrpc.client.ServerProxy('http://localhost:8000')
n = int(input("Enter the number to calculate factorial: "))
result = server.calculate_factorial(n)
print(f"The factorial of {n} is: {result}")