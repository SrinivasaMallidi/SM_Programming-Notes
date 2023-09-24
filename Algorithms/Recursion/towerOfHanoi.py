def toh(n,frm,aux,to):
    if(n == 1):
        print("Move "+str(n)+" from "+frm+" to "+to)
        return
    toh(n-1,frm,to,aux)
    print("Move "+str(n)+" from "+frm+" to "+to)
    toh(n-1,aux,frm,to)

toh(4,'FROMROD','auxiliary rod','TOROD')
