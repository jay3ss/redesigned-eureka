"""DEPRECATED: this module is no longer worked on/maintained/thought about. For
intents and purposes it has ceased to be.

This module will create the image data set"""
import os


def create_directories():
    """Creates the train, test, and validation directories"""
    directories = ['train', 'test', 'validation']

    for directory in directories:
        try:
            os.mkdir(directory)
        except OSError:
            print (f"Creation of the directory '{directory}' failed")


def scrape():
    pass


if __name__ == '__main__':
    create_directories()
