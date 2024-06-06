todo_list=[]
def add():
    item=input("enter task to be added:")
    todo_list.append(item)
    print(f"{todo_list,"has been added to the list"}")
def view():
    if not todo_list:
        print("list is empty")
    else:
        for i,item in enumerate (todo_list, start=1):
            print(f"{i}.{item}")  
     
def delete():
     view()
     try:
         index=int(input("enter the number of items to remove"))-1
         if 0<=index<len(todo_list):
             removed=todo_list.pop(index)
             print(" deleted")
         else:
             print("invalid index")
     except:ValueError
     print("please enter valid number")
     
def main_menu():
    while True:
        print("\nTO DO LIST:")
        print("1.add")
        print("2.view")
        print("3.delete")
        print("4.exit")

        choice=int(input("Choose option:"))
        if choice==1:
            add()
        elif choice==2:
            view()
        elif choice==3:
            delete()
        elif choice==4:
            break
        else:
            print("invalid input:")
main_menu()
