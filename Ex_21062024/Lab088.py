#set, tuple, dictionary

a,b,c,d=10,20,30,40
t=(34,67,8,9)
# append is not availble in the tuple
#t.append() , tuple is immutable
#s.append() , set is mutable
new_t=t +(a,b,c,d) #tuple
add_t=t+ (4,) # tuple
print(new_t)
print(add_t)
# or we can convert tuple to list and then append
temp_list=list(add_t)
print(temp_list)
temp_list.append(100)
add_t=tuple(temp_list)
print(add_t)
