dic={0: 10, 1: 20}
dic[2]=30
print dic

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
newdic={}
newdic.update(dic1)
newdic.update(dic2)
newdic.update(dic3)
print newdic

a=input("key?")
if a in newdic:
    print "yes"
else:
    print "no"

for i in newdic:
    print newdic[i]

for key in sorted(newdic.keys()):
  print key, newdic[key]
