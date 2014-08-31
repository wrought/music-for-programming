# Missing API to [Music for Programming](http://www.musicforprogramming.net)

I wanted a simple way to download all of the episodes of from MusicForProgramming, so figured I might as well write a reusable script.

## Usage

### Linux or whatever

#### Quickstart

    git clone https://github.com/wrought/music-for-programming.git
    cd music-for-programming
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

Update the value for `destination_dir` at the bottom of `musicforprogramming.py` to suit your system's needs.

Use following command to download all episodes (default). Note the script will skip any files with matching `filename` found in `destination_dir`, so you can also use this default action to download only new episodes.

    python musicforprogramming.py

#### Use as Module

You can also use this script as a python module without instantiating the default object.

    from musicforprogramming import MusicForProgramming
    mfp = MusicForProgramming(base_url="", feed_url="", destination_dir="")
