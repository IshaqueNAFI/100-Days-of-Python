import http.client
#'https://jsonplaceholder.typicode.com/todos/1'
#'heeps://rabbil.com'

#conn= http.client.HTTPConnection("jsonplaceholder.typicode.com")
conn1 = http.client.HTTPConnection("rabbil.com")
conn1.request("GEt", '/todos')
#conn.request("GET", '/ ')

#response = conn.getresponse()

response1 = conn1.getresponse()

#print (response.status)
#print(response.headers)
#print(response.read())


print(response1.status)
print(response1.read())
