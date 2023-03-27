def convert(num):
   if (num == 0):
      return num
   else:  
      return (num % 2 + 10 * convert(num // 2)) 

print (convert(5))


"""
     convert(10):
        num = 0 ? NO
        return (0 + 10 * convert(5)) = 1010
   
    convert(5):
        num = 0 ? NO
        return (1 + 10 * 10) = 101

    convert(2):
        num = 0 ? NO
        return (0 + 10 * 1) = 10

    convert(1):
        num = 0 ? NO
        return (1 + 10 * 0) = 1

    convert(0):
        num = 0 ? SI -> 0

        """


