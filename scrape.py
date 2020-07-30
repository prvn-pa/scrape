import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# Inlcude links to be scraped in 'links.txt file'
link = open('links.txt', 'r')
# Read each line of the file
urls = link.readlines() 

# Creating data for appending each webpage
data = []
# Open the output file for writing
with open('data.txt', 'w') as f:
	for url in urls:
		# Next line is mandatory for scraping Indian language sites
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		response = urlopen(req).read()
		html = response.decode('utf-8')
		soup = BeautifulSoup(html, 'html.parser')

		# kill all script and style elements
		for script in soup(["script", "style"]):
			script.extract()    # rip it out

		# get text
		text = soup.get_text()

		# break into lines and remove leading and trailing space on each
		lines = (line.strip() for line in text.splitlines())
		# break multi-headlines into a line each
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		# drop blank lines
		text = '\n'.join(chunk for chunk in chunks if chunk)
		# Write the scraped data
		f.write(text)
# Loop to write till last URL
data.append(text)

