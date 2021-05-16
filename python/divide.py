import glob, os
import argparse

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parser = argparse.ArgumentParser(description = "Add keyword for making dir for training and testing datasets")
parser.add_argument("--keyword", help = "string to save path in ", type = str, dest = 'keyword')
parser.add_argument("--path", help = "Path to dataset", type = str, dest = 'path')

args = parser.parse_args()	

current_dir = args.path
g_colab_full_path='/content/darknet/data/' + args.keyword

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open(args.keyword + '-train.txt', 'w')  
file_test = open(args.keyword + '-test.txt', 'w')# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write(g_colab_full_path + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(g_colab_full_path + "/" + title + '.jpg' + "\n")
        counter = counter + 1
