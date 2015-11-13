#!/usr/bin/env python

import socket
import time

UDP_IP = "192.168.253.38"
UDP_PORT = 5000
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

""" using Python 2.7 and urllib and urllib2."""

import urllib.request
#from random import randint

public_hash     = '8X4kXblp1ETpE26WN3EbUdr1WY1'
private_hash    = 'ym9bm6OKBdcGDwZnx3DMHOAKe6K'
base_url        = 'http://192.168.253.38:8080'
public_url      = base_url + '/input/' + public_hash
private_url     = public_url + '?private_key='+ private_hash

def main():
    while True:
        recv_data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print ("received message:", recv_data)	
        if(recv_data != None):	
            Str = recv_data.decode("utf-8") 
            Str = Str.strip("b")
            Str = Str.strip("'")
            Inputs = Str.split()
            field1 = Inputs[0]
            field2 = Inputs[1]		
            data = private_url + '&random_value1=' + field1 + '&random_value2=' + field2
            print(field1 + "_" + field2 + '\n')
            print(data+'\n')
            f = urllib.request.urlopen(data).read()
            time.sleep(30)

if __name__ == "__main__":
    main()
