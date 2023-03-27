def spell(txt):
    #caso base
    if (txt == ""):
        return txt
    #recursion
    return (spell(txt[1:]) + txt[0])
    

txt = input()
print(spell(txt))

"""
HELLO
01234

43210

"""