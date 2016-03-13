# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.dupefilters import RFPDupeFilter

class SeenURLFilter(RFPDupeFilter):

	#settings = None

    def __init__(self, path=None, debug=False):
        self.urls_seen = set()
        RFPDupeFilter.__init__(self, path)

    def request_seen(self, request):
    	# print "====request url is ",request.url
    	# print "request meta is ",request.meta
    	if request.meta.get("method"):
    		print "skip dupefilters"
    		return

        if request.url in self.urls_seen:
            return True
        else:
            self.urls_seen.add(request.url)
    
