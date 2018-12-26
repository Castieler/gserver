from __future__ import absolute_import
import xadmin
from .models import UserSettings, Log
from xadmin.layout import *

from django.utils.translation import ugettext_lazy as _, ugettext

class UserSettingsAdmin(object):
    model_icon = 'fa fa-cog'
    hidden_menu = True
# 基础设置
class BaseSetting(object):
    enable_themes = True    # 使用主题
    use_bootswatch = True

# 全局设置
class GlobalSettings(object):
    site_title = 'DataMining管理系统'  # 标题
    site_footer = 'DataMining管理系统'  # 页尾
    site_url = '/'
    menu_style = 'accordion'  # 设置左侧菜单  折叠样式
xadmin.site.register(xadmin.views.CommAdminView,GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView,BaseSetting)
xadmin.site.register(UserSettings, UserSettingsAdmin)

class LogAdmin(object):

    def link(self, instance):
        if instance.content_type and instance.object_id and instance.action_flag != 'delete':
            admin_url = self.get_admin_url('%s_%s_change' % (instance.content_type.app_label, instance.content_type.model), 
                instance.object_id)
            return "<a href='%s'>%s</a>" % (admin_url, _('Admin Object'))
        else:
            return ''
    link.short_description = ""
    link.allow_tags = True
    link.is_column = False

    list_display = ('action_time', 'user', 'ip_addr', '__str__', 'link')
    list_filter = ['user', 'action_time']
    search_fields = ['ip_addr', 'message']
    model_icon = 'fa fa-cog'

xadmin.site.register(Log, LogAdmin)







