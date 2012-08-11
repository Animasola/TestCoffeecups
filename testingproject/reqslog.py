from testapp.models import ReqsHistory
from datetime import datetime


class RequestLogger(object):

    def process_request(self, request):
        if request:
            rpath = request.path
            req = ReqsHistory(req_url=request.build_absolute_uri(rpath),
                        req_type=request.method,
                        req_ip=request.META['REMOTE_ADDR'],
                        timestamp=datetime.now(),
                        )
        req.save()
