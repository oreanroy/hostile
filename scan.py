import socket
import subprocess


all_up_host = []

# get host ip, adress fucntion
def get_host_name():
  return socket.gethostname()

def get_ip_normal():
  return socket.gethostbyname(get_host_name())

# virtual machines might give wrogng ip in that case this fucntion used  
def get_ext_ip():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 80))
  print(s.getsockname()[0])
  network_ip = s.getsockname()[0]
  s.close()
  return network_ip


print(" your computer name is: %r" % get_host_name())
print(" and the ip adress in %r." % get_ip_normal())
print(" and the ip adress on network is %s" % get_ext_ip())

network_ip = get_ext_ip()

print(network_ip[0:7])


# get the first three terms of ip adress
def split_ip(ip):
  terms = ip.split('.')
  return terms[0:3]


# sends a simple icmp packet and checks if the host is up
def normal_scan(ip):
  return subprocess.call(['ping', '-c', '3', adress]) and soc_test(adress)


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
  adress=""
  split = split_ip(network_ip)
  for terms in split:
    adress=adress+"."+terms
    adress = adress[1:]
  print adress
  adress = adress+"."+str(i)
  res = normal_scan(adress)
  if res == 0:
    print ("host %r is ok" % adress)
    all_up_host.append(adress)
  if res == 2:
    print ("host %r is down" % adress)
  else:
    print ("host %r does not exist" % adress)

print ("all the host up are.")

print ("all_up_host") 
