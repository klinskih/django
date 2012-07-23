from django.db.models import *
from socket import inet_aton, inet_ntoa
from struct import pack, unpack

class IPField(IPAddressField):
        empty_strings_allowed = False

        __metaclass__ = SubfieldBase

        def get_db_prep_value(self, value,*args,**kwargs):
#               print "to db", type(value), value
                if not value: return None
                return unpack('!l', inet_aton(value))[0]

        def get_internal_type(self):
                return "PositiveIntegerField"

        def to_python(self, value):
                if type(value).__name__ in ('NoneType', 'unicode'): return value
                try:
#                       print "to py", type(value), value
                        return inet_ntoa(pack('!l', value))
                except (TypeError, ValueError):
                        raise models.exceptions.ValidationError("IP address cannot be converted to string.")

