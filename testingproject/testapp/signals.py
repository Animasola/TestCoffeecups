# -*- coding: utf-8 -*-
import logging
import traceback
import pprint
import os
from django.db.models import get_models
from django.conf import settings


logging.basicConfig(
    level=logging.ERROR,
    filename=os.path.join(settings.DEPLOY_DIR, 'testapp/signals.log'),
    filemode='w'
    )


def ModelChangeLog(sender, instance, signal, *args, **kwargs):
    mdl = sender.__name__
    if mdl == "ModelLog":
        return
    tgt_instance = instance
    if 'created' in kwargs:
        if kwargs['created']:
            action_ = "Created"
        else:
            action_ = "Altered"
    else:
        action_ = "Deleted"
    from testingproject.testapp.models import ModelLog
    log = ModelLog(model=mdl,
                    target_instance=tgt_instance,
                    action=action_,)
    try:
        log.save()
    except:
        stack = pprint.pformat(traceback.extract_stack())
        logging.error('An error occurred:\n %s' % stack)
