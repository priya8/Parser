from bs4 import BeautifulSoup
import urllib2
import io,re
with open("urls.txt","r") as f:
  content1 = f.readlines()
  length=len(content1)
  fo=open("output1.txt","w")
  for url in content1[:length]:
    #print url
    fo.write("\n")
    fo.write(url);
    con = urllib2.urlopen(url).read()
    content=con.lower()
    #fo.write(content)
    soup = BeautifulSoup(content)
    #print soup.title.string.encode('ascii', 'ignore')
    fo.write("\n")
    fo.write(soup.title.string.encode('ascii', 'ignore')+'\n')
    list = []
    count1=count2=count3=count4=count5=count6=count7=count8=counta=countb=countc=count9=count10=count11=0
    #for link in soup.find_all(''):
     #t=link.get_text()
    
    if re.findall("[Bb]uy\w*",content):
     count1=len(re.findall("[Bb]uy\w*",content))
    if re.findall("[Aa]cquire\w*",content):
     count2=len(re.findall("[Aa]cquire\w*",content))
    if re.findall("[Mm]erge\w*",content):
     count3=len(re.findall("[Mm]erge\w*",content))
    if re.findall("[Rr]aise\w*",content):
     count4=len(re.findall("[Rr]aise\w*",content))
    if re.findall("[Ff]und\w*",content):
     count5=len(re.findall("[Ff]und\w*",content))
    if re.findall("[Ss]ecure\w*",content):
     count6=len(re.findall("[Ss]ecure\w*",content))
    if re.findall("[Ss]hut\w*",content):
     count7=len(re.findall("[Ss]hut\w*",content))
    if re.findall("[Cc]lose\w*",content):
     count8=len(re.findall("[Cc]lose\w*",content))
     count9=count1+count2+count3
     count10=count4+count5+count6
     count11=count7+count8

     
    class KeyValue:
       def __init__(self,key,value):
        self.key=key
        self.value=value

       def __str__(self):
        return self.key+":"+str(self.value)

    class HashTable:
       SIZE=8

       def __init__(self):
        i=0
        self.list=[]
        while i<self.SIZE:
         self.list.append([])
         i=i+1

       def getValue(self,key):
        h = self.hash (key)
        bucket = self.list[h]
        for kv in bucket:
          if kv.key==key:
           return kv.value
       def setValue(self,key,value):
         h = self.hash(key)
# should search first so we don't put key in twice, but for now ignore
         self.list[h].append(KeyValue(key,value))

       def hash(self,key):
        i=0
        total=0
        while i<len(key):
         total = total+ord(key[i])
         i=i+1
         return total % self.SIZE

    htable= HashTable()
    #htable.setValue("buy",count1)
    #htable.setValue("acquire",count2)
    #htable.setValue("merge",count3)
    #htable.setValue("raise",count4)
    #htable.setValue("fund",count5)
    #htable.setValue("secure",count6)
    #htable.setValue("shut",count7)
    #htable.setValue("close",count8)
    htable.setValue("MA",count9)
    htable.setValue("GROWTH",count10)
    htable.setValue("CLOSURE",count11)

    #MA= htable.getValue("buy") + htable.getValue("acquire") + htable.getValue("merge")
    #GROWTH = htable.getValue("raise") + htable.getValue("fund") + htable.getValue("secure")
    #CLOSURE = htable.getValue("shut") + htable.getValue("close")
    #print MA
    #print GROWTH
    #print CLOSURE
    MA=htable.getValue("MA")
    GROWTH=htable.getValue("GROWTH")
    CLOSURE=htable.getValue("CLOSURE")
    list.append(MA)
    list.append(GROWTH)
    list.append(CLOSURE)
    #print list
    #print max(list)

    p={}
    p = {'MA':0,'GROWTH':0, 'CLOSURE':0}
    p['MA']=MA

    p['GROWTH']=GROWTH

    p['CLOSURE']=CLOSURE

    m=max(p, key=p.get)
    #print m
    fo.write("\n")
    fo.write(m)
    fo.write("\n")
