from bs4 import BeautifulSoup
import requests

html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# To parse a document
soup = BeautifulSoup(html, 'html.parser')

# We can use the method prettify() to display the HTML in the nested structure:
print(soup.prettify())

# Tags: The Tag object correponds to an HTML tag in the original document
tag_object_t = soup.title
print("tag object:", tag_object_t)

# If there is more than one Tag with the same name, the first element with that Tag name is called. This corresponds to the most paid player:
tag_object = soup.h3
print(tag_object)

# Children, Parents, and Siblings: we can access the child of the tag or navigate down the branch as follows:
tag_child = tag_object.b
print(tag_child)

tag_parent = tag_child.parent
print(tag_parent)

sibling1 = tag_object.nextSibling
print(sibling1)

sibling2 = sibling1.nextSibling
print(sibling2)

# Exercise: next_sibling
# Use the object sibling_2 and the method next_sibling to find the salary of Stephen Curry:
print("Salary:", sibling2.next_sibling)

# HTML Atrributes

# If the tag has attributes, the tag id="boldest" has an attribute id whose value is boldest. You can access a tag’s attributes by treating the tag like a dictionary:
tag_child['id'] # or tag_child('id')
tag_child.attrs

# Downloading And Scraping The Contents Of A Web Page

url = "http://www.ibm.com"
data = requests.get(url).text

# We create a BeautifulSoup object using the BeautifulSoup constructor
soup = BeautifulSoup(data, 'html.parser')

# Scraping all links
for link in soup.find_all('a', href="True"):
    print(link.get('href'))

# Scrape all images Tags
for link in soup.find_all('img'):
    print(link.get('src'))

# Scrape data from HTML Tables
url_table = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

data = requests.get(url_table).text

soup = BeautifulSoup(data, 'html.parser')

# Find a html table in the webpage
table = soup.find('table')

# Get all rows from the table

for row in table.find_all('tr'):
    cols = row.find_all('td')
    color_name = cols[2].string
    color_code = cols[3].string
    print(f"{color_name}--->{color_code}")


