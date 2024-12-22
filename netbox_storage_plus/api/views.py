from netbox.api.viewsets import NetBoxModelViewSet
import netbox_storage_plus.models as models
import netbox_storage_plus.filtersets as filtersets
import netbox_storage_plus.api.serializers as serializers

class StorageClusterViewSet(NetBoxModelViewSet):
    queryset = models.StorageCluster.objects.all()
    serializer_class = serializers.StorageClusterSerializer
    filterset_class = filtersets.StorageClusterFilterSet

class StoragePoolViewSet(NetBoxModelViewSet):
    queryset = models.StoragePool.objects.all()
    serializer_class = serializers.StoragePoolSerializer
    filterset_class = filtersets.StoragePoolFilterSet

class StorageVolumeViewSet(NetBoxModelViewSet):
    queryset = models.StorageVolume.objects.all()
    serializer_class = serializers.StorageVolumeSerializer
    filterset_class = filtersets.StorageVolumeFilterSet

class StorageShareViewSet(NetBoxModelViewSet):
    queryset = models.StorageShare.objects.all()
    serializer_class = serializers.StorageShareSerializer
    filterset_class = filtersets.StorageShareFilterSet

class StorageSnapshotViewSet(NetBoxModelViewSet):
    queryset = models.StorageSnapshot.objects.all()
    serializer_class = serializers.StorageSnapshotSerializer
    filterset_class = filtersets.StorageSnapshotFilterSet

class StorageReplicationViewSet(NetBoxModelViewSet):
    queryset = models.StorageReplication.objects.all()
    serializer_class = serializers.StorageReplicationSerializer
    filterset_class = filtersets.StorageReplicationFilterSet

class StorageBackupViewSet(NetBoxModelViewSet):
    queryset = models.StorageBackup.objects.all()
    serializer_class = serializers.StorageBackupSerializer
    filterset_class = filtersets.StorageBackupFilterSet
