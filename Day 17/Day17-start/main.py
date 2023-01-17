class User:
    def __init__(self,user_id,username):
        self.user_id=user_id
        self.username=username
        self.followers=0
        self.following=0
    def follow(self,user):
        user.followers+=1
        self.following+=1
        # print("new user has been created")


user_1=User("001","pratik")
# user_1.name="pratik"
# user_1.id="001"
user_2=User("002","kartik")
user_1.follow(user_2)
print(user_2.followers)