## Written by oreanroy

import socket
import subprocess


all_up_host = []

print ('''
 __    __    ______        _______.___________. __   __       _______ 
|  |  |  |  /  __  \      /       |           ||  | |  |     |   ____|
|  |__|  | |  |  |  |    |   (----`---|  |----`|  | |  |     |  |__   
|   __   | |  |  |  |     \   \       |  |     |  | |  |     |   __|  
|  |  |  | |  `--'  | .----)   |      |  |     |  | |  `----.|  |____ 
|__|  |__|  \______/  |_______/       |__|     |__| |_______||_______|
                                                                      
                                                                      .......................''')

# get host ip, adress fucntion
def get_host_name():
  return socket.gethostname()

def get_ip_normal():
  return socket.gethostbyname(get_host_name())

# virtual machines might give virtual/internal dhcp ip in that case this fucntion used  
def get_ext_ip():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 80))
  print(s.getsockname()[0])
  network_ip = s.getsockname()[0]
  s.close()
  return network_ip

print ('\n \n \n')
print("your computer name is: %r" % get_host_name())
print("and the ip adress is %r" % get_ip_normal())
print("and the ip adress on network is %s" % get_ext_ip())
print ('\n \n \n')

network_ip = get_ext_ip()


# get the first three terms of ip adress
def split_ip(ip):
  terms = ip.split('.')
  return terms[0:3]


# sends a simple icmp packet and checks if the host is up
def normal_scan(ip):
  return subprocess.call(['ping', '-c', '3', ip]) 


# this fcuntion goes through all possible ip adress on the network and tries to ping it
def run_scan_normal():
  for i in range(0, 255):
    adress=""
    split = split_ip(network_ip)
    for terms in split:
      adress=adress+terms+"."
    adress = adress+str(i) # construct the ip
    res = normal_scan(adress)
    if res == 0:
      print ("host %r is ok" % adress)
      all_up_host.append(adress)
    if res == 2:
      print ("host %r is down" % adress)
    else:
      print ("host %r does not exist" % adress)


# this fuction goes for detailed scan just incase the machine do not respond to unkown icmp requests
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


run_scan_normal()

print ("all the host up are.")
print (all_up_host) 
