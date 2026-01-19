from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("", tlsAllowInvalidCertificates=True)



print(client)

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)


def add_video(name,time):
    video_collection.insert_one({"name": name , "time":time})

def list_videos():
    for vid in video_collection.find():
        print(f"ID: {vid['_id']}, Name: {vid['name']} and Time: {vid['time']}")



def update_video(video_id , name , time):
    video_collection.update_one({'_id': ObjectId(video_id)},{"$set": {"name" : new_name , "time":new_time}})


def delete_video(video_id):
    video_collection.delete_one({"_id": video_id})

# TODO  : debug this video_id problem

def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add a Videos")
        print("3. Update a videos")
        print("4. Delete a videos")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time:  ")
            add_video(name , time)
        elif choice == '3':
            video_id = input("Enter a video id to update: ")
            name = input("Enter a video name: ")
            time = input("Enter a video time: ")
            update_video(video_id , name , time)
        elif choice == '4':
            video_id = input("Enter a video id to delete: ")

            delete_video(video_id , name , time)
        elif choice == '5':
            print("Exit the app")
            break
        else:
            print("Invalid choice: ")


if __name__ == "__main__":
    main()


