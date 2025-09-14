class StarCookie:
    pass


star_cookie1 = StarCookie()
star_cookie1.weight = 19  # type: ignore
star_cookie1.color = "Red"
print(star_cookie1.weight)
print(star_cookie1.color)
star_cookie2 = StarCookie()
star_cookie2.weight = 14
star_cookie2.color = "green"
print(star_cookie2.weight)
print(star_cookie2.color)

# insted of doing one by one objects intialized(it is time wasting) ..... we use intializer or constructor to do in easy way

#       class StarCookie:
#             def __init__(self):
#                   (initialize attributes)
