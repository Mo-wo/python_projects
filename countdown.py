import time
def count_down():
    n = 10
    while n >= 1:
        print(n)
        time.sleep(1)
        n -= 1
    print("Blastoff!")

count_down()
