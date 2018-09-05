import facebook
import requests
import re

ACCESS_TOKEN="EAAFxSZCHMvkEBAJ9D6KAYpkOELNZBfzxweLZAgAfoI0yYDrNeEVoU2pbXnvEydjgmVI915JmDqgyWR8uk98EWifYZAeZB7zX8mVkFmLYmjT9dCuVA1bIUcmpMCckew7eE7VeDZBlUQgZAbwctZCwur8QxmvLnynGZAPZAdrjDN4Ske2AZDZD"
user_token="231239qdqee0ri0rer0q0eriq0ke-w"
access_token=ACCESS_TOKEN
page_access_token="EAAFxSZCHMvkEBAJ9D6KAYpkOELNZBfzxweLZAgAfoI0yYDrNeEVoU2pbXnvEydjgmVI915JmDqgyWR8uk98EWifYZAeZB7zX8mVkFmLYmjT9dCuVA1bIUcmpMCckew7eE7VeDZBlUQgZAbwctZCwur8QxmvLnynGZAPZAdrjDN4Ske2AZDZD"
page_token = page_access_token
user1="thenexpresstt"



graph=facebook.GraphAPI(access_token=page_token, version='2.7')
profile=graph.get_object(user1)
posts=graph.get_connections(id=user1,connection_name ='posts', fields='comments', limit=100)


for i, j in posts.items():
    for items in j:
        thelist=(items)
        otherlist=thelist.get('comments')
        if not otherlist:
         continue
        for l,m in otherlist.items():
                for p in m:
                    try:
                     if p.get('message'):
                         split = re.sub(r"[^a-zA-Z0-9\s]",' ',p.get('message')).lower().split()
                         replies = {"abcde": "hello to you too!"}
                         for item in split:
                             if item in replies:
                                response = p.get('id')
                                idfile=open("comment_ids.txt","r")
                                if response not in idfile:
                                    idfile1=open("comment_ids.txt","a")
                                    idfile1.write("\n" + response)
                                    graph.put_comment(object_id=response, message=replies.values())
                                    idfile1.readlines()
                                    idfile1.close()
                                    print(q)
                                else:
                                    print("hello")

                    except AttributeError:
                        continue
