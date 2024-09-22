import os
import shutil
import datetime
import schedule
import time


def get_valid_path(prompt):
    while True:
        path = input(prompt).strip()
        if os.path.isdir(path):
            return path
        else:
            print("Invalid path. Please enter a valid directory path.")  #if the path format is invalid for that reason ... And also run the loop again...

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    Welcome to automatic folder backup   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #To make it beautifil


print("This program will automatically back up your specified folder every day at 'time'.")
print("Please make sure that : ")

print(f"1. The source folder exists.")

print(f"2. You have write permissions in the destination folder.")

print(f"3. You have entered a valid time (e.g. '15:42').")

print(f"4. The destination folder does  exist.")

print ("To continue press enter...")
print("To Exit press 'Ctrl+c' ...")
input()



source_dir = get_valid_path(r"Enter the path of the folder you want to back up: ")
destination_dir = get_valid_path(r"Enter the path where you want to keep the backup files: ")

print("Your back up is started...")

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Backup completed successfully at : {dest_dir}")
    except FileExistsError :
        print(f"Backup failed: Destination directory already exists at : {dest_dir}")

schedule.every().day.at("15:42").do(copy_folder_to_directory, source_dir, destination_dir) #everyday shedule to back up the folder

while True:
    schedule.run_pending()
    time.sleep(1)