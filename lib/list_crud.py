def create_an_empty_list():
    list =[]
    return list
print(create_an_empty_list())

def create_a_list():
    data=['Valid env','Feedback','Repetition','practice']
    return data
print(create_a_list())



def add_element_to_end_of_list(data, element):
    data=['Valid env','Feedback','Repetition','practice']
    data.append(element)
    return data
print(add_element_to_end_of_list('data',"Lets do the job and get paid "))




def add_element_to_start_of_list(data, element):
    data=['Boniface','Kiprotich']
    data.insert(0,element)
    return data
print(add_element_to_start_of_list("data",'Cheruiyot'))


def remove_element_from_end_of_list(data):
    data.pop()
    return data
print(remove_element_from_end_of_list(data=[1,2,3]))

def remove_element_from_start_of_list(data):
    data.pop(0)
    return data
print(remove_element_from_start_of_list(data=[1,2,34]))

def retrieve_first_element_from_list(l): 
    for i in l:
        return l[0]
print(retrieve_first_element_from_list(l=[99,10,9,8]))

def retrieve_element_from_index(l, index):
    for i in l:
        return l[index]
print(retrieve_element_from_index(l=[1,2,3],index=1))

def retrieve_last_element_from_list(l):
    length=len(l)
    return l[length-1]
print(retrieve_last_element_from_list(l=['a','e','i','o','u']))