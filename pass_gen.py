import time

#colors
red='\033[91m'
b='\033[21m'
green='\033[92m'
yellow='\033[93m'
cyan='\033[96m'
blue='\033[94m'
#logo
print (green+b+"""
             IN THE NAME OF ALLAH WHO IS THE LORD OF LORDS, AND KING OF KINGS
(  __)\\ ____--------------WELCOME TO sumbicreaters------------•◈•
|__(~)    •||•SUMBI-CREATERS------•◈•
|__\~~) •||•Proud To Be A MUSLIM and PAKISTANI---------------•◈•
|__(-----\  •◈•------Pakistan-Zindabad--------•◈•
|__~~~\ •◈•-----█-------⑦-------█------•◈•
|__~~~\ •◈•-----█-------⑧-------█------•◈•
|__~~~\ •◈•-----█-------⑥-------█------•◈•
\033[1;91m=======================================
\033[1;96mAuthor  \033[1;93m: \033[1;92m Sumbicreaters
\033[1;96mInstagram \033[1;93m: \033[1;Black-Hat
\033[1;96mFacebook  \033[1;93m: \033[1;Sumbal
\033[1;96mGithub \033[1;93m: \033[1;92mhttps://github.com/sumbicreaters
\033[1;96mGithub \033[1;93m: \033[1;92mhttps://Youtube.com/Sumbii Tricky Wrold
\033[1;91m=======================================

"""+b+green)

print (red+b+"            <===[[ coded by SumbiCreator ]]===>"+b+red)
print (" ")
print (yellow+b+"     <---( search on youtube Sumbii Tricky World)--->"+b+yellow)
print (" ")

length=int(raw_input(cyan+b+"Enter the number of characters like (6,8,11,etc): "+b+cyan))
print (" ")
name=raw_input(cyan+b+"Name your wordlist with (.txt) extension: "+b+cyan)
tic = time.clock()
print (" ")
print (blue+b+"<======================{}===================>"+b+blue)
print (" ")
print (yellow+b+"Wordlist Generating Please Wait!"+b+yellow)
print (" ")
print (blue+b+"<===================={}=====================>"+b+blue)
print (" ")
lista=[0 for x in xrange(length)]
x=length-1
string="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
list_of_results=[]
file1=file(name,"w")
while(x>-1):
    result=""
    if lista[x]==len(string)-1:
        for z in xrange (length):
            result+=string[lista[z]]
        lista[x]=0
        x-=1
    elif x==length-1:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]+=1
    else:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]+=1
        if x>0:
            x+=1
        else:
            x=length-1
    file1.write(result+"\n")
toc = time.clock()
ttn = toc - tic
print (red+b+"<======================{}===================>"+b+red)
print (" ")
print (green+b+"Completed in "+str(ttn)+" seconds."+b+green)
print (" ")
print (green+b+"Please check "+str(name)+" in your lazy bee directoy"+b+green)
print (" ")
print (red+b+"<======================{}===================>"+b+red)
print (" ")
