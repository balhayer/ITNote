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

## Troubleshooting
- If pvgroup doesn't see new space, need to extend the physical partition: growpart
- Then rescan the physical volume: pvscan
- Then extend logical volume: lvextend
- Finally Resize File System: resize2fs
```bash
sudo growpart /dev/sda 3
CHANGED: partition=3 start=2101248 old: size=417327104 end=419428352 new: size=1046474719 end=1048575967
sudo pvdisplay
  --- Physical volume ---
  PV Name               /dev/sda3
  VG Name               ubuntu-vg
  PV Size               <199.00 GiB / not usable 1.00 MiB
  Allocatable           yes (but full)
  PE Size               4.00 MiB
  Total PE              50943
  Free PE               0
  Allocated PE          50943
  PV UUID               AEoQW4-KLnN-M8dm-qnFi-lnch-8IFC-Az2F5Y

sudo parted
GNU Parted 3.3
Using /dev/sda
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) print
Model: VMware Virtual disk (scsi)
Disk /dev/sda: 537GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:

Number  Start   End     Size    File system  Name  Flags
 1      1049kB  2097kB  1049kB                     bios_grub
 2      2097kB  1076MB  1074MB  ext4
 3      1076MB  537GB   536GB

(parted) print free
Model: VMware Virtual disk (scsi)
Disk /dev/sda: 537GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:

Number  Start   End     Size    File system  Name  Flags
        17.4kB  1049kB  1031kB  Free Space
 1      1049kB  2097kB  1049kB                     bios_grub
 2      2097kB  1076MB  1074MB  ext4
 3      1076MB  537GB   536GB

(parted) quit
sudo pvscan
  PV /dev/sda3   VG ubuntu-vg       lvm2 [<199.00 GiB / 0    free]
  Total: 1 [<199.00 GiB] / in use: 1 [<199.00 GiB] / in no VG: 0 [0   ]
su
su          sudo        sudoedit    sudoreplay  sulogin     sum         suspend
su
su          sudo        sudoedit    sudoreplay  sulogin     sum         suspend
su
su          sudo        sudoedit    sudoreplay  sulogin     sum         suspend

sudo pvresize /dev/sda3
  Physical volume "/dev/sda3" changed
  1 physical volume(s) resized or updated / 0 physical volume(s) not resized

sudo pvscan
  PV /dev/sda3   VG ubuntu-vg       lvm2 [<499.00 GiB / 300.00 GiB free]
  Total: 1 [<499.00 GiB] / in use: 1 [<499.00 GiB] / in no VG: 0 [0   ]


sudo pvdisplay
  --- Physical volume ---
  PV Name               /dev/sda3
  VG Name               ubuntu-vg
  PV Size               <499.00 GiB / not usable 16.50 KiB
  Allocatable           yes
  PE Size               4.00 MiB
  Total PE              127743
  Free PE               76800
  Allocated PE          50943
  PV UUID               AEoQW4-KLnN-M8dm-qnFi-lnch-8IFC-Az2F5Y

sudo lvdisplay
  --- Logical volume ---
  LV Path                /dev/ubuntu-vg/ubuntu-lv
  LV Name                ubuntu-lv
  VG Name                ubuntu-vg
  LV UUID                ZNH5ug-qe1m-1IFc-JbNg-6qFk-hQzo-1CdZG4
  LV Write Access        read/write
  LV Creation host, time ubuntu-server, 2020-12-01 08:16:49 +0800
  LV Status              available
  # open                 1
  LV Size                <199.00 GiB
  Current LE             50943
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:0


sudo lvextend -l 127743 /dev/ubuntu-vg/ubuntu-lv
  Size of logical volume ubuntu-vg/ubuntu-lv changed from 300.00 GiB (76800 extents) to <499.00 GiB (127743 extents).
  Logical volume ubuntu-vg/ubuntu-lv successfully resized.

sudo resize2fs /dev/ubuntu-vg/ubuntu-lv
resize2fs 1.45.5 (07-Jan-2020)
Filesystem at /dev/ubuntu-vg/ubuntu-lv is mounted on /; on-line resizing required
old_desc_blocks = 38, new_desc_blocks = 63
The filesystem on /dev/ubuntu-vg/ubuntu-lv is now 130808832 (4k) blocks long.

df -h
Filesystem                         Size  Used Avail Use% Mounted on
udev                               3.9G     0  3.9G   0% /dev
tmpfs                              797M  1.3M  795M   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv  491G   79G  392G  17% /
tmpfs                              3.9G     0  3.9G   0% /dev/shm
tmpfs                              5.0M     0  5.0M   0% /run/lock
tmpfs                              3.9G     0  3.9G   0% /sys/fs/cgroup
/dev/sda2                          976M  300M  610M  33% /boot
/dev/loop0                          56M   56M     0 100% /snap/core18/2074
/dev/loop1                          56M   56M     0 100% /snap/core18/2128
/dev/loop2                          62M   62M     0 100% /snap/core20/1169
/dev/loop5                          71M   71M     0 100% /snap/lxd/21029
/dev/loop4                          62M   62M     0 100% /snap/core20/1081
/dev/loop3                          33M   33M     0 100% /snap/snapd/13640
/dev/loop6                          33M   33M     0 100% /snap/snapd/13270
/dev/loop7                          68M   68M     0 100% /snap/lxd/21545
overlay                            491G   79G  392G  17% /var/lib/docker/overlay2/8bfc3f8b85adb329a1a68550ff4dabb5353a36a1c6d3896347864e2936c22e94/merged
overlay                            491G   79G  392G  17% /var/lib/docker/overlay2/9754c6749d64f7483994dcf573b5e76207a2bea44e9de0b2f6f1224eb1293771/merged
shm                                 64M     0   64M   0% /var/lib/docker/containers/1d43bba5e9174ff5180fc5bd00565d0287b0f3ba6cd7d54795b15db8785c7e47/mounts/shm
tmpfs                              797M     0  797M   0% /run/user/1000
```