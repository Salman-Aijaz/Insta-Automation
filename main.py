from instabot import Bot
from dotenv import load_dotenv
import os

load_dotenv()
bot=Bot()

username =os.getenv('INSTAGRAM_USERNAME')
password=os.getenv('INSTAGRAM_PASSWORD')

# print(f"username:{username}")
# print(f"password:{password}")

bot.login(username=username,password=password)

# bot.follow('icc')

# UPLOADING AN IMAGE
# bot.upload_photo("C:/Users/ghn/Downloads/2",caption="Routing in Next JS")1

# UNFOLLOW THE PEOPLE 
# bot.unfollow(user_id="icc")

# SENDING MESSAGE 
# bot.send_message("Hi Thanks for following me",user_ids=["sk27_photography","zaeem_altaf"])

# CHECK ALL FOLLOWER USING BOT 
# followers=bot.get_user_followers("tech.sk27")
# for follower in followers:
#     print(bot.get_user_info(follower))
    # time.sleep(10)

# CHECK ALL FOLLOWING USING BOT
followings=bot.get_user_following("tech.sk27")
for following in followings:
    print(bot.get_user_info(following))