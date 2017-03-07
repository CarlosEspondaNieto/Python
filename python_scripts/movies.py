# First import urllib for downloading and uncompress the file
import urllib.request
import zipfile
import os
import pandas as pd

# This is the URL for  the public data
url = "http://files.grouplens.org/datasets/movielens/ml-latest-small.zip"

# This is the working directory
working_dir = "../data/movies/"

# Destination filename
file_name =  working_dir +  "movies.zip"

# Download the file from `url` and save it locally under `file_name`:
if os.path.isfile(file_name):
	print('Data is already downloaded')
else:
	print("Downloading file")
	urllib.request.urlretrieve(url, file_name)

# We already know the expected files so:
expected_files = ['links.csv', 'movies.csv', 'ratings.csv', 'README.txt', 'tags.csv']

# There's an extra dir level in thwe extracted files
inner_dir = "ml-latest-small/"
# I want to know the names of the extracted files
file_names = os.listdir(working_dir + inner_dir)

if file_names == expected_files:
	print("You already have the data files, check it!")
else:
	# This is the code for uncompress hte zipfile
	path_to_zip_file =  working_dir + "movies.zip"
	# Reference to zipfile
	zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
	print("Extracting files")
	zip_ref.extractall(working_dir)
	# Is important to use .close()
	zip_ref.close()

# Reading the files needed for this analysis
movies = pd.read_csv(
	working_dir +
	inner_dir +
	expected_files[1],
	sep = ',')
ratings = pd.read_csv(
	working_dir +
	inner_dir +
	expected_files[2],
	sep = ',')

## Let's print the first lines of each dataframe
print(movies.head())
print(ratings.head())
