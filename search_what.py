#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Nguyen Hoai Nam
import optparse
import requests

MAPPING_MONTH = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August", 9: "September",
    10: "October", 11: "November", 12: "December"
}


def get_url(month_number, year):
    month_string = MAPPING_MONTH[month_number]
    url = "http://lists.openstack.org/pipermail/" \
          "openstack-dev/%s-%s/thread.html" % (month_string, year)
    return requests.get(url)


def main():
    global LF
    parser = optparse.OptionParser(usage="usage: %prog [options]",
                                   version="%prog 1.0")
    parser.add_option("-m", "--month", action='store', type="int",
                      dest="month", default=None,
                      help="A month which need to seach")
    parser.add_option("-sm", "--start-month", action='store', type="int",
                      dest="start_month", default=None, help="Start month")
    parser.add_option("-em", "--end-month", action='store', type="int",
                      dest="end_month", default=None, help="End month")
    parser.add_option("-y", "--year", action='store', type="int",
                      dest="year", help="Year", default=2016)
    parser.add_option("-k", "--keyword", action='store', type="string",
                      dest="keyword", help="Keyword to search")
    (options, args) = parser.parse_args()
    month = options.month
    start_month = options.start_month
    end_month = options.end_month
    year = options.year
    keyword = options.keyword
    
if __name__ == "__main__":
    main()
