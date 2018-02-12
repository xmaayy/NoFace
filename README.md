 No Face : An easy way to get faces from images and videos
 ==============================================================================
 
Extract faces from images using python and OpenCV


## Example
### For image files
<img src="/TestImg/face.jpg?raw=True" width="40%">

```
>>> python NoFace.py -d -p 'G:\DeepFake\NoFace\TestImg'
```

<img src="/TestImg/face_crop1.jpg?raw=True" width="40%">

### For a video directory
```

    Directory: G:\NotImportant\NoFace\vid


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----       2018-02-12   6:22 AM       10620330 Short Walks.mp4
```
```
>>> python NoFace.py -v -p 'G:\DeepFake\NoFace\vid'
```
Then check the new 'faces' folder in that directory

<img src="/TestImg/faces.JPG?raw=True" width="40%">

## Flags
```
-p
```
This flag indicates the path, it is necessary unless the file(s) you want to
process are in the same directory with NoFace

```
-d
```
This flag indicates a directory of images

```
-v
```
This flag indicates a directory of video files. It will create a new folder for each video

## TODO

 - Actual testing, this thing is a time bomb right now
 - Add more inpur verification (read any inpur verification at all
 - More checking of what files are where before I start doing processing on them
 - A better progess viewer
 - The face dection isn't all that great in a video with few faces (oops)
    - Maybe look into methods of improving accuracy

## References

https://stackoverflow.com/questions/13211745/detect-face-then-autocrop-pictures

https://static.pexels.com/photos/428339/pexels-photo-428339.jpeg

https://www.youtube.com/watch?v=gJdwtSeYclA
