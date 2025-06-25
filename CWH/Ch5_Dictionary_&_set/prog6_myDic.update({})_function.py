myDic={
    "fast" : "In a quick manner",
    "harry":"A coder",
    "marks":True,
    "list" :[34,65.5,"Ayaan"],
    "tuple":(34,67.43,"swgyuw"),
    1:2
}

#update the dictionary
updatemyDic={
    "Ayaan":"Failure",
}
myDic.update(updatemyDic)

print("\n",myDic)

myDic.update({"harry":"Khan"})
print("\n",myDic)