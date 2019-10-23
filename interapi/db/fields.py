import ast

from django.db import models

class DictField(models.TextField):

    description = "Dictionary"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def to_python(self, value):
        if value == "":
            return None
        
        return ast.literal_eval(value)
    
    def get_db_prep_save(self, value, *args, **kwargs):
        if value == "":
            return None

        if isinstance(value, dict):
            value = str(value)
        return super(DictField, self).get_db_prep_save(value, *args, **kwargs)

class JSONField(models.TextField):
    """
    JSONField is a generic textfield that neatly serializes/unserializes
    JSON objects seamlessly.
    Django snippet #1478

    example:
        class Page(models.Model):
            data = JSONField(blank=True, null=True)


        page = Page.objects.get(pk=5)
        page.data = {'title': 'test', 'type': 3}
        page.save()
    """

    def to_python(self, value):
        if value == "":
            return None

        try:
            if isinstance(value, basestring):
                return json.loads(value)
        except ValueError:
            pass
        return value

    def get_db_prep_save(self, value, *args, **kwargs):
        if value == "":
            return None
        if isinstance(value, dict):
            value = json.dumps(value, cls=DjangoJSONEncoder)
        return super(JSONField, self).get_db_prep_save(value, *args, **kwargs)