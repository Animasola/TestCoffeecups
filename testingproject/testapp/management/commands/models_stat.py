from django.core.management.base import NoArgsCommand
from sys import stderr


class Command(NoArgsCommand):
    requires_model_validation = True

    def handle_noargs(self, **options):
        from django.db.models import get_app, get_models
        lines = []
        for model in get_models():
            lines.append("[%s]" % model.__name__ +\
                " - %s objects" % model._default_manager.count() or "" + "\n")
        self.stderr.write("error: " + "%s" % "\nerror: ".join(lines))
        return "\n".join(lines)
