import requests
import bs4
from bs4 import element
from bs4 import BeautifulSoup
from bs4 import NavigableString
import re
import csv

url = 'http://www.rcsb.org/pdb/explore/explore.do?structureId=1za4'
response = requests.get(url)
#response.encoding = "utf-8"
#print response.text
soup = bs4.BeautifulSoup(response.text, "lxml")
infile = open('htmlfile.txt', 'w')
infile.write(str(soup))
infile.close()


#find PDBID
for title in soup.find_all('h1'):
    print(title.get_text())
    print url

#find classification
for classification in soup.find('a', class_="querySearchLink"):
    classification = str(classification).strip()
    print classification
outfiletxt = open(title.get_text()  + '.txt', 'w')
outfiletxt.write(title.get_text() + ', ' + url + ', ' + classification + ', ')

#find UniprotID information
for Uniprot in soup.find_all('div', class_="col-sm-7"):

    UniprotID = re.findall(r'[A-Z]\d+', Uniprot.get_text().strip())

    if UniprotID != []:
        strUniprotID = str(UniprotID[0])
        strUniprotlink = str(Uniprot.find_all('a', target="_blank")).split("\"")[1]
        print strUniprotID
        print strUniprotlink
        outfiletxt.write(strUniprotID + ', ' + strUniprotlink + ', ' )
    else:
        continue

#get primaryArtical ID
primaryArticle = str("http://www.rcsb.org/pdb/explore/primaryArticle.do?structureId=%s" %(title.get_text()))

response2 = requests.get(primaryArticle)
soup2 = bs4.BeautifulSoup(response2.text, "lxml")
infile2 = open('primaryArticle.txt', 'w')
infile2.write(str(soup2))
infile2.close()
print "DOI"
DOI = str(soup2.select("#pubmedLinks > li:nth-of-type(3) > a")).split("\"")[1]
print DOI
print "Pubmed"
PubMed = str(soup2.select("#pubmedLinks > li:nth-of-type(1) > span > a")).split("\"")[1]
print PubMed

outfiletxt.write( DOI + ', ' + PubMed + '\n')
outfiletxt.close()
