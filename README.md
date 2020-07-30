# Simple Python Code to Extract Text From a Website

![](https://i.postimg.cc/tgQsK9fD/pycode.png)

## About the code

The code will scrape the text content of a website using python 3.x. It require `urllib` and `beautifulsoup` libraries to do the same. It requires links has to be placed in a separate file as `links.txt`. Each URL should form a septate line. In case, if you don't want to be this as a separate file, replace **ln. 8** in `scrape.py` to 

`urls = ['http://www.xyz.com','http://www.abc.com', ...]`

Beautifulsoup will parse and clean the code by removing scripts and design elements. Then, it will be written in the output file `data.txt`.

## Usage

1. Clone this repository or download the contents as zip file
2. Replace the links in `links.txt` file
3. Run `python scrape.py`
4. Scraped data will be available in `data.txt`

## Library Installation

1. If you have both python 2 and 3 use the command `python3` to run the file
2. Install `urllib` by
	* `pip3 install urllib3`
3. Install `beautifulsoup` by
	* `pip install beautifulsoup4`
