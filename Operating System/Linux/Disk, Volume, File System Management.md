# Extend LVM Volume Size
## Check Disk Size
```bash
df -lh
Filesystem Size Used Avail Use% Mounted on
udev 967M 0 967M 0% /dev
tmpfs 200M 1.2M 199M 1% /run
/dev/mapper/ubuntu–vg-ubuntu–lv 3.9G 3.6G 107M 98% /
tmpfs 997M 0 997M 0% /dev/shm
tmpfs 5.0M 0 5.0M 0% /run/lock
tmpfs 997M 0 997M 0% /sys/fs/cgroup
/dev/loop0 98M 98M 0 100% /snap/docker/384
/dev/loop1 89M 89M 0 100% /snap/core/7270
/dev/sda2 976M 212M 698M 24% /boot
/dev/loop2 90M 90M 0 100% /snap/core/8039
tmpfs 200M 0 200M 0% /run/user/1000
/dev/loop3 123M 123M 0 100% /snap/docker/418
```

## Display Volume Group
```bash
server2:~$ sudo vgdisplay
— Volume group —
VG Name ubuntu-vg
System ID
Format lvm2
Metadata Areas 1
Metadata Sequence No 2
VG Access read/write
VG Status resizable
MAX LV 0
Cur LV 1
Open LV 1
Max PV 0
Cur PV 1
Act PV 1
VG Size <79.00 GiB
PE Size 4.00 MiB
Total PE 20223
Alloc PE / Size 1024 / 4.00 GiB
Free PE / Size 19199 / <75.00 GiB
VG UUID fU0TVP-fXBW-WbfE-jJUU-mlPF-x0Oh-2VS2wm
```

## Display Logical Volume
```bash
server2:~$ sudo lvdisplay
— Logical volume —
LV Path /dev/ubuntu-vg/ubuntu-lv
LV Name ubuntu-lv
VG Name ubuntu-vg
LV UUID iGplFB-6ByB-K2os-8Pf7-u0BI-R1qL-3JmDv6
LV Write Access read/write
LV Creation host, time ubuntu-server, 2019-11-11 16:00:29 +0800
LV Status available
# open 1
LV Size 4.00 GiB
Current LE 1024
Segments 1
Allocation inherit
Read ahead sectors auto
– currently set to 256
Block device 253:0
```

## Extend Logical Volume
```bash
server2:~$ sudo lvextend -l 19199 /dev/ubuntu-vg/ubuntu-lv
Size of logical volume ubuntu-vg/ubuntu-lv changed from 4.00 GiB (1024 extents) to <75.00 GiB (19199 extents).
Logical volume ubuntu-vg/ubuntu-lv successfully resized.
```

## Display Volume Group again

- It still has 4GB free
```bash
server2:~$ sudo vgdisplay
— Volume group —
VG Name ubuntu-vg
System ID
Format lvm2
Metadata Areas 1
Metadata Sequence No 3
VG Access read/write
VG Status resizable
MAX LV 0
Cur LV 1
Open LV 1
Max PV 0
Cur PV 1
Act PV 1
VG Size <79.00 GiB
PE Size 4.00 MiB
Total PE 20223
Alloc PE / Size 19199 / <75.00 GiB
Free PE / Size 1024 / 4.00 GiB
VG UUID fU0TVP-fXBW-WbfE-jJUU-mlPF-x0Oh-2VS2wm
```

## Extend it again, but this time use + to specify additional space
```bash
server2:~$ sudo lvextend -l +1024 /dev/ubuntu-vg/ubuntu-lv
Size of logical volume ubuntu-vg/ubuntu-lv changed from <75.00 GiB (19199 extents) to <79.00 GiB (20223 extents).
Logical volume ubuntu-vg/ubuntu-lv successfully resized.
```

## Display Volume Group
```bash
server2:~$ sudo vgdisplay
— Volume group —
VG Name ubuntu-vg
System ID
Format lvm2
Metadata Areas 1
Metadata Sequence No 4
VG Access read/write
VG Status resizable
MAX LV 0
Cur LV 1
Open LV 1
Max PV 0
Cur PV 1
Act PV 1
VG Size <79.00 GiB
PE Size 4.00 MiB
Total PE 20223
Alloc PE / Size 20223 / <79.00 GiB
Free PE / Size 0 / 0
VG UUID fU0TVP-fXBW-WbfE-jJUU-mlPF-x0Oh-2VS2wm
```

## Resize File System 
```bash
server2:~$ sudo resize2fs /dev/ubuntu-vg/ubuntu-lv
resize2fs 1.44.1 (24-Mar-2018)
Filesystem at /dev/ubuntu-vg/ubuntu-lv is mounted on /; on-line resizing required
old_desc_blocks = 1, new_desc_blocks = 10
The filesystem on /dev/ubuntu-vg/ubuntu-lv is now 20708352 (4k) blocks long.
```

## Check Disk Size again
```bash
server2:~$ df -h
Filesystem Size Used Avail Use% Mounted on
udev 967M 0 967M 0% /dev
tmpfs 200M 1.2M 199M 1% /run
/dev/mapper/ubuntu–vg-ubuntu–lv 78G 3.6G 71G 5% /
tmpfs 997M 0 997M 0% /dev/shm
tmpfs 5.0M 0 5.0M 0% /run/lock
tmpfs 997M 0 997M 0% /sys/fs/cgroup
/dev/loop0 98M 98M 0 100% /snap/docker/384
/dev/loop1 89M 89M 0 100% /snap/core/7270
/dev/sda2 976M 212M 698M 24% /boot
/dev/loop2 90M 90M 0 100% /snap/core/8039
tmpfs 200M 0 200M 0% /run/user/1000
/dev/loop3 123M 123M 0 100% /snap/docker/418
```
