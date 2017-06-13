# blender-makehuman-fanim

This is a little experiment for blender to create facial animation from video
It uses objects following trackers on video to calculate translation for face bones

Right now it doesn't support complex bone position/rotation calculating
At now it just translates bones according to trackers

# Use it
## Trackers
First of all you should create a set of trackers from video
All needed trackers see in `FRun.py`

## Run script
To use it run 
```
from FRun import FRun
FRun.run(your_imported_makehuman_object)
```


