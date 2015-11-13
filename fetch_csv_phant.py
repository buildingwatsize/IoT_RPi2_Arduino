import urllib.request
import csv

base_url = 'http://192.168.253.38:8080'
url = base_url + '/output/8X4kXblp1ETpE26WN3EbUdr1WY1.csv'
file_name = 'feed_phant.csv'

r = urllib.request.urlretrieve(url, file_name)

print("Saved as "+file_name+"\n")

print("__Show Entry__")
with open(file_name, newline='') as csvfile:
    Reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in Reader:
        print (', '.join(row))

