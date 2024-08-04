import sys
import boto3

# Input section
album_cover = sys.argv[1]
name_of_album = input("Enter the album name: ")
name_of_artist = input("Enter the name of the artist: ")
comments = input("Please enter your thoughts on the album: ")
rating = input("Please enter the rating of the album out of 10: ")


db = boto3.resource('dynamodb')
table = db.Table('mickeys-marvels')
result = table.scan()['Items']

# Setting a value that is impossible for the entry ID to ensure this will contain the maximum value
max_entry = -1

for item in result:
    if item['entryID'] > max_entry:
        max_entry = item['entryID']

max_entry += 1

try:
    table.put_item(
        Item={
            'entryID': max_entry,
            'albumCover': album_cover,
            'albumName': name_of_album,
            'artist': name_of_artist,
            'comments': comments,
            'rating': rating,
        }
    )
except Exception:
    print("Something went wrong!")
    sys.exit(-1)

print("Review has been submitted to the table successfully! ")
sys.exit(0)