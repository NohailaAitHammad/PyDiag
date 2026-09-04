#
#f = {10, 2 + 8, 2**62 + 8}
#print(f)
#
#print(hash(hash(hash(10)))) # Sortie: 10
#print(hash(2+8)) # Sortie: 10
#print(hash(2**62 + 8))
#  # Sortie: 10
#print("docstring" == hash(hash("docstring")))
#print(hash("docstring"))
#print(hash(hash("docstring")))

def some(a,b):
    if b == 0:
        raise ValueError("Ivalid info")
    return a/b

try:
    a = some(10, 0)
except ValueError as e:
    print(e)
    raise

"""
ila khlina ghir message dial exception howa li tafficha tma fa hna ila knt chi couche akhra li rdi thdr 3la hdhci fa rh maradich t3rf achno kyn dkchi bch kndiro raise hit hiya kt3awd tpropage lina exception bi ga3 les info dialha bch hna ndiro liha handling  o dkchi 
"""
    
