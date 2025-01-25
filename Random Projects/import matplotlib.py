import matplotlib.pyplot as plt

def collatz(i):
    count = []
    iCollecter = []
    counter = 0
    while i != 1 :
        if (i % 2) == 0:
            i /= 2
        else:
            i = 3 * i + 1
        counter += 1
        count.append(counter)
        iCollecter.append(i)
        print("Count: ", counter, "\ti = " , i)
    
    plt.xlabel("Counter")
    plt.ylabel("i")

    plt.title("Collatz Conjecture")

    plt.scatter(count, iCollecter)
    plt.plot(count, iCollecter)

    plt.show()




    
collatz(12)

