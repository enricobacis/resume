#!/usr/bin/env python2

from argparse import ArgumentParser
from bs4 import BeautifulSoup

parser = ArgumentParser(description="fix the html resume")
parser.add_argument("INPUT", help="input file")
parser.add_argument("OUTPUT", help="output file")
args = parser.parse_args()

with open(args.INPUT) as fp:
    soup = BeautifulSoup(fp.read(), 'html.parser')

mail = 'enrico.bacis@gmail.com'
mailto_soup = BeautifulSoup('<a href="mailto:{0}">{0}</a>'.format(mail), 'html.parser')

# add google analytics script
ANALYTICS_PLACEHOLDER = 'ANALYTICS_PLACEHOLDER'
ANALYTICS_CODE = '''
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-73621100-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-73621100-1', { 'anonymize_ip': true });
</script>
'''

soup.head.insert(0, soup.new_string(ANALYTICS_PLACEHOLDER))

# generate html
html = soup.prettify(soup.original_encoding)

# substitute placeholder
html = html.replace(ANALYTICS_PLACEHOLDER, ANALYTICS_CODE)

# write back to file
with open(args.OUTPUT, 'wb') as fp:
    fp.write(html)
