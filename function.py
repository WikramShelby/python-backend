def login_user(username,password):
    if not username:
        raise ValueError("username is required")
    
    if len(password)<= 6:
        raise ValueError("password must have more than 6 characters")
    
    return{
        "username":username,
        "message":"login successful"
    }

try:
    user = login_user("vamsi","vamsi1818")
    print(user)
except ValueError as e:
    print("user login un-successful",e)