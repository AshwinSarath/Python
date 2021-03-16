phone_book={}
name=str
number=int
print("Type NEW for new phone entry")
condition=str(input())
if(condition=="NEW"or"new"):
    for i in range(0,250):
        print("Current Dict is: ", phone_book)
#update phone number
        if name and number not in phone_book:
            name=input()
            if (name=='nobody'):         
                break                
            number=input()
            phone_book.update({name:number}) 
print("YOUR PHONE BOOK ",phone_book)
print("Do you want to update?(Y/S)")
update_condition=str(input())
if(update_condition=="Y" or "y"):
    nam=str(input("TYPE THE NAME OF THE CONTACT TO BE UPDATED"))
    del phone_book[nam]       
    print("CONTACT TO BE UPDATED")
    name_updated=str(input("***NAME TO BE UPDATED*** :"))
    number_updated=int(input("***NUMBER TO BE UPDATED*** :"))
    phone_book.update({name_updated:number_updated})
    sorted_phone_book= sorted(phone_book.items(), key=lambda x: x[0])

    print("YOUR PHONE BOOK CONTACTS AFTER UPDATE :",sorted_phone_book)
