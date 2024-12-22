from django.urls import path
import netbox_storage_plus.views as views

app_name = 'storage_plus'

urlpatterns = [
    # StorageCluster
    path('clusters/', views.StorageClusterListView.as_view(), name='storagecluster_list'),
    path('clusters/add/', views.StorageClusterEditView.as_view(), name='storagecluster_add'),
    path('clusters/import/', views.StorageClusterImportView.as_view(), name='storagecluster_import'),
    path('clusters/edit/', views.StorageClusterBulkEditView.as_view(), name='storagecluster_bulk_edit'),
    path('clusters/delete/', views.StorageClusterBulkDeleteView.as_view(), name='storagecluster_bulk_delete'),
    path('clusters/<int:pk>/', views.StorageClusterView.as_view(), name='storagecluster'),
    path('clusters/<int:pk>/edit/', views.StorageClusterEditView.as_view(), name='storagecluster_edit'),
    path('clusters/<int:pk>/delete/', views.StorageClusterDeleteView.as_view(), name='storagecluster_delete'),
    path('clusters/<int:pk>/changelog/', views.StorageClusterChangeLogView.as_view(), name='storagecluster_changelog'),

    # StoragePool
    path('pools/', views.StoragePoolListView.as_view(), name='storagepool_list'),
    path('pools/add/', views.StoragePoolEditView.as_view(), name='storagepool_add'),
    path('pools/import/', views.StoragePoolImportView.as_view(), name='storagepool_import'),
    path('pools/edit/', views.StoragePoolBulkEditView.as_view(), name='storagepool_bulk_edit'),
    path('pools/delete/', views.StoragePoolBulkDeleteView.as_view(), name='storagepool_bulk_delete'),
    path('pools/<int:pk>/', views.StoragePoolView.as_view(), name='storagepool'),
    path('pools/<int:pk>/edit/', views.StoragePoolEditView.as_view(), name='storagepool_edit'),
    path('pools/<int:pk>/delete/', views.StoragePoolDeleteView.as_view(), name='storagepool_delete'),
    path('pools/<int:pk>/changelog/', views.StoragePoolChangeLogView.as_view(), name='storagepool_changelog'),

    # StorageVolume
    path('volumes/', views.StorageVolumeListView.as_view(), name='storagevolume_list'),
    path('volumes/add/', views.StorageVolumeEditView.as_view(), name='storagevolume_add'),
    path('volumes/import/', views.StorageVolumeImportView.as_view(), name='storagevolume_import'),
    path('volumes/edit/', views.StorageVolumeBulkEditView.as_view(), name='storagevolume_bulk_edit'),
    path('volumes/delete/', views.StorageVolumeBulkDeleteView.as_view(), name='storagevolume_bulk_delete'),
    path('volumes/<int:pk>/', views.StorageVolumeView.as_view(), name='storagevolume'),
    path('volumes/<int:pk>/edit/', views.StorageVolumeEditView.as_view(), name='storagevolume_edit'),
    path('volumes/<int:pk>/delete/', views.StorageVolumeDeleteView.as_view(), name='storagevolume_delete'),
    path('volumes/<int:pk>/changelog/', views.StorageVolumeChangeLogView.as_view(), name='storagevolume_changelog'),

    # StorageShare
    path('shares/', views.StorageShareListView.as_view(), name='storageshare_list'),
    path('shares/add/', views.StorageShareEditView.as_view(), name='storageshare_add'),
    path('shares/import/', views.StorageShareImportView.as_view(), name='storageshare_import'),
    path('shares/edit/', views.StorageShareBulkEditView.as_view(), name='storageshare_bulk_edit'),
    path('shares/delete/', views.StorageShareBulkDeleteView.as_view(), name='storageshare_bulk_delete'),
    path('shares/<int:pk>/', views.StorageShareView.as_view(), name='storageshare'),
    path('shares/<int:pk>/edit/', views.StorageShareEditView.as_view(), name='storageshare_edit'),
    path('shares/<int:pk>/delete/', views.StorageShareDeleteView.as_view(), name='storageshare_delete'),
    path('shares/<int:pk>/changelog/', views.StorageShareChangeLogView.as_view(), name='storageshare_changelog'),

    # StorageSnapshot
    path('snapshots/', views.StorageSnapshotListView.as_view(), name='storagesnapshot_list'),
    path('snapshots/add/', views.StorageSnapshotEditView.as_view(), name='storagesnapshot_add'),
    path('snapshots/import/', views.StorageSnapshotImportView.as_view(), name='storagesnapshot_import'),
    path('snapshots/edit/', views.StorageSnapshotBulkEditView.as_view(), name='storagesnapshot_bulk_edit'),
    path('snapshots/delete/', views.StorageSnapshotBulkDeleteView.as_view(), name='storagesnapshot_bulk_delete'),
    path('snapshots/<int:pk>/', views.StorageSnapshotView.as_view(), name='storagesnapshot'),
    path('snapshots/<int:pk>/edit/', views.StorageSnapshotEditView.as_view(), name='storagesnapshot_edit'),
    path('snapshots/<int:pk>/delete/', views.StorageSnapshotDeleteView.as_view(), name='storagesnapshot_delete'),
    path('snapshots/<int:pk>/changelog/', views.StorageSnapshotChangeLogView.as_view(), name='storagesnapshot_changelog'),

    # StorageReplication
    path('replications/', views.StorageReplicationListView.as_view(), name='storagereplication_list'),
    path('replications/add/', views.StorageReplicationEditView.as_view(), name='storagereplication_add'),
    path('replications/import/', views.StorageReplicationImportView.as_view(), name='storagereplication_import'),
    path('replications/edit/', views.StorageReplicationBulkEditView.as_view(), name='storagereplication_bulk_edit'),
    path('replications/delete/', views.StorageReplicationBulkDeleteView.as_view(), name='storagereplication_bulk_delete'),
    path('replications/<int:pk>/', views.StorageReplicationView.as_view(), name='storagereplication'),
    path('replications/<int:pk>/edit/', views.StorageReplicationEditView.as_view(), name='storagereplication_edit'),
    path('replications/<int:pk>/delete/', views.StorageReplicationDeleteView.as_view(), name='storagereplication_delete'),
    path('replications/<int:pk>/changelog/', views.StorageReplicationChangeLogView.as_view(), name='storagereplication_changelog'),

    # StorageBackup
    path('backups/', views.StorageBackupListView.as_view(), name='storagebackup_list'),
    path('backups/add/', views.StorageBackupEditView.as_view(), name='storagebackup_add'),
    path('backups/import/', views.StorageBackupImportView.as_view(), name='storagebackup_import'),
    path('backups/edit/', views.StorageBackupBulkEditView.as_view(), name='storagebackup_bulk_edit'),
    path('backups/delete/', views.StorageBackupBulkDeleteView.as_view(), name='storagebackup_bulk_delete'),
    path('backups/<int:pk>/', views.StorageBackupView.as_view(), name='storagebackup'),
    path('backups/<int:pk>/edit/', views.StorageBackupEditView.as_view(), name='storagebackup_edit'),
    path('backups/<int:pk>/delete/', views.StorageBackupDeleteView.as_view(), name='storagebackup_delete'),
    path('backups/<int:pk>/changelog/', views.StorageBackupChangeLogView.as_view(), name='storagebackup_changelog'),
]
