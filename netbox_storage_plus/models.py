from django.db import models
from django.core.exceptions import ValidationError
from netbox.models import NetBoxModel
from dcim.models import Device

#
# StorageCluster
#
class StorageCluster(NetBoxModel):
    name = models.CharField(max_length=100, unique=True)
    devices = models.ManyToManyField(
        to=Device,
        blank=True,
        related_name='storage_clusters'
    )
    cluster_type = models.CharField(max_length=50, blank=True)
    osd_count = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


#
# StoragePool
#
class StoragePool(NetBoxModel):
    name = models.CharField(max_length=100)
    cluster = models.ForeignKey(
        to=StorageCluster,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='storage_pools'
    )
    device = models.ForeignKey(
        to=Device,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='storage_pools'
    )
    pool_type = models.CharField(
        max_length=50,
        blank=True,
        help_text="e.g. LVM, ZFS, Ceph, MDRAID, etc."
    )
    raid_level = models.CharField(
        max_length=20,
        blank=True,
        help_text="e.g. RAID5, Z2, etc."
    )
    replication_factor = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="For Ceph, Gluster, etc."
    )
    erasure_code_profile = models.CharField(
        max_length=50,
        blank=True,
        help_text="e.g. 'k=2,m=1' for Ceph"
    )
    capacity_gb = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    used_gb = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    description = models.TextField(blank=True)

    def clean(self):
        if not self.cluster and not self.device:
            raise ValidationError("Specify either a cluster or a device for this pool.")
        if self.cluster and self.device:
            raise ValidationError("Cannot specify both a cluster and a device for the same pool.")

    def __str__(self):
        return self.name


#
# StorageVolume
#
class StorageVolume(NetBoxModel):
    name = models.CharField(max_length=100)
    pool = models.ForeignKey(
        to=StoragePool,
        on_delete=models.PROTECT,
        related_name='volumes'
    )
    volume_type = models.CharField(
        max_length=50,
        blank=True,
        help_text="e.g. LVM LV, ZFS dataset, Ceph RBD, etc."
    )
    capacity_gb = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    used_gb = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    thin_provisioned = models.BooleanField(default=False)
    compression = models.CharField(
        max_length=50,
        blank=True,
        help_text="Compression alg if relevant (ZFS, btrfs, etc.)"
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pool.name}/{self.name}"


#
# StorageShare
#
class StorageShare(NetBoxModel):
    name = models.CharField(max_length=100)
    volume = models.ForeignKey(
        to=StorageVolume,
        on_delete=models.PROTECT,
        related_name='shares'
    )
    share_type = models.CharField(max_length=50, blank=True)
    export_path = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.share_type})"


#
# StorageSnapshot
#
class StorageSnapshot(NetBoxModel):
    name = models.CharField(max_length=100)
    volume = models.ForeignKey(
        to=StorageVolume,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='snapshots'
    )
    share = models.ForeignKey(
        to=StorageShare,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='snapshots'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    snapshot_type = models.CharField(max_length=50, blank=True)
    size_gb = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


#
# StorageReplication
#
class StorageReplication(NetBoxModel):
    name = models.CharField(max_length=100, unique=True)
    source_volume = models.ForeignKey(
        to=StorageVolume,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='replications_as_source'
    )
    target_volume = models.ForeignKey(
        to=StorageVolume,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='replications_as_target'
    )
    source_share = models.ForeignKey(
        to=StorageShare,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='replications_as_source'
    )
    target_share = models.ForeignKey(
        to=StorageShare,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='replications_as_target'
    )
    schedule = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


#
# StorageBackup
#
class StorageBackup(NetBoxModel):
    name = models.CharField(max_length=100, unique=True)
    volume = models.ForeignKey(
        to=StorageVolume,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='backups'
    )
    share = models.ForeignKey(
        to=StorageShare,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='backups'
    )
    backup_location = models.CharField(max_length=255, blank=True)
    schedule = models.CharField(max_length=100, blank=True)
    last_run = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
