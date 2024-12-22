from netbox.tables import NetBoxTable
from django2_tables import columns
import netbox_storage_plus.models as models

class StorageClusterTable(NetBoxTable):
    name = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.StorageCluster
        fields = ('pk', 'id', 'name', 'cluster_type', 'osd_count', 'description')
        default_columns = ('name', 'cluster_type', 'osd_count')


class StoragePoolTable(NetBoxTable):
    name = columns.Column(linkify=True)
    cluster = columns.Column(linkify=True)
    device = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.StoragePool
        fields = (
            'pk', 'id', 'name', 'cluster', 'device', 'pool_type', 'raid_level',
            'replication_factor', 'erasure_code_profile', 'capacity_gb', 'used_gb', 'description'
        )
        default_columns = ('name', 'cluster', 'device', 'pool_type', 'raid_level')


class StorageVolumeTable(NetBoxTable):
    name = columns.Column(linkify=True)
    pool = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.StorageVolume
        fields = (
            'pk', 'id', 'name', 'pool', 'volume_type', 'capacity_gb',
            'used_gb', 'thin_provisioned', 'compression', 'description'
        )
        default_columns = ('name', 'pool', 'volume_type')


class StorageShareTable(NetBoxTable):
    name = columns.Column(linkify=True)
    volume = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.StorageShare
        fields = (
            'pk', 'id', 'name', 'volume', 'share_type',
            'export_path', 'description'
        )
        default_columns = ('name', 'volume', 'share_type')


class StorageSnapshotTable(NetBoxTable):
    name = columns.Column(linkify=True)
    volume = columns.Column(linkify=True)
    share = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.StorageSnapshot
        fields = (
            'pk', 'id', 'name', 'volume', 'share', 'created_at',
            'snapshot_type', 'size_gb', 'description'
        )
        default_columns = ('name', 'volume', 'share', 'created_at', 'snapshot_type')


class StorageReplicationTable(NetBoxTable):
    name = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.StorageReplication
        fields = (
            'pk', 'id', 'name', 'source_volume', 'target_volume',
            'source_share', 'target_share', 'schedule', 'description'
        )
        default_columns = ('name', 'schedule')


class StorageBackupTable(NetBoxTable):
    name = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.StorageBackup
        fields = (
            'pk', 'id', 'name', 'volume', 'share',
            'backup_location', 'schedule', 'last_run', 'description'
        )
        default_columns = ('name', 'schedule', 'last_run')
