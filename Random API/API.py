from randomuser import RandomUser
import pandas as pd

#RandomUser object
r=RandomUser()

#Generate 10 random users
some_list=r.generate_users(10)
#print(some_list)

name=r.get_full_name()
for user in some_list:
    print(f'{user.get_full_name()}, {user.get_email()}')

#Pictures
for user in some_list:
    print(f'{user.get_full_name} {user.get_picture()}')

# Generate a table with name, gender, city parameters inside
def get_users():
    users=[]
    for user in some_list:
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
    return pd.DataFrame(users)

df1=pd.DataFrame(get_users())
#print(df1)

# Fruitvice API
import requests
import json

data = requests.get("https://www.fruityvice.com/api/fruit/all")
#print(data)
results=json.loads(data.text)
#convert json to dataframe
pd.DataFrame(results)

#Normalizing
df2=pd.json_normalize(results)

cherry=df2.loc[df2["name"]=='Cherry']
print(cherry.iloc[0]['family'])
print(cherry.iloc[0]['genus'])

#calories in a banana
cal_banana=df2.loc[df2["name"]=='Banana']
print(cal_banana.iloc[0]['nutritions.calories'])

#another url
data2 = requests.get("https://www.fishwatch.gov/api/species")
results=json.loads(data2.text)
df3=pd.DataFrame(results)