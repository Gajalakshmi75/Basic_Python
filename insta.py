import requests
from bs4 import BeautifulSoup
import instaloader
URL="https://www.instagram.com/{}/"
def parse_data(s):
    data={}
    s=s.split("-")[0]
    s=s.split(" ")
    data["Followers"]=s[0]
    data["Following"]=s[2]
    data["Posts"]=s[4]
    return data

def scrape_data(username):
    r=requests.get(URL.format(username))
    s=BeautifulSoup(r.text,"html.parser")
    meta=s.find("meta",property="or:description")
    return  parse_data(meta.attrs['content'])

if __name__=="_main_":
    print(30*"=","Instagram",30*"=")
    username=input("Enter the ID:")
    data=scrape_data(username)
    print()
    print(username,"having",data["Followers"],"followers")
    print(username,"having",data["Following"],"following")
    print(username,"having",data["Posts"],"posts")
    print(65*"=")
    lakshmi=instaloader.Instaloader()
    lakshmi.download_profile(username,profile_pic_only=True)
