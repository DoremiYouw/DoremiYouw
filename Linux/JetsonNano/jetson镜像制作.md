# 制作镜像

[参考文献](https://zhuanlan.zhihu.com/p/446999714)

1. 下载安装vmware虚拟机软件
2. 安装ubuntu虚拟机（[清华源](https://mirrors.tuna.tsinghua.edu.cn/ubuntu-releases/18.04/)）
3. 下载L4T Driver Package (BSP)以及Sample Root Filesystem([官方](https://developer.nvidia.cn/embedded/l4t-3231-archive))
4. 在虚拟机中解压两个文件
5. 下载([文件](https://forums.developer.nvidia.com/uploads/short-url/iRzK9h6r9FOJYkclcaRxIiwWZye.gz))并替换Linux_for_Tegra/bootloader/nvtboot_recovery.bin文件，记得改名
6. 在Linux_for_Tegra目录下，拷贝NVIDIA 库文件到文件系统
   `sudo ./apply_binaries.sh`
7. 将待复制的jetson设备进入恢复模式（先用跳帽短接GND和REC，再通电），用数据线连接jetson设备和虚拟机（lsusb中出现NVidia Corp）
8. 如果出现‘python’: No such file or directory ，执行:
   `sudo ln -s /usr/bin/python3 /usr/bin/python`
9. 在Linux_for_Tegra目录下执行指令，备份镜像到backup.img:
    `sudo ./flash.sh -r -k APP -G backup.img jetson-nano-emmc mmcblk0p1`
10. 将生成的backup.img以及backup.img.raw，将两个文件复制到bootloader文件夹下并分别重命名为system.img以及system.img.raw
```ruby
cp backup.img bootloader/system.img 
cp backup.img.raw bootloader/system.img.raw
```

# 镜像恢复

1. 将待恢复的新jetson设备进入恢复模式，用数据线连接jetson设备和虚拟机
2. 在Linux_for_Tegra目录下执行如下指令，将刚刚生成的镜像复制到新的jetson设备：
   `sudo ./flash.sh -r jetson-nano-emmc mmcblk0p1`
