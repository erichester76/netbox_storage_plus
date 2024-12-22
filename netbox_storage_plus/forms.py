from django import forms
from utilities.forms import NetBoxModelForm, BulkEditForm, CSVModelForm
import netbox_storage_plus.models as models

#
# StorageCluster
#
class StorageClusterForm(NetBoxModelForm):
    class Meta:
        model = models.StorageCluster
        fields = ('name', 'devices', 'cluster_type', 'osd_count', 'description')


class StorageClusterBulkEditForm(BulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.StorageCluster.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    class Meta:
        nullable_fields = ['description', 'cluster_type']


class StorageClusterImportForm(CSVModelForm):
    class Meta:
        model = models.StorageCluster
        fields = ('name', 'cluster_type', 'osd_count', 'description')


#
# StoragePool
#
class StoragePoolForm(NetBoxModelForm):
    class Meta:
        model = models.StoragePool
        fields = (
            'name', 'cluster', 'device', 'pool_type', 'raid_level',
            'replication_factor', 'erasure_code_profile', 'capacity_gb',
            'used_gb', 'description'
        )

class StoragePoolBulkEditForm(BulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.StoragePool.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    class Meta:
        nullable_fields = ['description', 'raid_level', 'erasure_code_profile']


class StoragePoolImportForm(CSVModelForm):
    class Meta:
        model = models.StoragePool
        fields = (
            'name', 'cluster', 'device', 'pool_type', 'raid_level',
            'replication_factor', 'erasure_code_profile', 'capacity_gb',
            'used_gb', 'description'
        )


#
# StorageVolume
#
class StorageVolumeForm(NetBoxModelForm):
    class Meta:
        model = models.StorageVolume
        fields = (
            'name', 'pool', 'volume_type', 'capacity_gb', 'used_gb',
            'thin_provisioned', 'compression', 'description'
        )

class StorageVolumeBulkEditForm(BulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.StorageVolume.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    class Meta:
        nullable_fields = ['description', 'compression']


class StorageVolumeImportForm(CSVModelForm):
    class Meta:
        model = models.StorageVolume
        fields = (
            'name', 'pool', 'volume_type', 'capacity_gb', 'used_gb',
            'thin_provisioned', 'compression', 'description'
        )


#
# StorageShare
#
class StorageShareForm(NetBoxModelForm):
    class Meta:
        model = models.StorageShare
        fields = ('name', 'volume', 'share_type', 'export_path', 'description')

class StorageShareBulkEditForm(BulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.StorageShare.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    class Meta:
        nullable_fields = ['description', 'export_path']

class StorageShareImportForm(CSVModelForm):
    class Meta:
        model = models.StorageShare
        fields = ('name', 'volume', 'share_type', 'export_path', 'description')


#
# StorageSnapshot
#
class StorageSnapshotForm(NetBoxModelForm):
    class Meta:
        model = models.StorageSnapshot
        fields = (
            'name', 'volume', 'share', 'snapshot_type',
            'size_gb', 'description'
        )

class StorageSnapshotBulkEditForm(BulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.StorageSnapshot.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    class Meta:
        nullable_fields = ['description', 'snapshot_type']


class StorageSnapshotImportForm(CSVModelForm):
    class Meta:
        model = models.StorageSnapshot
        fields = (
            'name', 'volume', 'share', 'snapshot_type',
            'size_gb', 'description'
        )


#
# StorageReplication
#
class StorageReplicationForm(NetBoxModelForm):
    class Meta:
        model = models.StorageReplication
        fields = (
            'name', 'source_volume', 'target_volume',
            'source_share', 'target_share', 'schedule', 'description'
        )

class StorageReplicationBulkEditForm(BulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.StorageReplication.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    class Meta:
        nullable_fields = ['description', 'schedule']


class StorageReplicationImportForm(CSVModelForm):
    class Meta:
        model = models.StorageReplication
        fields = (
            'name', 'source_volume', 'target_volume',
            'source_share', 'target_share', 'schedule', 'description'
        )


#
# StorageBackup
#
class StorageBackupForm(NetBoxModelForm):
    class Meta:
        model = models.StorageBackup
        fields = (
            'name', 'volume', 'share', 'backup_location',
            'schedule', 'last_run', 'description'
        )

class StorageBackupBulkEditForm(BulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.StorageBackup.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    class Meta:
        nullable_fields = ['description', 'last_run']

class StorageBackupImportForm(CSVModelForm):
    class Meta:
        model = models.StorageBackup
        fields = (
            'name', 'volume', 'share', 'backup_location',
            'schedule', 'last_run', 'description'
        )
