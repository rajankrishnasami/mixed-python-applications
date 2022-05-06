k = input()
for x in range(int(k[0])*1000,int(k[0])*1000+1000):
  f = open('log.txt','a')
  f.write("https://www.xyz.abc/files/" + str(x)+'\n')
  f.close()
