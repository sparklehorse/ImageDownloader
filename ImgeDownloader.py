import urllib.request
import re
import os
import queue
import threading

class MyThread(threading.Thread):
        def __init__(self,myQueue):#passing myQueue
                #print(myQueue.get())
                print("init")
                threading.Thread.__init__(self)
                self.myQueue=myQueue
        def run(self):
                print("download")
                while(self.myQueue.empty()==False):
                        imgUrl=self.myQueue.get()
                        num=imgUrl.rfind('/')
                        imgName=imgUrl[(num+1):]
                        #urllib.request.urlretrieve(imgUrl,"F:\img\\"+imgname,reporthook)
                        #urllib.request.urlretrieve(imgUrl,"F:\img\\"+imgname)
                        try:
                                urllib.request.urlretrieve(imgUrl,"N:\image1\\"+imgName)#no dir dont stop
                        except Exception as err:
                                print(imgName,err)
                                #save the imgUrl that haven't been downloaded
                                self.myQueue.put(imgUrl)
                                
                        if(self.myQueue.empty()):
                                break
                #else:break
                
        
def reporthook(a,b,c):
        #print(a,b,c)
        percent=a*b/c*100
        if percent>100:
                percent=100
        print("%d %d"%(percent,(count+(a*b/c))/len(myItems)*100))

def getHtml():
        url="http://www.lingvistov.ru/doodles/#!prettyPhoto"
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        # note that Python3 does not read the html code as string
        # but as html code bytearray, convert to string with
        html = mybytes.decode("utf8")
        fp.close()
        return html
def getImgList():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        html=getHtml()
        pattern=re.compile(r'<a href=".*?.jpg')
        rawImgList= pattern.findall(html)
        count=0
        for count in range(0,len(rawImgList)):
        #for img in rawImgList:
                rawImgList[count]=rawImgList[count].replace('<a href="','')
                count+=1
                #print(img)
        #print(rawImgList)
        print('count is %d'%(count))
        return rawImgList
def download(myQueue):
        for i in range(0,40):#number of thread
                myThread=MyThread(myQueue)
                myThread.start()

def main():
        imgList=getImgList()
        myQueue=queue.Queue() #init queue
        '''
        for imgUrl in imgList:
                myQueue.put(imgUrl)
        '''
        for i in range(0,len(imgList)):
                myQueue.put(imgList[i])
        download(myQueue)
        
main()

