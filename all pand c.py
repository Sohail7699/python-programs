for a in range(1,21):
    for i in range(2,a):
        if (a%i) == 0:
            print(a,"number is composite")
            break
    else:
            print(a,"it is prime")
