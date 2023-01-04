import tweepy
import datetime

#Calculo cuanto paso desde que messi levanto la copa
fecha_final = datetime.date(2022,12,18)
fecha_actual = datetime.date.today()
contador_dias = fecha_actual - fecha_final

#Datos necesarios de la cuenta developer de twitter para poder utilizar la API - https://developer.twitter.com/en/portal/dashboard
api_key = ""
api_key_secret =  ""
access_token= ""
access_token_secret = ""

#Autentico la api para poder acceder a la cuenta y hacer el tweet
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Condicional dependiendo si se cumplio o no un año desde la final
if contador_dias.days < 365:   
    api.update_status("Pasaron {} desde que Lionel Messi levantó la copa".format(contador_dias.days))
elif contador_dias.days == 365:
    api.update_status("Pasó un año desde que Lionel Messi levantó la copa y Argentina ganó el mundial :)")


    

