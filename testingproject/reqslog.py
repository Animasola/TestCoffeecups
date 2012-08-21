from testapp.models import ReqsHistory


class RequestLogger(object):

    def process_request(self, request):
        if request:
            requested_url = request.build_absolute_uri(request.path)
            if request.method == 'POST':
                priority = 2
            elif request.method == 'GET' and ('/static/' in requested_url or '/media/' in requested_url):
                priority = 1
            else:
                priority = 0
            req = ReqsHistory(req_url=requested_url,
                        req_type=request.method,
                        req_ip=request.META['REMOTE_ADDR'],
                        req_priority=priority
                        )
        req.save()
