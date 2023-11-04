import pyshorteners
long_url = input("Enter the URL to Short it: ")
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

print("The Shortned URL is: " + short_url)

import pyshorteners
long_url = input("Enter thr Url to Shorten: ")

#Tinyusrl shortner service
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

print("The Shorten URL is: " + short_url)
type_bitly = pyshorteners.Shortener(api_key='11df033412cb74eb8ff5c1982b96c92c42ab')
short_url = type_bitly.bitely.short("https://www.google.com")
import pyshorteners
long_url = input("Enter the URL to Shorten: ")

#Bitly Shortener service
type_bitly = pyshorteners.Shortener(api_key='01b6c587cskek4kdfijsjce4cf27ce2')
short_url = type_bitly.bitly.short("htts://www.google.com")
print("The Shorten URL is:" + short_url)    #gives the url in expand or original from

expand_url = type_bitly.bitly.expand('https://bit.ly/TEST')
print(expand_url)  #gives the url in expand original from
count = type_bitly.bitly.total_clicks("https://bit.ly/TEST")
import pyshorteners
s = pyshorteners.Shortener()
#Chilp.it
s.chilpit.short('http://www.google.com') #gives output --> 'http://chilp.it/TEST'
s.chilpit.expand('http://chilp.it/TEST')

#Adf.ly
s=pyshorteners.Shortener(api_key='YOU_KEY',user_id='USER_ID',domain='test.us',group_id=12,type='int' )
s.adfly.short('http://www.google.com')   #gives output
