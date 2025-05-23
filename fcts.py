

def download_set_youtube(l):
    '''Downloads multiple youtube videos '''
    l=list(set(l))
    for i in l:
        download_youtube(i)

def download_youtube(url):
    '''Download one single youtube video'''
    from pytubefix import YouTube
    from pytubefix.cli import on_progress
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"Téléchargement de : {yt.title}")
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path="C:\\Users\\arban\\Downloads")

# def download_youtube(link,pathh="C:\\Users\\arban\\Downloads"):
#     '''downloads one youtube video'''
#     from pytube import YouTube
#     import os
#     # where to save
#     #pathh="C:\\Users\\Oussama\\Downloads"
#     # link of the video to be downloaded
#     try:
#         # object creation using YouTube
#         # which was imported in the beginning
#         yt = YouTube(link)
#     except:
#         print("Connection Error") #to handle exception
#     signes_interdits='\\:*/?"<>|'
#     name=yt.title
#     for i in signes_interdits:
#         name=name.replace(i,'')
#     print("Start downloading...")
#     pathh="C:\\Users\\arban\\Downloads"
#     yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[0].download(output_path=pathh,filename=name+'.mp4')
#     print("Download finished")
#     print("Video "+name+" successfully downloaded")

def fetch():
    '''find a working proxy'''
    import instaloader as i
    import requests
    import numpy as np
    r=requests.get("https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=protocolipport&format=text")
    r_text=r.text
    r_text.split('r')
    http=r_text.split('\r\n')
    http=[http[i].replace('socks4','http') for i in range(len(http))]
    http=[http[i].replace('socks5','http') for i in range(len(http))]
    http=[http[i].replace('http://','') for i in range(len(http))]
    session = requests.Session()
    j=0
    print("Search for a proxy")
    while j<len(http):
        try:
            login = session.post('https://www.instagram.com/accounts/login/ajax/',data={'enc_password': "Spiderman-123", 'username': "plaisirplaisir95"},allow_redirects=True,proxies={'https':http[j],'http':http[j]},timeout=2)
            print(http[j]+" is working")
            #login=requests.get(url,proxies={'https':http[j],'http':http[j]},timeout=2,stream=True) #proxies={https,http}
            #print(http[j]+" is working")
            break
        except:
            print(j)
            pass
        j=j+1
    return login


def download_photo(nom):
    '''download pictures and videos of an instagram account only by giving the nickname of the account'''
    import time
    import instaloader as i
    import os
    import Oussama.fcts as fct
    os.chdir(r"C:\Users\arban")
    loader = i.Instaloader(download_pictures=True, download_videos=True, download_video_thumbnails=True, download_geotags=False, download_comments=False,compress_json=False,save_metadata=False,check_resume_bbd=False)
    loader.load_session_from_file("loginpla")
    profile=i.Profile.from_username(loader.context,nom)
    c=0
    for j in profile.get_posts():
        try:
            loader.download_post(j,nom)
        except KeyError:
            pass
        except:
            fct.fetch()
            loader.download_post(j,nom)
        c=c+1
        print(c)
    os.chdir(r"C:\Users\arban")


def complete_insta_profile(nom):
    '''Donwloads the rest of photos and videos of an account
    that has already been downloaded'''
    import instaloader as i
    import os
    import pandas as pd
    from datetime import date, datetime
    from itertools import dropwhile, takewhile
    os.chdir(r"C:\Users\Oussama\Instagram")
    loader = i.Instaloader(download_pictures=True, download_videos=True, download_video_thumbnails=True, download_geotags=False, download_comments=False,compress_json=False,save_metadata=False,check_resume_bbd=False)
    fetch()
    profile=i.Profile.from_username(loader.context,nom)
    c=0
    lis=os.listdir("C:\\Users\\Oussama\\Instagram\\"+nom)
    lis=[i for i in lis if (("_" in i) and ("jpg" in i))]
    lis=[i[:i.index("_")] for i in lis]
    col_date = pd.to_datetime(lis)
    df = pd.DataFrame({"A":range(len(lis)), "my_date":col_date})
    recent_date=df["my_date"].max()
    eldest_date=df["my_date"].min()
    todayy=date.today()
    Until=datetime(todayy.year,todayy.month,todayy.day+1)
    Since=datetime(recent_date.year,recent_date.month,recent_date.day-1)
    posts = profile.get_posts()
    for j in takewhile(lambda x: x.date>Since , dropwhile(lambda x: x.date > Until, posts)):
        try:
            loader.download_post(j,nom)
        except KeyError:
            pass
        except:
            print("1")
            fetch()
            loader.download_post(j,nom)
    os.chdir(r"C:\Users\Oussama")

def size_url(url):
    """display the size of an image by knowing its url"""
    #should install Pillow before importing PIL
    from PIL import Image
    from io import BytesIO
    import requests
    from bs4 import BeautifulSoup
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    img=Image.open(BytesIO(r.content))
    return(img.size)


def download_twitter(url):
    "download a twitter video"
    import yt_dlp
    ydl_opts = {
        'outtmpl': r'C:\Users\arban\video_twitter.%(ext)s'  # nom du fichier de sortie
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])





