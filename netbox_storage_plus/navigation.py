from netbox.plugins import PluginMenuItem, PluginMenuButton
from utilities.choices import ButtonColor

menu_items = (
    PluginMenuItem(
        link='plugins:storage_plus:storagecluster_list',
        link_text='Storage Clusters',
        buttons=[
            PluginMenuButton(
                link='plugins:storage_plus:storagecluster_add',
                title='Add Cluster',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColor.GREEN
            ),
            PluginMenuButton(
                link='plugins:storage_plus:storagecluster_import',
                title='Import Clusters',
                icon_class='mdi mdi-upload',
                color=ButtonColor.BLUE
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:storage_plus:storagepool_list',
        link_text='Storage Pools',
        buttons=[
            PluginMenuButton(
                link='plugins:storage_plus:storagepool_add',
                title='Add Pool',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColor.GREEN
            ),
            PluginMenuButton(
                link='plugins:storage_plus:storagepool_import',
                title='Import Pools',
                icon_class='mdi mdi-upload',
                color=ButtonColor.BLUE
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:storage_plus:storagevolume_list',
        link_text='Volumes',
        buttons=[
            PluginMenuButton(
                link='plugins:storage_plus:storagevolume_add',
                title='Add Volume',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColor.GREEN
            ),
            PluginMenuButton(
                link='plugins:storage_plus:storagevolume_import',
                title='Import Volumes',
                icon_class='mdi mdi-upload',
                color=ButtonColor.BLUE
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:storage_plus:storageshare_list',
        link_text='Shares',
        buttons=[
            PluginMenuButton(
                link='plugins:storage_plus:storageshare_add',
                title='Add Share',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColor.GREEN
            ),
            PluginMenuButton(
                link='plugins:storage_plus:storageshare_import',
                title='Import Shares',
                icon_class='mdi mdi-upload',
                color=ButtonColor.BLUE
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:storage_plus:storagesnapshot_list',
        link_text='Snapshots',
        buttons=[
            PluginMenuButton(
                link='plugins:storage_plus:storagesnapshot_add',
                title='Add Snapshot',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColor.GREEN
            ),
            PluginMenuButton(
                link='plugins:storage_plus:storagesnapshot_import',
                title='Import Snapshots',
                icon_class='mdi mdi-upload',
                color=ButtonColor.BLUE
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:storage_plus:storagereplication_list',
        link_text='Replication',
        buttons=[
            PluginMenuButton(
                link='plugins:storage_plus:storagereplication_add',
                title='Add Replication',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColor.GREEN
            ),
            PluginMenuButton(
                link='plugins:storage_plus:storagereplication_import',
                title='Import Replications',
                icon_class='mdi mdi-upload',
                color=ButtonColor.BLUE
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:storage_plus:storagebackup_list',
        link_text='Backups',
        buttons=[
            PluginMenuButton(
                link='plugins:storage_plus:storagebackup_add',
                title='Add Backup',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColor.GREEN
            ),
            PluginMenuButton(
                link='plugins:storage_plus:storagebackup_import',
                title='Import Backups',
                icon_class='mdi mdi-upload',
                color=ButtonColor.BLUE
            )
        ]
    ),
)
