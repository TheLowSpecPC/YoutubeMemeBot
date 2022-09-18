import praw
import requests, sys
import config,os
from RedDownloader import RedDownloader

reddit = praw.Reddit(
    client_id= config.client_id,
    client_secret= config.client_secret,
    user_agent= config.user_agent,
    username= config.username
)

def links():
    x=1
    no = 0
    sub = config.subreddit
    # Clearing the folder
    for i in os.listdir("Bot\\Reddit"):
        try:
            os.remove("Bot\\Reddit\\" + i)
        except:
            continue
    # Grabbing links
    for s in sub:
        no += round(config.limit/len(sub))
        no1 = no+1
        try:
            for submission in reddit.subreddit(s).new(limit=None): #can use hot,top,new,rising
                if os.path.exists("Bot\\Reddit\\Output "+"%04i" %no+".mp4") or os.path.exists("Bot\\Reddit\\Output "+"%04i" %no1+".mp4")==True:
                    break
                else:
                    if (submission.over_18==False and submission.is_video==True):
                        urls = submission.url
                        link = requests.get(urls).url
                        RedDownloader.Download(url = link,
                                                   output="Bot\\Reddit\\Output %04i" %x,
                                                   quality = 1080)
                        x+=1
                        print(link)
                    else:
                        print("NSFW or Image")
        except:
            print("Enter Proper Details in Config")
            sys.exit(1)
        if s == sub[-1]:
            break

    return "Finished Downloading video"
links()