from instagrapi import Client
import os
import http.client, urllib
import pickle

account = ""
password = ""

dbfile = open('followers.pkl', 'rb')

try:
  followers = pickle.load(dbfile)
except EOFError:
   followers = set()

try:
    following = pickle.load(dbfile)  
except EOFError:
    following = set()   



cl = Client()

cl.load_settings('dump.json')
cl.login(account, password)


# print("Target: " + str(cl.user_info_by_username_v1('hulyarein').model_dump()))

followings = cl.user_following("2715101859")
followers = cl.user_followers("2715101859")
# print(followers)

print("Target: _wewedemeyer")
print("Followers: \n")

for user_id, user_short in followers.items():
    followers.add(user_id)
    print("Fullname: " + user_short.full_name + " Username: " + user_short.username)


print("Following: \n")

for user_id, user_short in followings.items():
    following.add(user_id)
    print("Fullname: " + user_short.full_name + " Username: " + user_short.username)

# conn = http.client.HTTPSConnection("api.pushover.net:443")
# conn.request("POST", "/1/messages.json",
#     urllib.parse.urlencode({
#     "title": "NEW FOLLOWER ON TARGET!",
#     "token": "af1i44abb2zreyxm7suxp9bq74u9hw",
#     "user": "ufd51y9n28co3dkaqrifiad9ko9xdp",
#     "message": ",
#     }), { "Content-type": "application/x-www-form-urlencoded" })
# conn.getresponse()


# print("\nDone!")
cl.dump_settings('dump.json')
