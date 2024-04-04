def new_func(*args, **kwargs):
    pass

# So when the above function is called, it returns the args into the args tuple and the kwargs into the kwargs dictionary


"""
a = lambda x, y: return x + y  its wrong , we don't need return in the lamda function
print (a(20, 15))
"""

if __name__ == '__main__':
    fruits = {'apple', 'banana', 'apple', 'lemon'}  # as its a set and it only counts distinct
    print(fruits)
    mylist = ['P', 'y', 't', 'h', 'o', 'n']
    print(mylist[1], mylist[-1])
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(mylist[4::4]) # 4 element and skipping 4
    print(mylist[3:16:4])  # Start with index 3 and then go till 16 with the step of 4
    