import time, threading

list1 = [1,2,3,4,5]
list2 = [2,4,6,8,10]

def natural_nums(lst1):
    for i in lst1:
        print(f"Natural Number: {i}")
        time.sleep(2)
        
def even_nums(lst2):
    for i in lst2:
        print(f"Even Number: {i}")
        time.sleep(2)

t1 = threading.Thread(target= natural_nums, args=(list1,))
t2 = threading.Thread(target= even_nums, args=(list2,))

t1.start()
t2.start()