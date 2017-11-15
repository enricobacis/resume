#!/usr/bin/env python

from argparse import ArgumentParser
from bs4 import BeautifulSoup
from sys import argv
import re

parser = ArgumentParser(description="fix the html resume")
parser.add_argument("INPUT", help="input file")
parser.add_argument("OUTPUT", help="output file")
args = parser.parse_args()

with open(args.INPUT) as fp:
    soup = BeautifulSoup(fp.read(), 'lxml')

# make google analytics soup
analytics_soup = BeautifulSoup('''
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-73621100-1', 'auto');
  ga('set', 'anonymizeIp', true);
  ga('send', 'pageview');

</script>''', 'lxml')

mail = 'enrico.bacis@gmail.com'
mailto_soup = BeautifulSoup('<a href="mailto:{0}">{0}</a>'.format(mail), 'lxml')

# remove phone
phone = soup.find('div', {'class': 'phone'})
if phone: phone.decompose()

# remove all email obfuscation scripts
for script in soup.findAll('script'):
    script.decompose()

# unprotect email
for email in soup.findAll('div', {'class': 'email'}):
    email.a.replace_with(mailto_soup.a)

for link in soup.findAll('link'):
    link['href'] = link['href'].replace('bootswatch.com/lumen/', 'bootswatch.com/3/lumen/')
    link['href'] = re.sub(r'https?://', '//', link['href'])

# add google analytics script
soup.head.insert(len(soup.head.contents), analytics_soup.script)

# write back to file
html = soup.prettify(soup.original_encoding)
with open(args.OUTPUT, 'wb') as fp:
    fp.write(html)
