def login(username, password):
    if len(password) <6:
        print("Passsword too short")
    elif username =="admin" and password =="admin123":
        print("login done")
    else:
        print("invalid")