from xadmin import views
import xadmin
from rbac import models
from rbac.email_task import register_mail
from werkzeug.security import generate_password_hash



class GroupAdmin(object):
    list_display = ['id', 'title', 'menu']
    # model_icon = 'fa fa-check'
class PermissionAdmin(object):
    list_display = ['id', 'url', 'feature',  'group']
    # list_editable = ('url',)

class RoleAdmin(object):
    list_display = ['id', 'title',]


class UserAdmin(object):
    list_display = ['id', 'username','email' ]
    search_fields = ('username',)



    def save_models(self):
        """
        Given a model instance save it to the database.
        """
        obj = self.new_obj
        request = self.request
        if obj.email:
            register_mail.delay(obj.email,obj.username,obj.password_hash)
        obj.password_hash = str(generate_password_hash(obj.password_hash))

        print(obj.password_hash)
        print(obj.__dict__)

        obj.save()

class UserPayAdmin():
    list_display = ['id', 'amount', 'stime','month','alipay_num','weichat_num']

class VipAdmin():
    list_display = ['id', 'isvip', 'stime', 'etime', ]

xadmin.site.register(models.Menu)
xadmin.site.register(models.User, UserAdmin)
xadmin.site.register(models.Permission, PermissionAdmin)
xadmin.site.register(models.Group, GroupAdmin)
xadmin.site.register(models.Role, RoleAdmin)
xadmin.site.register(models.UserPay, UserPayAdmin)
xadmin.site.register(models.VIP, VipAdmin)
