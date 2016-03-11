import urllib2
from bs4 import BeautifulSoup as bs4

def main():
    try:
         i = 0
         while i < len(list1):
              url = urllib2.urlopen("https://in.finance.yahoo.com/q?s=" + list1[i] + "&ql=0")
              soup = bs4(url,"html.parser")
              price = soup.find(attrs={'id':"yfs_l84_" + list1[i]})
              print "Stock Symbol : " + stocks.upper()
              if price:
                    print ("price: {1}".format(list1[i],price.contents[0]))
                    i += 1
              for open in soup.find_all('td', attrs={'class': 'yfnc_tabledata1'})[1:2]:
                     print "open: " + (''.join( open.strings))
                     i += 1
              for prev_open in soup.find_all('td', attrs={'class': 'yfnc_tabledata1'})[0:1]:
                      print "prev close : "  + (''.join(prev_open.strings))
                      i += 1
              for days_range in soup.find_all('td', attrs={'class': 'yfnc_tabledata1'})[7:8]:
                      print "days range : " + (''.join(days_range.strings))
                      i += 1
              for eps in soup.find_all('td',attrs={'class':'yfnc_tabledata1'})[13:14]:
                      print "EPS: " + (''.join(eps.strings))
                      i += 1
              for vol in soup.find_all('td',attrs={'class':'yfnc_tabledata1'})[9:10]:
                      print "Volume: " + (''.join(vol.strings))
                      i += 1
              for volavg in soup.find_all('td',attrs={'class':'yfnc_tabledata1'})[10:11]:
                       print "Volume(avg 3m): " + (''.join(volavg.strings))
                       i += 1
              for rangewk in soup.find_all('td',attrs={'class':'yfnc_tabledata1'})[8:9]:
                       print "52 WK Range: " + (''.join(rangewk.strings))
                       i += 1
              for cap in soup.find_all('td',attrs={'class':'yfnc_tabledata1'})[11:12]:
                        print "Market Capitalization: " + (''.join(cap.strings))
                        i += 1
              for earning in soup.find_all('td',attrs={'class':'yfnc_tabledata1'})[6:7]:
                        print "Earning Date: " + (''.join(earning.strings))
    except:
       print "ERROR! something went wrong!"



if __name__ == "__main__":
      stocks = raw_input("Please enter a stock symbol: ")
      list1 = stocks.split()
      main()
      




