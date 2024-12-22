from netbox.plugins import PluginConfig

class StoragePlusConfig(PluginConfig):
    name = 'netbox_storage_plus'
    verbose_name = 'Storage+'
    description = 'Additional storage management plugin for NetBox'
    version = '0.1'
    min_version = '3.4.0'
    max_version = '3.6.99'
    default_auto_field = 'django.db.models.AutoField'

config = StoragePlusConfig
