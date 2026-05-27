def fun_loop (n):
    if n > 0:
        print(n)
        n-=1
    elif n < 0:
        n += 1
        print(n)
    else : 
        print(n)
        return
    fun_loop(n)
fun_loop(5)
