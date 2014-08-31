#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import re
import wget
import os.path

class MusicForProgramming:

    def __init__(self, base_url, feed_url, destination_dir):

        # set initial values

        self.base_url = base_url
        self.feed_url = feed_url
        self.destination_dir = destination_dir

        self.episodes = dict()
        self.file_urls = dict()

        # parse feed

        self.feed = requests.get(self.feed_url, timeout=30) # seconds

        if (self.feed.status_code == requests.codes.ok):
            self.results = BeautifulSoup(self.feed.content)
            # find and store relevant data
            for item in self.results.find_all('item'):
                title = item.title.string
                episode_number_regex = re.compile("\d+")
                number = int(episode_number_regex.findall(title)[0])
                self.episodes[number] = title
                url = item.guid.string
                self.file_urls[number] = url

        else:
            self.feed.raise_for_status()

    def list_episodes(self):
        episodes = self.episodes.items()
        print episodes
        return episodes

    def count_episodes(self):
        count = len(self.episodes)
        print count
        return count

    def get_episode(self, episode_number):
        filename = wget.filename_from_url(self.file_urls[episode_number])
        full_file_path = self.destination_dir + filename
        if (not os.path.isfile(full_file_path)):
            print "Downloading... " + filename
            file_url = self.file_urls[episode_number]
            print file_url
            wget.download(file_url, out=full_file_path)
            print "Done... Next!"
        else:
            print "Skipping ... " + filename

    def get_all_episodes(self):
        for episode in self.episodes.keys():
            self.get_episode(episode)

if __name__ == "__main__":
    mfp = MusicForProgramming(base_url="http://www.musicforprogramming.net/",
    feed_url="http://www.musicforprogramming.net/rss.php",
    destination_dir="/home/YOUR_USERNAME/music/musicforprogramming/") # use full path with end slash

    mfp.get_all_episodes()
