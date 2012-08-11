from testapp.models import ReqsHistory


class RequestLogger(object):

    def process_request(self, request):
        if request:
            rpath = request.path
            req = ReqsHistory(req_url=request.build_absolute_uri(rpath),
                        req_type=request.method,
                        req_ip=request.META['REMOTE_ADDR'],
                        )
        req.save()
