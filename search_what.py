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
    month_string = MAPPING_MONTH[int(month_number)]
    url = "http://lists.openstack.org/pipermail/" \
          "openstack-dev/%s-%s/thread.html" % (year, month_string)
    get_request = requests.get(url)
    content_request = get_request.content
    return content_request.split('\n')


def my_heart(content, list_filter):
    result = []
    list_filter_upper = [member.upper() for member in list_filter]
    for i in content:
        if i.startswith('<LI><A'):
            i_upper = i.upper()
            if all(word in i_upper for word in list_filter_upper):
                from_index = i.find('[openstack-dev]')
                result.append(i[from_index:])
    return result


def action_filter(month, year, keywords):
    content_ml = get_url(month, year)
    result_filter = my_heart(content_ml, keywords)
    print '#### The result for %s in %s' % \
          (MAPPING_MONTH[month], year)
    for i in result_filter:
        print i


def main():
    parser = optparse.OptionParser(usage="usage: %prog [options]",
                                   version="%prog 1.0")
    parser.add_option("-m", "--month", action='store', type="int",
                      dest="month", default=None, metavar="MONTH",
                      help="A month which need to seach")
    parser.add_option("-s", "--start-month", action='store',
                      type="int", dest="start_month",
                      metavar="START_MONTH",
                      default=None, help="Start month")
    parser.add_option("-e", "--end-month", action='store',
                      type="int", dest="end_month", default=None,
                      metavar="END_MONTH", help="End month")
    parser.add_option("-y", "--year", action='store', type="int",
                      metavar="YEAR",
                      dest="year", help="Year", default=2016)
    parser.add_option("-k", "--keyword", action='append',
                      type="string", dest="keywords",
                      metavar="KEYWORDS", help="Keyword to search")
    (options, args) = parser.parse_args()
    month = options.month
    start_month = options.start_month
    end_month = options.end_month
    year = options.year
    keywords = options.keywords
    if month:
        action_filter(month, year, keywords)
    else:
        range_month = range(int(start_month), int(end_month) + 1)
        for month in range_month:
            action_filter(month, year, keywords)


if __name__ == "__main__":
    main()
