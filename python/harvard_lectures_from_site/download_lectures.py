#!/usr/bin/env python3
"""
Download all pdfs and YouTube videos from links in a webpage.
used for Harvard Big Data lectures at
http://people.seas.harvard.edu/~minilek/cs229r/fall15/lec.html
Depends on:
    - BeatifulSoup
    - YouTube-DL
    - ffmpeg
"""

__author__ = "Robert Young"
__version__ = "0.1.0"
__license__ = "GPL3"

import argparse
from urllib import parse, request
import pathlib
from subprocess import check_call, getoutput

from bs4 import BeautifulSoup

from logger import setup_logger

logger = setup_logger(logfile="log.txt")

PDF_DIR = pathlib.Path('pdfs')
VIDEO_DIR = pathlib.Path('videos')


def get_links(url):
    """Get pdf and youtube links from page."""
    url_base = url.rstrip('lec.html')

    html = request.urlopen(url)
    logger.info("Reading html")
    soup = BeautifulSoup(html.read(), 'lxml')
    links = soup.find_all('a')

    doc_links = [url_base + link['href']
                 for link in links
                 if 'pdf' in link['href']]
    vid_links = [link['href']
                 for link in links
                 if 'youtube' in link['href']]
    return doc_links, vid_links


def pdfs_from_url(links):
    """Find pdf links and download them"""
    if not PDF_DIR.exists():
        PDF_DIR.mkdir()
    for link in links:
        # Download file with default name to PDF dir
        logger.info("Downloading {}".format(link))
        pdf_path = parse.urlsplit(link).path
        pdf_path = PDF_DIR / pathlib.Path(pdf_path).parts[-1]
        try:
            filename, _ = request.urlretrieve(link,
                                              filename=pdf_path.absolute())
        except Exception as e:
            logger.error("Failed to download {0}: {1}".format(
                link, str(e)))


def videos_from_url(links):
    """Find youtube links and download them"""
    if not VIDEO_DIR.exists():
        VIDEO_DIR.mkdir()
    for link in links:
        logger.info("Downloading {}".format(link))
        check_call(['youtube-dl', link, '-o',
                    VIDEO_DIR.name + r'/%(title)s.%(ext)s'])


def acodec(text):
    """ copy audio or rencode opus audio """
    return 'aac' if 'Opus' in text else 'copy'


def vcodec(text):
    """ copy video or rencode opus audio """
    return 'h264' if 'VP9' in text else 'copy'


def encode_files():
    """Make sure all files are in proper format for media players"""
    for f in VIDEO_DIR.glob('*.mkv'):
        logger.info("Re-encoding {} for use on media players".format(f.name))
        info = getoutput('mediainfo "{}"'.format(f.name))
        check_call(['ffmpeg', '-i', f.absolute(), '-acodec', acodec(info),
                    '-vcodec', vcodec(info), f.with_suffix('.mp4').absolute()])
        f.unlink()


def main(args):
    """ Main entry point of the app """
    logger.info("Attempting with these args:")
    logger.info(args)

    url = args.url
    pdf_links, video_links = get_links(url)

    if pdf_links:
        logger.info("Found {} pdf links".format(len(pdf_links)))
        if args.links_only:
            for link in pdf_links:
                logger.info(link)
        else:
            pdfs_from_url(pdf_links)
    else:
        logger.error("No PDF links found in the page")

    if video_links:
        logger.info("Found {} YouTube links".format(len(video_links)))
        if args.links_only:
            for link in video_links:
                logger.info(link)
        else:
            videos_from_url(video_links)
            encode_files()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("url", help="URL to parse")

    # Optional argument flag which defaults to False
    parser.add_argument("--links-only", action="store_true", default=False)

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
