import socket


hostIp = socket.gethostbyname("google.com")


# ip = socket.gethostbyaddr(hostIp)
# print(ip)
# print(ip[2][0])

listX = str(list(socket.gethostbyaddr(hostIp)))

# word=[] 
# for x in range(2,len(listX)-2):
#     word.append(listX[x]) 
#     print(x)

# print(''.join(word))

# listY = socket.gethostbyaddr(hostIp)
# print(type(listY))
# for y in (listY):  
#     print(str(y))
print(listX)
actualList = []
actualList = list(listX)
print(actualList)
# print((list(listX)))
# print(len(list(listX)))

import socket

hostIp = socket.gethostbyname("google.com")

# ip = socket.gethostbyaddr(hostIp)
# print(ip)
# print(ip[2][0])

print("Grabbing IP Information: ", socket.gethostbyaddr(hostIp))
print("Type: ", type(socket.gethostbyaddr(hostIp)))
print("Converting to list")
listX = (list(socket.gethostbyaddr(hostIp)))

#delete/comment out line below to utilize the above function
#listX = ('nuq04s44-in-f14.1e100.net', [], ['142.251.46.174', '12354.5634','848484848'])
print(type(listX))

print("Printing Converted list: ", listX)
print()

print("Looping")
for x in range(len(list(listX))):
    print("index x: ", x)
    listX[x]
    # print(listX[x])
    # print(type(listX[x]))
    print()
    if type(listX[x]) is list:
        for y in range(len(listX[x])):
            print("index y: ", y)
            print(listX[x][y])
    print("-----------------")