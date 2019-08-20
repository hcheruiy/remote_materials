#
# OOP in Python
# 
"""
The most basic element of any modern application is an object
To a programmer, the world is a collection of objects.
Objects consists of two types of members: attributes and methods.
Members can be private, public or protected.
Classes are data types of objects. 
Every object is an instance of a class.
A class can be inherited in child classes.
Two classes can be associated using composition.

Example of a generic web crawler:
"""
from abc import ABCMeta, abstractmethod
import BeautifulSoup
import urllib
import sys
import bleach

############## Root Class (Abstract) ################
class SkyThoughtCollector(object):

    __metaclass__ = ABCMeta

    base_url_string = "base_url"
    airlines_string = "air_lines"
    limit_string = "limits"
    base_url = ""
    airlines = []
    limit = 10

    @abstractmethod
    def collect_thoughts(self):
        print("Something Wrong!! You are calling an abstract method")

    @classmethod
    def get_config(self, config_path):
        #print("in get Config")
        config = {}
        conf = open(configpath)
        for line in conf:
            if ("#" not in line):
                words = line.strip().split('=')
                config[words[0].strip()] = words[1].strip()
        
        #print config
        self.base_url = config[self.base_url_string]
        if config.has_key(self.airlines_string):
            self.airlines = config[self.airlines_string].split(',')
        if config.has_key(self.limit_string):
            self.limit = int(config[self.limit_string])

        # print self.airlines

    def download_url(self, url):
        #print("downloading url...")
        page_file = urllib.urlopen(url)
        if page_file.getcode() != 200:
            return "Problem in URL"
        page_html = page_file.read()
        page_file.close()
        return "".join(page_html)

    def remove_junk(self, arg):
        f = open('junk.txt')
        for line in f:
            arg.replace(line.strip(), '')
        return arg

    def print_args(self, args):
        out = ''
        last = 0
        for arg in args:
            if args.index(arg) == len(args) - 1:
                last = 1
            reload(sys)
            sys.setdefaultencoding('utf-8')
            arg = arg.decode('utf8', 'ignore')
            encode('ascii', 'ignore').strip()
            arg = arg.replace('\n', ' ')
            arg = arg.replace('\r', '')
            arg = self.remove_junk(arg)
            if last == 0:
                out = out + arg + '\t'
            else:
                out = out + arg
        print(out)


############## Airlines Chield ##################
class AirlineReviewCollector(SkyThoughtCollector):

    months = ['January', 'February', 'March', 'April', 'May',
              'June', 'July', 'August', 'September', 'October',
              'November', 'December' ]

    def __init__(self, config_path):
        #print("In Config")

    super(AirlineReviewCollector, self).get_config(config_path)

    def parse_soup_header(self, header):
        #print("Parsing header")
        name = surname = year = month = date = country = ''
        tct = header.find('h9')
        words = str(txt).strip().split(' ')
        for j in range(len(words) - 1):
            if words[j] in self.months:
                date = words[j -1]
                month = words[j]
                year = words[j + 1]
                name = words[j + 3]
                surname = words[j + 4]
        if ")" in words[-1]:
            country = words[-1].split(')')[0]
        if "(" in country:
            country = country.split("(")[1]
        else:
            country = words[-2].split('(')[1] + country
        
        return (name, surname, year, month, date, country)

def parse_soup_table(self, table):
    #print("parsing table...")
    images = table.findAll("img")
    over_all = str(images[0]).split("grn_bar_")[1].split(".gif")[0]
    money_value = str(images[1]).split("SCORE_")[1].split(".gif")[0]
    seat_comfort = str(images[2]).split("SCORE_")[1].split(".gif")[0]
    staff_service = str(images[3]).split("SCORE_")[1].split(".gif")[0]
    catering = str(images[4]).split("SCORE_")[1].split(".gif")[0]
    entertainment = str(images[4]).split("SCORE_")[1].split(".gif")[0]
    
    if 'YES' in str(images[6]):
        recommend = 'YES'
    else:
        recommend = 'NO'
        
    status = table.findAll("p", {"class":"text25"})
    stat = str(status[2]).split(">")[1].split("<")[0]
    
    return (stat, over_all, money_value, seat_comfort,
            staff_service, catering, entertainment, recomend)

def collect_thoughts(self):
    #print("Collecting Thoughts")
    
    for al in AirlineReviewCollector.airlines:
        count = 0
        while count < AirlineReviewCollector.limit:
            count = count + 1
            url = ''
            if count == 1:
                url = AirlineReviewCollector.base_url + al + ".htm"
            else:
                url = AirlineReviewCollector.base_url + al + "_" + str(count) + ".htm"
            soup = BeautifulSoup.BeautifulSoup(super(AirlineReviewCollector, self).downloadURL(url))
            
            blogs = soup.findAll("p", {"class":"text2"})
            tables = soup.findAll("table", {"width":"192"})
            review_headers = soup.findAll("td", {"class":"airport"})
for i in range(len(tables)-1):
(name, surname, year, month,
date, country) = self.parse
SoupHeader(review_headers[i])
(stat, over_all, money_value,
seat_comfort, staff_service,
catering, entertainment,
recomend) = self.parseSoup
Table(tables[i])
blog = str(blogs[i]).
split(">")[1].split("<")[0]
args = [al, name, surname,
year, month, date, country,
stat, over_all, money_value,
seat_comfort, staff_service,
catering, entertainment,
recomend, blog]

