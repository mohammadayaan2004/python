myDic={
    "fast" : "In a quick manner",
    "harry":"A coder",
    "marks":True,
    "list" :[34,65.5,"Ayaan"],
    "tuple":(34,67.43,"swgyuw"),
    1:2
}

#dictionary.get -->> return the values of specified keys
print(myDic.get("list"))
print(myDic["list"])

#difference between .get and square method is .get will print "None"   
# if keys is not present but square methos will return error
print(myDic.get("lsoi"))

#print(myDic["lsirrjof"])--->>>error 