from time import time


def factorization(n):
    if n % 2 == 0:
        for i in range(2, int(n/2)):
            for j in range(2, int(n/2)):
                if i*j == n:
                    print(i, j)
                    return
    else:
        for i in range(2, int((n+1)/2)):
            for j in range(2, int((n+1)/2)):
                if i*j == n:
                    print(i, j)
                    return


n = int(input("N: "))
# start the timer
start = time()
factorization(n)
# stop the timer
end = time()
print("Elapsed time: {} seconds".format(end - start))
