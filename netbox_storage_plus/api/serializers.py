from netbox.api.serializers import NetBoxModelSerializer
import netbox_storage_plus.models as models

class StorageClusterSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.StorageCluster
        fields = '__all__'

class StoragePoolSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.StoragePool
        fields = '__all__'

class StorageVolumeSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.StorageVolume
        fields = '__all__'

class StorageShareSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.StorageShare
        fields = '__all__'

class StorageSnapshotSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.StorageSnapshot
        fields = '__all__'

class StorageReplicationSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.StorageReplication
        fields = '__all__'

class StorageBackupSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.StorageBackup
        fields = '__all__'
