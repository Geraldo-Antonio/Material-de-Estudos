a = ['maça', 'banana', 'melancia', 'abacate', 'cenoura', 'a', 'asdasdasdasdas']
x = ['maça', 'banana', 'melancia', 'abacate', 'cenoura', 'a', 'asdasdasdasdas']
a.sort( key= lambda x: len(x))
sorted(x, reverse=True, key=lambda x: len(x))
print(x)
print(f"\n{a}")