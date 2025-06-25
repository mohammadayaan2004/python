myDic={
    "fast" : "In a quick manner",
    "harry":"A coder",
    "marks":True,
    "list" :[34,65.5,"Ayaan"],
    "tuple":(34,67.43,"swgyuw"),
    1:2,
    5.4:4.432,
}

print("\n",type(myDic.keys()))#class == keys
print("Keys : \n",list(myDic.keys()))#print keys of the dictionary

print("\n",list(myDic.values()))#print values of the dictionary
print("\n",myDic.values())#print values of the dictionary

print("\n",list(myDic.items()))#print keys and it values of the dictionary

#update the dictionary
updatemyDic={
    "Ayaan":"Failure",
}
myDic.update(updatemyDic)

print("\n",myDic)

myDic.update({"harry":"Khan"})
print("\n",myDic)

#dictionary.get -->> return the values of specified keys
print(myDic.get("list"))
print(myDic["list"])

#difference between .get and square method is .get will print "None"   
# if keys is not present but square methos will return error
print(myDic.get("lsoi"))

#print(myDic["lsirrjof"])--->>>error           