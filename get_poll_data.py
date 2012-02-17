""" Try to web scrap some poll data and get it into a nice format """

import lxml.html, csv

webbase = "http://www.realclearpolitics.com/epolls/2012/president/us/{page}"

faceoff_pages = {'allreps' : 'republican_presidential_nomination-1452.html',
            'obamaVromney' : 'general_election_romney_vs_obama-1171.html',
            'obamaVgingrich' : 'general_election_gingrich_vs_obama-1453.html',
            'obamaVsantorum' : 'general_election_santorum_vs_obama-2912.html',
            'obamaVpaul': 'general_election_paul_vs_obama-1750.html'}


for name,page in faceoff_pages.iteritems():
    print "Parsing {page} and writing {name} file...".format(page=page,name=name)

    address = webbase.format(page=page)
    doc = lxml.html.parse(address)
    table = doc.xpath("//table[@class='data layout']")[0]

    with open('data/{name}.csv'.format(name=name),'w') as f:
        cf = csv.writer(f)
        #grab every row after the first two
        for tr in table.xpath('./tr')[2:]:
            # add the text of all tds inside each tr to a list
            row = [td.text_content().strip() for td in tr.xpath('./td')]
            # write the list to the csv file:
            cf.writerow(row)
            print row