from instabot import Bot
import os
import shutil, glob, time

from instabot.bot.state.bot_state import BotState


def create_dir():
	cd = os.getcwd()
	images = cd + "/images/"
	upload = cd + "/images/upload"
	after = cd + "/images/after-upload"
	if os.path.exists(images) == False:
		os.mkdir(images)
		os.mkdir(upload)
		os.mkdir(after)






def clean_up():
    dir = "config"
    remove_me = "imgs\img.jpg.REMOVE_ME"
    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(remove_me):
        src = os.path.realpath("imgs\img.jpg")
        os.rename(remove_me, src)


def upload_post():
	source = os.getcwd() + "/images/upload/"
	dest = os.getcwd() + "/images/after-upload/"


	bot = Bot()
	bot.login(username="your_username", password="your_password")
	
	file_ext = ['.jpeg','.jpg','.png']
	for ext in file_ext:
		if glob.glob(source + f"*{ext}"):
			images = glob.glob(source + f"*{ext}", recursive=False)
	

	for i in images:
		caption_i = i.split(sep="/")[-1].split(sep=".")[0:-1]
		print(caption_i)
		captions = ''.join(caption_i)
		print(captions)
		if len(images)>1:
			time.sleep(60)
		bot.upload_photo(i, caption=captions)
		
	for j in os.listdir(source):
		shutil.move(f"images/upload/{j}",dest + j)

	bot.logout()



if __name__ == '__main__':
	create_dir()
	path = os.getcwd() + "/images/upload/"
	
	while True:
		vf = glob.glob(path + "*")
		if vf != []:
			print("file found :")
			clean_up()
			upload_post()

			#set your gap duration here in seconds
			time.sleep(5)