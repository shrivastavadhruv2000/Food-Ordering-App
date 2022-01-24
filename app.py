class Admin:
    def login(self):
        id=input("enter your id ")
        password=input('enter password ')
        return ''
    def AdminData(self):
        list_food=['meggi','machurian']
        food_id = 0
        dict1={'name':'meggi','quantity':'100gm','stock':10}
        name = input("enter food name  ")
        quantity=input("enter quantity  ")
        stock=int(input('enter stock   '))
        price = int(input('enter price'))
        discount =int(input('enter discount'))
        list_food.append(name)
        food_id= food_id+1
        dict1={'food id ':food_id,'name':name,'quantity':quantity,'stock':stock}
        print(list_food)
        print(dict1)
        return  'succesfully added'
obj=Admin()
print(obj.login())
print(obj.AdminData())
# print(obj.AdminData())
    


