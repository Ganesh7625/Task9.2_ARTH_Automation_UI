#!/usr/bin/python3
print("content-type: text/plain")
print()
import subprocess as sp
import cgi
#form =   cgi.FieldStorage()
cmd1 = "sudo yum install httpd -y"
output1 = sp.getstatusoutput(cmd1)
status1 = output1[0]
out1 = output1[1]
cmd2 = "sudo systemctl start httpd"
output2 = sp.getstatusoutput(cmd2)
status2 = output2[0]
out2 = output2[1]
cmd3 = "sudo systemctl enable httpd"
output3 = sp.getstatusoutput(cmd3)
status3 = output3[0]
out3 = output3[1]
if status1 == 0 :
        print("Apache software installed successfully")
        if status2 == 0:
            print("Apache webserver service is started")
            if status3 == 0:
                print("Apache webservice is enabled")
            else:
                print("error occuring during Apache webservice enable")
                print(output3)
        else:
            print("error occuring during Apache webservice start")
            print(output2)
        print("Webserver Configured!!!")
else:
    print("error occuring during Apache webserver installing")
    print(output1)

~
