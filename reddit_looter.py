import praw
import requests, sys
import config,os
from RedDownloader import RedDownloader
cwd = os.getcwd()

reddit = praw.Reddit(
    client_id= config.client_id,
    client_secret= config.client_secret,
    user_agent= config.user_agent,
    username= config.username
)

def links():
    x = 0
    no = 0
    sub = config.subreddit
    # Clearing the folder
    for i in os.listdir(cwd+"/Bot/Reddit"):
        try:
            os.remove(cwd+"/Bot/Reddit/" + i)
        except:
            continue
    # Grabbing links
    for s in sub:
        no += round(config.limit/len(sub))
        try:
            for submission in reddit.subreddit(s).new(limit=None): #can use hot,top,new,rising
                if x>=no:
                    break
                else:
                    if (submission.over_18==False and submission.is_video==True):
                        urls = submission.url
                        link = requests.get(urls).url
                        x+=1
                        RedDownloader.Download(url = link,
                                                   output=cwd+"/Bot/Reddit/Output %04i" %x,
                                                   quality = 1080)
                        print(link)
                    else:
                        print("NSFW or Image")
        except:
            print("Enter Proper Details in Config")
            sys.exit(1)
        if s == sub[-1]:
            break

    return "Finished Downloading video"