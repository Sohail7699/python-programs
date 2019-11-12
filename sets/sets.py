#3 sets of fruits.and then finding:repeated , unique and unrepeated items
a={'apple','orange','banana','pineapple'}
b={'watermelon,guava','peach','apple'}
c={'apple','mango',"guava"}
z=(a.intersection(b,c))
y=(a.difference(b,c))
x=(a.union(b,c))
w=(x.difference(z))
print("reapeated items",z)
print("unique items",w)
print("unrepeated items",x)



