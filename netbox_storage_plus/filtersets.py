import django_filters
from netbox.filtersets import NetBoxModelFilterSet
import netbox_storage_plus.models as models

class StorageClusterFilterSet(NetBoxModelFilterSet):
    q = django_filters.CharFilter(method='search', label='Search')

    class Meta:
        model = models.StorageCluster
        fields = ('id', 'name', 'cluster_type')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(name__icontains=value)


class StoragePoolFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.StoragePool
        fields = ('id', 'name', 'pool_type', 'raid_level')


class StorageVolumeFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.StorageVolume
        fields = ('id', 'name', 'pool', 'volume_type')


class StorageShareFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.StorageShare
        fields = ('id', 'name', 'share_type')


class StorageSnapshotFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.StorageSnapshot
        fields = ('id', 'name', 'volume', 'share', 'snapshot_type')


class StorageReplicationFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.StorageReplication
        fields = ('id', 'name', 'source_volume', 'target_volume', 'source_share', 'target_share')


class StorageBackupFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.StorageBackup
        fields = ('id', 'name', 'volume', 'share')
