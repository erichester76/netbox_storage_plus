from netbox.views import generic
import netbox_storage_plus.models as models
import netbox_storage_plus.forms as forms
import netbox_storage_plus.filtersets as filtersets
import netbox_storage_plus.tables as tables

#
# StorageCluster
#
class StorageClusterListView(generic.ObjectListView):
    queryset = models.StorageCluster.objects.all()
    filterset = filtersets.StorageClusterFilterSet
    table = tables.StorageClusterTable

class StorageClusterView(generic.ObjectView):
    queryset = models.StorageCluster.objects.all()

class StorageClusterEditView(generic.ObjectEditView):
    queryset = models.StorageCluster.objects.all()
    form = forms.StorageClusterForm

class StorageClusterDeleteView(generic.ObjectDeleteView):
    queryset = models.StorageCluster.objects.all()

class StorageClusterBulkEditView(generic.BulkEditView):
    queryset = models.StorageCluster.objects.all()
    filterset = filtersets.StorageClusterFilterSet
    table = tables.StorageClusterTable
    form = forms.StorageClusterBulkEditForm

class StorageClusterBulkDeleteView(generic.BulkDeleteView):
    queryset = models.StorageCluster.objects.all()
    filterset = filtersets.StorageClusterFilterSet
    table = tables.StorageClusterTable

class StorageClusterImportView(generic.BulkImportView):
    queryset = models.StorageCluster.objects.all()
    model_form = forms.StorageClusterImportForm

class StorageClusterChangeLogView(generic.ObjectChangeLogView):
    queryset = models.StorageCluster.objects.all()


#
# StoragePool
#
class StoragePoolListView(generic.ObjectListView):
    queryset = models.StoragePool.objects.all()
    filterset = filtersets.StoragePoolFilterSet
    table = tables.StoragePoolTable

class StoragePoolView(generic.ObjectView):
    queryset = models.StoragePool.objects.all()

class StoragePoolEditView(generic.ObjectEditView):
    queryset = models.StoragePool.objects.all()
    form = forms.StoragePoolForm

class StoragePoolDeleteView(generic.ObjectDeleteView):
    queryset = models.StoragePool.objects.all()

class StoragePoolBulkEditView(generic.BulkEditView):
    queryset = models.StoragePool.objects.all()
    filterset = filtersets.StoragePoolFilterSet
    table = tables.StoragePoolTable
    form = forms.StoragePoolBulkEditForm

class StoragePoolBulkDeleteView(generic.BulkDeleteView):
    queryset = models.StoragePool.objects.all()
    filterset = filtersets.StoragePoolFilterSet
    table = tables.StoragePoolTable

class StoragePoolImportView(generic.BulkImportView):
    queryset = models.StoragePool.objects.all()
    model_form = forms.StoragePoolImportForm

class StoragePoolChangeLogView(generic.ObjectChangeLogView):
    queryset = models.StoragePool.objects.all()


#
# StorageVolume
#
class StorageVolumeListView(generic.ObjectListView):
    queryset = models.StorageVolume.objects.all()
    filterset = filtersets.StorageVolumeFilterSet
    table = tables.StorageVolumeTable

class StorageVolumeView(generic.ObjectView):
    queryset = models.StorageVolume.objects.all()

class StorageVolumeEditView(generic.ObjectEditView):
    queryset = models.StorageVolume.objects.all()
    form = forms.StorageVolumeForm

class StorageVolumeDeleteView(generic.ObjectDeleteView):
    queryset = models.StorageVolume.objects.all()

class StorageVolumeBulkEditView(generic.BulkEditView):
    queryset = models.StorageVolume.objects.all()
    filterset = filtersets.StorageVolumeFilterSet
    table = tables.StorageVolumeTable
    form = forms.StorageVolumeBulkEditForm

class StorageVolumeBulkDeleteView(generic.BulkDeleteView):
    queryset = models.StorageVolume.objects.all()
    filterset = filtersets.StorageVolumeFilterSet
    table = tables.StorageVolumeTable

class StorageVolumeImportView(generic.BulkImportView):
    queryset = models.StorageVolume.objects.all()
    model_form = forms.StorageVolumeImportForm

class StorageVolumeChangeLogView(generic.ObjectChangeLogView):
    queryset = models.StorageVolume.objects.all()


#
# StorageShare
#
class StorageShareListView(generic.ObjectListView):
    queryset = models.StorageShare.objects.all()
    filterset = filtersets.StorageShareFilterSet
    table = tables.StorageShareTable

class StorageShareView(generic.ObjectView):
    queryset = models.StorageShare.objects.all()

class StorageShareEditView(generic.ObjectEditView):
    queryset = models.StorageShare.objects.all()
    form = forms.StorageShareForm

class StorageShareDeleteView(generic.ObjectDeleteView):
    queryset = models.StorageShare.objects.all()

