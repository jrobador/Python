def decor (func):
    def new_f(num):
        print ("***")
        func(num)
        print ("***")
        print ("END OF PAGE")
    return new_f

@decor
def invoice(num):
    print("INVOICE #" + num)

invoice(input())