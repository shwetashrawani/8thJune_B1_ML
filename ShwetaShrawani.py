Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # QUESTION 2
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20;a+=30;a%=3;print(a)
2
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> #QUESTION 3
>>> s1="nice to have it"
>>> s2="here"
>>> s1 + ' ' + s2
'nice to have it here'
>>> #QUESTION 4
>>> a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][2]
['hello']
>>> #QUESTION 5
>>> a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a+=["nice to have it here"]
>>> a
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'nice to have it here']
>>> a[:0] + ["nice to have it here"] + a[0:]
['nice to have it here', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'nice to have it here']
>>> #QUESTION 6
>>> color_list_1=set(["White","Black","Red"])
>>> color_list_2=set(["Red","Green"])
>>> color_list_1.difference(color_list_2)
{'White', 'Black'}
>>> #QUESTION 8
>>> eval('{0}+{0}{0}+{0}{0}{0}'.format(input('Enter the number:')))
Enter the number:5
615
>>> #QUESTION 9
>>> d={'Student':['Rahul','Kishor','Vidhya','Raakhi'],'Marks':[57,87,65,79]}
>>> d['Marks']
[57, 87, 65, 79]
>>> max(d['Marks'])
87
>>> 