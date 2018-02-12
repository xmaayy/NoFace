'''
# This file is called DirProc to indicate it being used for directory and
# process management through os and subprocess.
# This sets up the folders needed (frames) and will do all the image
# extraction from videos.
# It will also fetch all video and picture files from a given directory.
'''

from FaceExtraction import get_faces
import subprocess
import sys
import os


'''
# Run FFMPEG on a given file, this ouputs all its frames to jpg files
# for later use in facial extration
'''
def run_ff(dir_path, file_path):    
    command = [r'.\res\ffmpeg ', r'-i', file_path , r'-qscale:v ', r'2', dir_path + r'\faces\out-%03d.jpg']

    #Used for debugging
    #print ('About to execute command: ')
    #print (command)

    #Create the FFMPEG process, unfortunately it creates its own little window
    #and wont update me on its progress during the extraction
    proc = subprocess.Popen(command,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE)
    
    #This is just so we wait until after its done executing
    #just throwing away all that string data :(
    while proc.poll() is None:        
        proc.communicate()

    #I dont really know if anything can be done with these because
    #damn ffmpeg pipes all its output INTO STDERR FOR SOME REASON
    stout, sterr = proc.communicate();
    print stout
    print sterr

def verify_paths(dir_path):

    #Make sure what they gave us exists
    #Normally you could just make it but we want files in there
    if not os.path.exists(dir_path):
        print('Path does not exist, exiting...')
        return 0;

    #If what they gave us exists and has no frames folder,
    #set up frames folder
    if not os.path.exists(dir_path + r'\faces'):
        os.makedirs(dir_path + r'\faces')
    return 1;

def yn_prompt():
    yes = {'yes','y', 'ye'}
    no = {'no','n'}

    choice = raw_input().lower()
    if choice in yes:
       return True
    elif choice in no:
       return False
    else:
       sys.stdout.write("Please respond with 'yes' or 'no'")

'''
# This function makes sure we remove all those extra frames after
# we're done grabbing faces because that'd take up a lot of storage
# space that could otherwise be used for more training data
'''
def clean_up(dir_path):
    print ('Would you like to clean up (delete) folder: "' + dir_path + '" [y/n]')
    if yn_prompt():
        subprocess.Popen(['rm', '-rf', dir_path])
    print('\nDone cleaning')  

'''
# Find all the videos in the folder the user gives us and store their
# names for future use
'''
def find_all_videos(dir_path):
    #I really hope all these work and I'm not just giving that
    #one guy with a .vob file false hope. I knew some work I did on
    #Alexandria would eventually come in handy
    ext = [".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv", \
                        ".m2ts", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", \
                        ".rm", ".swf", ".vob", ".wmv"]
    file_list = list()
    
    for file in os.listdir(dir_path):
            if file.endswith(tuple(ext)):
                    file_list.append(file)

    return file_list;

'''
# Make everything as modular as possible.
# I envision that some expansion may be done here some time in the
# future so I thought I might as well make this function now
'''
def process_videos (dir_path, video_list):
    for filename in video_list:
        file_to_do = os.path.join(dir_path, filename)
        run_ff(dir_path, file_to_do)
        print('Done extracting frames, moving onto faces...')
        for file in os.listdir(dir_path + r'\faces'):
            if file.endswith('.jpg'):
                    get_faces(os.path.join(dir_path + r'\faces', file))
                    os.remove(os.path.join(dir_path + r'\faces', file))

def process_dir (dir_path):
    for file in os.listdir(dir_path):
            if file.endswith('.jpg'):
                    get_faces(os.path.join(dir_path, file))    





