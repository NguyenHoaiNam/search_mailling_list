ml_search - Search all header of mailing-list on OpenStack
========================================================================

Installation
------------

By using pip::

    pip install ml_search

Example
-------

To find all mailing-lists which has a "Nova" keyword on the title
from Dec-2016 to Nov-2016::

    ml_search -s 10 -e 11 -y 2016 -k Nova

Author
------
Nguyen Hoai Nam
