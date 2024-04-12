#! TeamElite 1.6k Special Gift ❤️❤️
#! 100% Working Temporary mails

import requests,json,time,os,sys

line="—"*34
def main():
    os.system("clear")
    h=requests.get("https://internxt.com/api/temp-mail/create-email").json()
    print("Email : "+h["address"])
    print(line)
    print(" Waiting for Your Received Mail")
    print(line)
    while True:
        try:
            g=requests.get("https://internxt.com/api/temp-mail/get-inbox?token="+h["token"]).json()["emails"]
        except:
            pass
        if "[]" in str(g):
            continue
        else:
            sub=g[0].get("subject")
            print("Received Mail : "+sub)
            print(line)
            break
        time.sleep(1)
    More=input(" Do You Want More Mails [Y/n] ")
    if "y" == More.lower():
        main()
    else:
        sys.exit()


if __name__ =="__main__":
    main()



