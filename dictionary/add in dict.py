maths={'john':88.0, 'sam':77.0,'sohail':66}
print(maths)
maths.update({'bishnu':55,'hari':99})
print(maths)
dict={'sita':65,'gita':68}
final={}
for d in (maths,dict):
    final.update(d)
print(final)
if 'surasha'in final:
    print('key is presnt')
else:
    print('key is not present')