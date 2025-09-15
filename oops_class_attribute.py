class StarCookie:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
        pass


star_cookie1 = StarCookie("Red", 16)
print(star_cookie1.color)
print(star_cookie1.weight)
star_cookie2 = StarCookie("green", 20)
print(star_cookie2.weight)
print(star_cookie2.color)

# insted of doing one by one objects intialized(it is time wasting) ..... we use intializer or constructor to do in easy way

#       class StarCookie:
#             def __init__(self):
#                   (initialize attributes)

# now set attribute in initializer [to set attributes in every objects]
#          class StarCookie:
#               def __init__(self,color):
#                       self.color = color

# example 2


class youtube:
    def __init__(self, username, subscribers=0):
        self.username = username
        self.subscribers = subscribers


user1 = youtube("abhishek")
print(user1.username)
print(user1.subscribers)

user2 = youtube("rahul")
user2.subscribers = 5
print(user2.username)
print(user2.subscribers)
