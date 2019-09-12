import socket
import subprocess

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


all_up_host = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
network_ip = s.getsockname()[0]
s.close()

print(" your computer name is: %r" % hostname)
print(" and the ip adress in %r." % IPAddr)
print(" and the ip adress on network is %s" % network_ip)

print(network_ip[0:7])

addrr = network_ip[0:7]


def soc_test(add):
  print ("the socket fucntion was called")
  ports = [20,21,22,23,25,80,111,443,445,631,993,995,135,137,138,139,548,631]
  socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  socket.setdefaulttimeout(1)
  for port in ports:
#    print port
    result = socket_obj.connect_ex((add,port))
    if result == 0:
      print("this host is up at port number %s" %port)
      break
  socket_obj.close()
  print ("the value of result is %s"%result)
  if result == 0:
    return 0
  else:
    return 2

for i in range(0, 25):
  adress = addrr+str(i)
  res = subprocess.call(['ping', '-c', '3', adress]) and soc_test(adress)
  if res == 0:
    print ("host %r is ok" % adress)
    all_up_host.append(adress)
  if res == 2:
    print ("host %r is down" % adress)
  else:
    print ("host %r does not exist" % adress)

print ("all the host up are.")

print all_up_host 
