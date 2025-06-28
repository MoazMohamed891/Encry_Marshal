import marshal
import os
import sys
import sys
import time
##############################################################################################
print ("\033[31m")

os.system("figlet Hallo To Moaz Mohamed Script")

time.sleep(3)

os.system("clear")


print ("\033[1;31m")

print ("#"*67)

print ("\033[1;34m")

os.system('figlet Encry Marshal ')

print ("\033[1;31m")

print ("\033[35m")
print (" \033[93;5m⚡\033[0m \033[35mBY.Moaz Mohamed\033[93;5m ⚡\033[0m")
print ("\033[36m")
print ("Github : https://github.com/MoazMohamed891")
print ("Linkedin : https://www.linkedin.com/in/moaaz-mohamed-hassan-07604a348")
print ("\033[1;31m")

print ("#"*67)
##############################################################

print ("\033[1;34m")
file=input('File > ')
openfile=open(file,'r').read()
com=compile(openfile,'','exec')
encrypt=marshal.dumps(com)
enc=open('enc_'+str(file),'w')
enc.write('import marshal\n')
enc.write('exec(marshal.loads('+repr(encrypt)+'))')
print ('success encrypt | file save as enc_'+str(file))
