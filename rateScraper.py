#author	 :	PrabhakaranS
#purpose :	utility for scraping zar_in exch_rate from sbi.co.za
from html.parser import HTMLParser
import urllib.request as urllib2
marker = 0
tag = ''

class myHTMLParser(HTMLParser):
	def handle_data(self, data):
		global marker
		global tag
		if(marker == 1):
			tag = data
			marker = 0
		if(data == "ZAR - INR"): 
			marker += 1
		
parser = myHTMLParser()
ccy = urllib2.urlopen("https://www.statebank.co.za/conversion-rates.aspx")
ccyhtml = ccy.read()
parser.feed(str(ccyhtml))
print('ZAR-INR: '+tag)