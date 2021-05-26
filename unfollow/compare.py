followers = []
following = []
bir = open("followers.txt","r")

for i in bir:
    followers.append(i)
iki = open("following.txt","r")
for k in iki:
    following.append(k)

not_following_back = [user for user in following if user not in followers]
not_following_back.sort()
with open("results.txt","w",encoding = "UTF-8") as file:
    for i in not_following_back:
        file.write(i)




