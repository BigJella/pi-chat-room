users = [
    {username:"Gustavo"; password: "Gustavo"},
    {username:"Amani"; password: "Amani"},
    {username:"Muhammad"; password: "Muhammad"},
    {username:"Andres"; password: "Andres"},
    {username:"Lucas"; password: "Lucas"},
    {username:"Cole"; password: "Cole"},
    {username:"Yusuf"; password: "Yusuf"},
    {username:"Bilal"; password: "Bilal"}
]

def authenticate(username, password):
    for user in users:
        if user.username == username and user.password == password:
            return True
    return False