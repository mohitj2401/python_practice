def timeConversion(s):
    
    ls=s.split(':')
    curr=ls[2][-2:]
    print(curr)
    if(curr=='PM'):
       if(int(ls[0])<12):
            ls[0]=int(ls[0])+12
    if(curr=='AM' and int(ls[0])==12):
        ls[0]='00'
    withoutcurr=ls[2].replace(curr,'')
    
    
    return str(ls[0])+':'+ls[1]+':'+withoutcurr