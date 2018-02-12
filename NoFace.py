'''
# Call this file with its absolute MULTITUDE of options
# to pass in either a video or image file directory
'''

from DirProc import verify_paths, find_all_videos, process_videos, process_dir
import time
import sys

def main():
    is_video = False;
    is_dir = False;
    img_file = "";

    for x in range(1,len(sys.argv)):
        if(sys.argv[x] == '-v'):
            is_video = True;
        elif (sys.argv[x] == '-d'):
            is_dir = True;
        elif (sys.argv[x] == '-p' ):
            img_file = sys.argv[x+1]
            x = x+1
    if (is_video):
        verify_paths(img_file)
        vids = find_all_videos(img_file)
        process_videos(img_file, vids)
    elif (is_dir):
        process_dir(img_file)

t0 = time.time()
main()
t1 = time.time()

print('The process completed in: ')
print(t1-t0)

