import platform
MYSQL_HOST = '10.30.1.22'
MYSQL_PORT = 3555
MYSQL_DATABASE = 'django_role'
MYSQL_USER = 'xiamingyu'
MYSQL_PASS = 'xiamingyu'

DEFAULT_CONF = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gserver',
        'USER': 'root',
        'PASSWORD': 'xiamingyu',
        'HOST': '106.13.49.191',
        'PORT': 3306,
        'CHARSET': 'utf8',
        'COLLATION': 'utf8_general_ci',
        'OPTIONS':{
            # 'init_command':"SET sql_mode='STRICT_TRANS_TABLES'",
                'sql_mode': 'traditional',
        }
    }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'djangoblog',
#         'USER': 'root',
#         'PASSWORD': 'xiamingyu',
#         'HOST': '106.13.49.191',
#         'PORT': 3306,
#         'OPTIONS': {'charset': 'utf8mb4'},
#     }
# }
