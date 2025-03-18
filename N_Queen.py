pos = [0]*8
flag_a = [False]*8
flag_b = [False]*15
flag_c = [False]*15

def put():
    for i in range(8):
      for j in range(8):
          print("O" if pos[i]== j else "X", end="")
      print()
    print()
    
def set(n:int):
    for j in range(8):
        if ( not flag_a[j]
             and not flag_b[n+j]
             and not flag_c[n-j+7] ):
            pos[n] = j
            if n==7:
                put()
            else:
                flag_a[j] = flag_b[n+j] = flag_c[n-j+7] = True
                set(n+1)
                flag_a[j] = flag_b[n+j] = flag_c[n-j+7] = False

set(0)