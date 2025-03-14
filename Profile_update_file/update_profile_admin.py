update_profile_path="Data/update_profile.txt"
def update_profile():
    print("-"*77)
    print('+-'*12 + "WELCOME TO PROFILE UPDATE PAGE" + '+-'*12)
    print("-"*77)
    print("1. View profile")
    print("2. Update profile details")
    print()
    while True:
      choice=input("Enter your choice: ")
      if choice=='1':
          view_profile()
      elif choice=='2':
          update_details()
      else:
          print(f"Invalid choice!!..{choice}")
def view_profile():
    f=open(update_profile_path,"r")
    lines=f.readlines()
    if len(lines)==3:
        return{
            'name':lines[0].strip(),
            'email':lines[1].strip(),
            'age':lines[2].strip()

        }
    return{'name':'','Email':'','Age':0}


def update_details():
    profile=view_profile()
    print("Update your profile")
    profile['name']=input(f"Enter name[{profile['name']}]:")
    profile['email']=input(f"Enter age[{profile['email']}]:")
    profile['age']=input(f"Enter email[{profile['age']}]:")
    print("successfully updated your data...")
    save_data()
    
def save_data():
    profile=view_profile()
    file=open(update_profile_path,"w")
    file.write(f"{profile['name']}\n")
    file.write(f"{profile['email']}\n")
    file.write(f"{profile['age']}\n")


    