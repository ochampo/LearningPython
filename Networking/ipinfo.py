import socket


hostIp = socket.gethostbyname("google.com")


ip = socket.gethostbyaddr(hostIp)
print(ip)
print(ip[2][0])

listX = str(list(socket.gethostbyaddr(hostIp)[2]))

word=[] 
for x in range(2,len(listX)-2):
    word.append(listX[x]) 
    print(x)

print(''.join(word))
