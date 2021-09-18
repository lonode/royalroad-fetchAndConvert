# royalroad-fetchAndConvert
Automatically download a royalroad story, convert it to kindle format and push it to the device.


# Features

* Retrieve automatically all the chapters of the given story
* Support table of content for ebook conversion
* Support author note at both end and start of the chapter
* Support images
* Support CSS rules for different stories (e.g. "Everybody Love Large Chest")
* Very low memory and performance footprint
* Convert the story in the azw3 format, and push it to the kindle.


# Libraries used

This script uses requests_html python package. https://html.python-requests.org/. Install it :  

	pip install requests

This script is based on this royalroad fetcher : [royalroad-reader](https://github.com/lpicou/royalroad-reader/). It also uses [calibre](https://github.com/kovidgoyal/calibre) to convert and push the ebook to the kindle. Everything is included here. 

# Usage 

	fetchAndCopy.py url_of_chapter number_of_chapters name_of_ebook

Parameters :  

* url_of_chapter : The URL of the chapter (not of the story homepage!)
* number_of_chapters : You guessed. If you want the whole book, just enter something like 99999
* name_of_ebook : The name of the ebook, .html extension will be added when the file is written on the filesystem. 

It reads the chapter content of the URL given ( url_of_chapter ) and goes to the next chapter, and it loops number_of_chapters times.  
name_of_ebook is the name of the ebook which will be pushed to the kindle.  

This script write .html and .azw3 file temporary on the filesystem, and then delete them.

## Example  

If you want to fetch the best rated story Mother of Learning from the first chapter, execute the following command :

    python fetch_book.py https://www.royalroad.com/fiction/21220/mother-of-learning/chapter/301778/1-good-morning-brother 102 MOL
  
In the example above, MOL.html is written a the working directory.
