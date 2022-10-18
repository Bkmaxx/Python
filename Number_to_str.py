tens={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
tmul={20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninty'}
elevens={10:'Ten',11:'Eleven',12:'Tweleve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen'}
sizerange={3:'Hundred',4:'Thousand',5:'Thousand',6:'Lakhs',7:'Crore'}
def twod(number):
    if number<1:
        return 'Zero ^_^'
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
        s=''    
    else:
        s=str(number)
        fp=s[0]
        fp=int(fp)
        td=s[1]+s[2]
        if s[1]=='0' and s[2]=='0':
            return tens[fp]+' '+'Hundred' 
        td=int(td)
        s=tens[fp]+' '+sizerange[3]+' '+twod(td)
    return s
def fourd(number):
    if number<1:
        o=''
    else:
        s=str(number)
        fp=s[0]
        fp=int(fp)
        td=s[1]+s[2]+s[3]
        td=int(td)
        if td==0:
            return tens[fp]+' '+'Thousand'
        o=tens[fp]+' '+sizerange[4]+' '+threed(td)
    return o
def fived(number):
    s=str(number)
    fp=s[0]+s[1]
    fp=int(fp)
    td=s[2]+s[3]+s[4]
    td=int(td)
    
    o=twod(fp)+' '+sizerange[5]+' '+threed(td)
    return o 
def sixd(number):

    s=str(number)
    fp=s[0]
    fp=int(fp)
    td=s[1]+s[2]+s[3]+s[4]+s[5]
    td=int(td)
    if td==0:
            return tens[fp]+' '+'Lakh'
    o=twod(fp)+' '+sizerange[6]+' '+fived(td)
    return o
def sevend(number):
    s=str(number)
    fp=s[0]+s[1]
    fp=int(fp)
    td=s[2]+s[3]+s[4]+s[5]+s[6]
    td=int(td)
    if td==0:
            return twod(fp)+' '+'Lakhs'
    o=twod(fp)+' '+sizerange[6]+' '+fived(td)
    return o 
def eightd(number):
    s=str(number)
    fp=s[0]
    fp=int(fp)
    td=s[1]+s[2]+s[3]+s[4]+s[5]+s[6]+s[7]
    td=int(td)
    if td==0:
            return twod(fp)+' '+'Crore'
    o=twod(fp)+' '+sizerange[7]+' '+sevend(td)
    return o
def nined(number):
    s=str(number)
    fp=s[0]+s[1]
    fp=int(fp)
    td=s[2]+s[3]+s[4]+s[5]+s[6]+s[7]+s[8]
    td=int(td)
    if td==0:
            return twod(fp)+' '+'Crore'
    o=twod(fp)+' '+sizerange[7]+' '+sevend(td)
    return o 
#inputs
print("Number To String [Ones ~ Crore] ")
number=int(input('Enter Your Number  :  '))
size=len(str(number))
if(size<3):
    print(twod(number))
elif(size>2 and size<4):  
    print(threed(number))
elif(size>3 and size<5):   
    print(fourd(number))
elif(size>4 and size<6):
    print(fived(number))
elif(size>5 and size<7):
    print(sixd(number))
elif(size>6 and size<8):
    print(sevend(number))
elif(size>7 and size<9):
    print(eightd(number))
elif(size==9):
    print(nined(number))
else:
    print('Enter a valid response ! ')
