#author	 :	PrabhakaranS
#purpose :	utility for scraping zar_inr exch_rate from sbi.co.za
from html.parser import HTMLParser
import urllib.request as urllib2
marker = 0
rate = ''

class myHTMLParser(HTMLParser):
	def handle_data(self, data):
		global marker
		global rate
		if(marker == 1):
			rate = data
			marker = 0
		if(data == "ZAR - INR"): 
			marker += 1
		
parser = myHTMLParser()
urlcon = urllib2.urlopen("https://www.statebank.co.za/conversion-rates.aspx")
ccyhtml = urlcon.read()
parser.feed(str(ccyhtml))
print('ZAR-INR: '+rate)
