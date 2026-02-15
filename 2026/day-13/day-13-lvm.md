## Command Used ##
pvcreate /dev/sdb   # or your loop device
pvs
vgcreate devops-vg /dev/sdb
vgs
lvcreate -L 500M -n app-data devops-vg
lvs
mkfs.ext4 /dev/devops-vg/app-data
mkdir -p /mnt/app-data
mount /dev/devops-vg/app-data /mnt/app-data
df -h /mnt/app-data
lvextend -L +200M /dev/devops-vg/app-data
resize2fs /dev/devops-vg/app-data
df -h /mnt/app-data


What you learned (3 points)
1) learn how to mount the external disk
2) learned how to extend disk
3) learn about volume in AWS
