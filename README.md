# make better QOL scripts
生活に役立つスクリプトを適宜おいていくリポジトリ

# Apple Script
## environments
Mac OS High Sierra

## environments
### textCount
count to selected text without space & enter on Apple Script.

### Replacement Dictionary
open Replacement Dictionary with selected text to the clipboard on Apple Script
## How to use
Make own "Services" using Automator Apps.
* open Automator Apps, select "Services"
* double click "run Apple Script"
* copy&paste blow scripts
* then save, move to Keyboard Preference in System Preference.
* already added your service to "Services Preference" in Shortcut tab there.

# python
## environments
Python 3.7.0

requirements.txt

ffmpeg version 4.1

## equipments

### logging_settings.py
setting your logger object
* logging Level
    - DEBUG level
* saving format
```
(current directry)/[YOUR_LOGGER_OBJECT_NAME]/[YOUR_LOGGER_OBJECT_NAME]_y-m-d.log
```
#### how to use
call below in your python file
```
from logging_settings import logging_setting
logger = logging_setting([YOUR_LOGGER_OBJECT_NAME])
```

### youtube2wav.py
download youtube video for mp4 and wav files.
* saving format
```
(current directry)/youtube2mp4/[YOUTUBE_TILE].mp4   # mp4 file
(current directry)/youtube2wav/[YOUTUBE_TILE].wav # wav file
```
#### how to use
```
python youtube2wav.py [YOUTUBE URL]
```
