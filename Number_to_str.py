tens={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
tmul={20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninty'}
elevens={10:'Ten',11:'Eleven',12:'Tweleve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen'}
sizerange={3:'Hundred',4:'Thousand',5:'Thousand',6:'Lakhs',7:'Lakhs'}
def twod(number):
    if number<1:
        print("")
    else:
        if number > 9 and number < 20:
            return elevens[number]
        elif number<10:
            return tens[number]
        elif number>19 and number < 100:
            if(number%10 == 0):
                return tmul[number]
            else:
                fp=number%10
                return tmul[number-fp]+' '+tens[fp]
        

def threed(number):
    if number<1:
        print("")
    else:
        s=str(number)
        fp=s[0]
        fp=int(fp)
        td=s[1]+s[2]
        td=int(td)
        print(tens[fp],sizerange[3],end=" ")
        print(twod(td))
    return ""
def fourd(number):
    if number<1:
        print("")
    else:
        s=str(number)
        fp=s[0]
        fp=int(fp)
        td=s[1]+s[2]+s[3]
        td=int(td)
        print(tens[fp],sizerange[4],end=" ")
        print(threed(td))
    return ""

def fived(number):
    s=str(number)
    fp=s[0]+s[1]
    fp=int(fp)
    td=s[2]+s[3]+s[4]
    td=int(td)
    print(twod(fp),end=" ")
    print(sizerange[5],end=" ")
    print(threed(td))
    return ""

def sixd(number):
    s=str(number)
    fp=s[0]
    fp=int(fp)
    td=s[1]+s[2]+s[3]+s[4]+s[5]
    td=int(td)
    print(twod(fp),end=" ")
    print(sizerange[6],end=" ")
    print(fived(td))
    return ""

def sevend(number):
    s=str(number)
    fp=s[0]+s[1]
    fp=int(fp)
    td=s[2]+s[3]+s[4]+s[5]+s[6]
    td=int(td)
    print(twod(fp),end=" ")
    print(sizerange[6],end=" ")
    print(fived(td))
    return ""
#inputs
number=int(input())
size=len(str(number))
if(size<3):
    twod(number)
elif(size>2 and size<4):
    if(number==100):
        print('One Hundred')
    else:    
        threed(number)
elif(size>3 and size<5):
    if(number==1000):
        print('One Thousand ')
    else:    
        fourd(number)
elif(size>4 and size<6):
    fived(number)
elif(size>5 and size<7):
    sixd(number)
elif(size>6 and size<8):
    sevend(number)
else:
    print('Enter a valid response ! ')