def Fibo(a):
    if(a > 0):
        #Main loop
        Fibo(a - 1)
        print(Fibo(a * -1))
    elif(a < 0):
        #Secondery loop for a each place
        if(a >= -2):
            #First two places
            return 1
        return Fibo(a + 1) + Fibo(a + 2)
""" For example: "Fibo(5)" will give the output of: "1 1 2 3 5" """
