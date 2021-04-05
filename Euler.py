def fat(i):
    if isinstance(i,int):
        if i==0:
            return 1
        elif i>=1:
            return i*(fat(i-1))
        else:
            return None
def Euler(n):
    if n==0:
        return None
    elif n==1:
        return (1/fat(n))
    else:
        return (1/fat(n-1)+Euler(n-1))
def main(n):
    if n>=0:
        print("Número de termos: {}".format(n))
        print("Resultado: {}".format(Euler(n)))
    else:
        print("Error")
    
