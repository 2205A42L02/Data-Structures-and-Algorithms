def authenticate():
    password="Meghana123"
    attempts=3
    
    while attempts>0:
        user_input=input("Enter the password:")
        
        if user_input==password:
            print("Welcome!")
            break
        else:
            attempts-=1
            if attempts>0:
                print(f"Wrong password! You have {attempts} attempts left.")
            else:
                print("Account blocked.")
                break
authenticate()