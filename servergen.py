import requests
import json

#API_KEY = "SWJMM21eiODiYwV47gwiBMl302kIy2"
#EMAIL = "minnkyawkyaw91@gmail.com"
#SERVER_ID = 920846
#APP_ID = 3196496
BASE_URL = "https://api.cloudways.com/api/v1/oauth/access_token"
#USERNAME = 'leelopallozcvx'
#PASSWORD =  'Leelopalloz@123'

def access_token(API_KEY,EMAIL,BASE_URL):
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',}
    data = [
    ('email', EMAIL),
    ('api_key', API_KEY),]
    token = requests.post('https://api.cloudways.com/api/v1/oauth/access_token', headers=headers, data=data)
    value = json.loads(token.text).get('access_token')
    return (value)



def genserver(SERVER_ID,APP_ID,API_KEY,EMAIL,USERNAME,PASSWORD,DESCRIP,IPADD):
    try:
        token =  access_token(API_KEY,EMAIL,BASE_URL)
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'Authorization': 'Bearer '+token+'',
        }
        data = [
        ('server_id', SERVER_ID),
        ('app_id', APP_ID),
        ('username', USERNAME),
        ('password', PASSWORD),]

        req = requests.post('https://api.cloudways.com/api/v1/app/creds', headers=headers, data=data)
        value = json.loads(req.text).get('status')
        Error = str(json.loads(req.text))
        if str(value) == 'True':
            msg = f"you account is successfully created\nUsername:{USERNAME}\nPassword:{PASSWORD}\nIP:{IPADD} Port:22\n{DESCRIP}"
        
        else:
                msg = f"We do not allow to create multiple accounts on our provider's server. You can try this again to get from other server providers.\nPlease contact us @binbeginners \nERROR : {Error}"
        return msg

       
    except:
        return ("SERVER IS DOWN and We are updating soon.Sorry for inconvient")


