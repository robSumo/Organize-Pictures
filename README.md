#Organize Pictures and Videos

##Summary
This is a small Python utility script that I have been using to organize my smart phone pictures and videos with. It does the following:

1. Takes the pictures from a specified folder and puts them into another. The destination of these files will be in a folder with the format “year”/”year_month”. For example, if you specified “pictures” as the destination directory, you would have folders that looked something like: pictures/2012/2012_02, pictures/2012/2012_03, etc…
2. Takes the videos from the specified folder and puts them into another. Similar to the point above.
3. This script will also not move the file if it is already in the destination folder. 
4. This script will output move report. Listing files that were moved and files that were not moved.

##Configuration:
Specify the following inside the config.properties file:

1. The root directory of the origin folder. This is the folder where you have the pictures and/or videos in them. The script will recursively iterate all the way down all of the folders.
2. The destination folder for the pictures.
3. The destination folder for the videos.

##Run
python organizePictures.py
