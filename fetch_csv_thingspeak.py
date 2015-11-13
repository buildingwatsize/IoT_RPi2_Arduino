import urllib.request
import csv

base_url = 'http://192.168.253.38:3000'
url = base_url + '/channels/1/feed.csv'
file_name = 'feed_thingspeak.csv'

r = urllib.request.urlretrieve(url, file_name)

print("Saved as "+file_name+"\n")

print("__Show Entry__")
with open(file_name, newline='') as csvfile:
    Reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in Reader:
        print (', '.join(row))
