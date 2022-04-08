import json

from django.conf import settings
from django.urls import reverse

try:
    from django.urls.exceptions import NoReverseMatch
except ImportError:
    from django.core.urlresolvers import NoReverseMatch

MAX = 75


class LogEntryAdminMixin:

    def created(self, obj):
        return obj.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    created.short_description = 'Created'

    def user_url(self, obj):
        if obj.actor:
            app_label, model = settings.AUTH_USER_MODEL.split('.')
            viewname = f'admin:{app_label}_{model.lower()}_change'
            link = reverse(viewname, args=[obj.actor.id])
            return f'<a href="{link}">{obj.actor}</a>'

        return 'system'
    user_url.allow_tags = True
    user_url.short_description = 'User'

    def resource_url(self, obj):
        app_label, model = obj.content_type.app_label, obj.content_type.model
        viewname = f'admin:{app_label}_{model}_change'
        try:
            link = reverse(viewname, args=[obj.object_id])
        except NoReverseMatch:
            return obj.object_repr
        else:
            return f'<a href="{link}">{obj.object_repr}</a>'
    resource_url.allow_tags = True
    resource_url.short_description = 'Resource'

    def msg_short(self, obj):
        if obj.action == 2:
            return ''  # delete
        changes = json.loads(obj.changes)
        s = '' if len(changes) == 1 else 's'
        fields = ', '.join(changes.keys())
        if len(fields) > MAX:
            i = fields.rfind(' ', 0, MAX)
            fields = fields[:i] + ' ..'
        return '%d change%s: %s' % (len(changes), s, fields)
    msg_short.short_description = 'Changes'

    def msg(self, obj):
        if obj.action == 2:
            return ''  # delete
        changes = json.loads(obj.changes)
        msg = '<table><tr><th>#</th><th>Field</th><th>From</th><th>To</th></tr>'
        for i, field in enumerate(sorted(changes), 1):
            value = [i, field] + (['***', '***'] if field == 'password' else changes[field])
            msg += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % tuple(value)
        msg += '</table>'
        return msg
    msg.allow_tags = True
    msg.short_description = 'Changes'
