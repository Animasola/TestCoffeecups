# -*- coding: utf-8 -*-


def ModelChangeLog(sender, instance, signal, *args, **kwargs):
    mdl = sender.__name__
    id_ = instance.id
    if 'created' in kwargs:
        if kwargs['created']:
            action_ = "Created"
        else:
            action_ = "Altered"
    else:
        action_ = "Deleted"
    try:
        from testapp.models import ModelLog
        log = ModelLog(model=mdl,
                       id_zap=id_,
                       action=action_,)
        log.save()
    except:
        pass
