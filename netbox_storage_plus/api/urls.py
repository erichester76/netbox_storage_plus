from rest_framework.routers import DefaultRouter
import netbox_storage_plus.api.views as api_views

router = DefaultRouter()
router.register('clusters', api_views.StorageClusterViewSet)
router.register('pools', api_views.StoragePoolViewSet)
router.register('volumes', api_views.StorageVolumeViewSet)
router.register('shares', api_views.StorageShareViewSet)
router.register('snapshots', api_views.StorageSnapshotViewSet)
router.register('replications', api_views.StorageReplicationViewSet)
router.register('backups', api_views.StorageBackupViewSet)

urlpatterns = router.urls
