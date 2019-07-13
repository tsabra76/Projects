'''DOWNLOAD JSON AND CONVERT TO CSV LOCALLY'''

# URLLIB.REQUEST, JSON, AND CSV MODULES REQUIRED
import urllib.request, json, csv 

with urllib.request.urlopen("https://jsonplaceholder.typicode.com/photos") as url:

# ENSURE JSON IS UTF-8
    data = json.loads(url.read().decode())

# WRITE HEADER ROW
with open('file.csv', 'w') as f:
    JsonToCSV = csv.writer(f)
    JsonToCSV.writerow(["Album id", "id", "title", "URL", "ThumbnailURL"])

# LOOP THROUGH ALL ROWS
    for item in data:
        JsonToCSV.writerow([item["albumId"],
        item["id"],
        item["title"],
        item["url"],
        item["thumbnailUrl"]])
f.close()