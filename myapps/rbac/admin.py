from django.contrib import admin
from rbac import models
from werkzeug.security import generate_password_hash
from rbac.email_task import register_mail
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'menu']


class PermissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', 'feature',  'group']
    # list_editable = ('url',)

class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',]


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username','email' ]
    search_fields = ('username',)

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """

        if obj.email:
            register_mail.delay(obj.email,obj.username,obj.password_hash)
        obj.password_hash = str(generate_password_hash(obj.password_hash))

        print(obj.password_hash)
        print(obj.__dict__)

        obj.save()


class UserPayAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'stime','month','alipay_num','weichat_num']

class VipAdmin(admin.ModelAdmin):
    list_display = ['id', 'isvip', 'stime', 'etime', ]


admin.site.register(models.Menu)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Permission, PermissionAdmin)
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.Role, RoleAdmin)
admin.site.register(models.UserPay, UserPayAdmin)
admin.site.register(models.VIP, VipAdmin)
