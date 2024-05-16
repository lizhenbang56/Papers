## 子系统瘦身

```powershell
//进入 powershell

wsl.exe --list --verbose  // 查看子系统名称
wsl.exe --terminate 子系统名称
diskpark  // 在新窗口中启动diskpart

//进入diskpark
select vdisk file="D:\apps\wsl-ubuntu18.04\ext4.vhdx"
compact vdisk  // 133.1GB->79.8GB
```