
staff_file_path="Data/manage_staff.txt"
def manage_staff():
   print("-"*77)
   print('+-'*12 + "WELCOME TO OUR STAFF MANAGE PAGE" + '+-'*12)
   print("-"*77)
   print( "1. Add staff"  )
   print( "2. Edit staff" )
   print( "3. Delete staff")
   print( "4. Back to role of Admin")

   while True:
      choice=input( "Enter your choice (EX:1,2,3): ")
      #adding staff
      if choice=="1":
         f=open(staff_file_path,"a+")
         add=input( "Enter the name of staff: ").lower()
         f.write("\n" + add) #adding staff to next line
         print("successfully added" )
        
      elif choice=="2":
         #editing staff
         f=open(staff_file_path,"w+")
         add=input("Enter the name of staff: ").lower()
         f.write(add)
         print("successfully edited")

         #manage_staff()
      elif choice=="3":
         f=open(staff_file_path,"r+")
         name=f.readlines()
         add=input("Enter the name of staff you want to delete: ").lower()
         for line in name:
            if add in line:
               del line
               print("successfully deleted" )
               #manage_staff()
            else:
               print("Name is not in list...!!" )
               #manage_staff()
         
      elif choice=="4":
         from Menu_file.admin_menu import admin_menu
         admin_menu()


      else:
         manage_staff()


      
         
    