class StorageShareBulkEditView(generic.BulkEditView):
    queryset = models.StorageShare.objects.all()
    filterset = filtersets.StorageShareFilterSet
    table = tables.StorageShareTable
    form = forms.StorageShareBulkEditForm

class StorageShareBulkDeleteView(generic.BulkDeleteView):
    queryset = models.StorageShare.objects.all()
    filterset = filtersets.StorageShareFilterSet
    table = tables.StorageShareTable

class StorageShareImportView(generic.BulkImportView):
    queryset = models.StorageShare.objects.all()
    model_form = forms.StorageShareImportForm

class StorageShareChangeLogView(generic.ObjectChangeLogView):
    queryset = models.StorageShare.objects.all()


#
# StorageSnapshot
#
class StorageSnapshotListView(generic.ObjectListView):
    queryset = models.StorageSnapshot.objects.all()
    filterset = filtersets.StorageSnapshotFilterSet
    table = tables.StorageSnapshotTable

class StorageSnapshotView(generic.ObjectView):
    queryset = models.StorageSnapshot.objects.all()

class StorageSnapshotEditView(generic.ObjectEditView):
    queryset = models.StorageSnapshot.objects.all()
    form = forms.StorageSnapshotForm

class StorageSnapshotDeleteView(generic.ObjectDeleteView):
    queryset = models.StorageSnapshot.objects.all()

class StorageSnapshotBulkEditView(generic.BulkEditView):
    queryset = models.StorageSnapshot.objects.all()
    filterset = filtersets.StorageSnapshotFilterSet
    table = tables.StorageSnapshotTable
    form = forms.StorageSnapshotBulkEditForm

class StorageSnapshotBulkDeleteView(generic.BulkDeleteView):
    queryset = models.StorageSnapshot.objects.all()
    filterset = filtersets.StorageSnapshotFilterSet
    table = tables.StorageSnapshotTable

class StorageSnapshotImportView(generic.BulkImportView):
    queryset = models.StorageSnapshot.objects.all()
    model_form = forms.StorageSnapshotImportForm

class StorageSnapshotChangeLogView(generic.ObjectChangeLogView):
    queryset = models.StorageSnapshot.objects.all()


#
# StorageReplication
#
class StorageReplicationListView(generic.ObjectListView):
    queryset = models.StorageReplication.objects.all()
    filterset = filtersets.StorageReplicationFilterSet
    table = tables.StorageReplicationTable

class StorageReplicationView(generic.ObjectView):
    queryset = models.StorageReplication.objects.all()

class StorageReplicationEditView(generic.ObjectEditView):
    queryset = models.StorageReplication.objects.all()
    form = forms.StorageReplicationForm

class StorageReplicationDeleteView(generic.ObjectDeleteView):
    queryset = models.StorageReplication.objects.all()

class StorageReplicationBulkEditView(generic.BulkEditView):
    queryset = models.StorageReplication.objects.all()
    filterset = filtersets.StorageReplicationFilterSet
    table = tables.StorageReplicationTable
    form = forms.StorageReplicationBulkEditForm

class StorageReplicationBulkDeleteView(generic.BulkDeleteView):
    queryset = models.StorageReplication.objects.all()
    filterset = filtersets.StorageReplicationFilterSet
    table = tables.StorageReplicationTable

class StorageReplicationImportView(generic.BulkImportView):
    queryset = models.StorageReplication.objects.all()
    model_form = forms.StorageReplicationImportForm

class StorageReplicationChangeLogView(generic.ObjectChangeLogView):
    queryset = models.StorageReplication.objects.all()


#
# StorageBackup
#
class StorageBackupListView(generic.ObjectListView):
    queryset = models.StorageBackup.objects.all()
    filterset = filtersets.StorageBackupFilterSet
    table = tables.StorageBackupTable

class StorageBackupView(generic.ObjectView):
    queryset = models.StorageBackup.objects.all()

class StorageBackupEditView(generic.ObjectEditView):
    queryset = models.StorageBackup.objects.all()
    form = forms.StorageBackupForm

class StorageBackupDeleteView(generic.ObjectDeleteView):
    queryset = models.StorageBackup.objects.all()

class StorageBackupBulkEditView(generic.BulkEditView):
    queryset = models.StorageBackup.objects.all()
    filterset = filtersets.StorageBackupFilterSet
    table = tables.StorageBackupTable
    form = forms.StorageBackupBulkEditForm

class StorageBackupBulkDeleteView(generic.BulkDeleteView):
    queryset = models.StorageBackup.objects.all()
    filterset = filtersets.StorageBackupFilterSet
    table = tables.StorageBackupTable

class StorageBackupImportView(generic.BulkImportView):
    queryset = models.StorageBackup.objects.all()
    model_form = forms.StorageBackupImportForm

class StorageBackupChangeLogView(generic.ObjectChangeLogView):
    queryset = models.StorageBackup.objects.all()
