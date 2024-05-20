
#creating a list

namrata_list = [1,2,3,4,5]

#adding an element to the list
namrata_list.append(6)

#removing an element from the list
namrata_list.remove(4)

#modifying an element in the list
namrata_list[1]=20

print("Updated list:" , namrata_list)




#creating a dictionary
namrata_dict = {'name':'Manisha', 'age':20, 'city': "Delhi"}

#adding
namrata_dict['gender'] = 'Female'

#removing
del namrata_dict['age']

#modifying
namrata_dict['city'] = 'Lahore'

print("Updated dictionary:" , namrata_dict)





#creating a set
namrata_set = {1,2,3,4,5,6}

#adding
namrata_set.add(8)

#removing
namrata_set.remove(3)

#modifying
namrata_set.discard(1)
namrata_set.add(30)

print("Updated Set:", namrata_set)