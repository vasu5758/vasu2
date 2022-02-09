# string_ = 'vasu gurram'
# for char in string_:
#     print(char,string_.find(char))
# string_= 'vasu gurram'
# for index in range(len(string_)):
#     print(string_[index],index)
# string_ = 'vasu gurram'
# for index, char in enumerate(string_):
#     print(index,char,end = ' ')
# name = 'gurramg vasug'
# print(name.lstrip('g'))
#
# print(name.upper())
# print(name.split('g'))
# print(name.split('g',1))
# string_ = '@vasu'
# print(string_.islower())
# print the characters and its ascii value
# a = 'hello world'
# l = ()
# for char in a:
#     l+=(char,ord(char))
# print(l)
# consonent
# a = 'vassssu'
# for name in a:
#     if name not in 'aeiouAEIOU':
#         print(name,'it is a consonent')
#     else:
#         print(name,'it is not consonent')
# a = 'vasu'
# tuple_ = ()
# for name in enumerate(a):
#     print(name)
# a = 'vasu'
# for rev in a[::-1]:
#     print(rev)
# for rev in reversed(a):
#     print(rev)
# # write a progrom to create a list of sequres for the elements in the below
list_ = [10,20,30,60]
# y = []
# for sequres in list_:
#     y.append(sequres**2)
# print(y)
# res = [i**2 for i in list_]
# print(res)
# l = []
# for index,item in enumerate(list_):
#     l.append(item)
# print(l)
# l_index = [item for item in enumerate(list_)]
# print(l_index)
# l = [10,20,30,50,7]
# l1 = []
# l2 = []
# for i in l:
#     if i%2==0:
#         l1.append(i)
#     else:
#         l2.append(i)
# print(l1,l2)
# l = list(range(10))
# even = [i for i in l if i%2==0]
# print(even)
# a = [10,20,50,60,7,'vasu','gurram']
# # res = {item for item in a if item%2==0}
# # print(res)
# res2 = {a[value] if type(a[value])==str and a[value] %2==0 for value in range(len(a))}
# print(res2)
# d = 'happy birthday'
# c = {}
# for i in set(d):
#     c[i]=d.count(i)
# print(c)
#
# l = ['vasu','gurram','balaji','venkat',10,888845]
# res = []
# for i in l:
#     if type(i)==str:
#         res.append(i)
#     elif type(i)==int:
#         res.append(str(i)[::-1])
# print(res)
# res = []
# out =[]
# for i in l:
#     if isinstance(i,str):
#         res.append(i[::-1])
#     else:
#         out.append(i)
# print(res,out)
# output = [item[::-1] if isinstance(item,str) else item for item in l]
# print(output)
# output1 = [str(item1)[::-1]if not isinstance(item1,str) else item1 for item1 in l]
# print(output1)
# res = {(item,l[item])for item in range(len(l))}
# print(res)
# res1 = {(index,value)for index,value in enumerate(l)}
# print(res1)
# res = {(item,l[item]) for item in range(len(l))}
# print(res)
a = 'vaaasu'
rev = [res for res in a if isinstance(res,str)]
print(rev)