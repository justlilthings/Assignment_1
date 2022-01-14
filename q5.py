#quetion 5

#(a)  print a list and then remove 4th element from the list and let it print the new list
_list=['Red','Green','White','Black','Pink','Yellow']
# removing 4th element that is black
_list.pop(3)
print(_list)


#(b) remove 'Black' and 'Pink' from the list and replace it with 'Purple'
_list=['Red','Green','White','Black','Pink','Yellow']
#replace black and pink with purple
_list[3:5]=['Purple']
print(_list)