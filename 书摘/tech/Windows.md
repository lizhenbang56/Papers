## WSL

### 子系统瘦身

```powershell
//进入 powershell

wsl.exe --list --verbose  // 查看子系统名称
wsl.exe --terminate 子系统名称
diskpart  // 在新窗口中启动diskpart

//进入 diskpart
select vdisk file="D:\apps\wsl-ubuntu18.04\ext4.vhdx"
compact vdisk  // 133.1GB->79.8GB
```

### 子系统迁移

```powershell
// 进入 powershell
wsl -l -v  //显示<子系统名称>、<运行状态>、<子系统版本号>

//如果Running<运行状态>，关掉它
wsl --shutdown

//导出系统镜像
wsl --export <子系统名称> <tar文件路径>

//注销原有的linux子系统
wsl --unregister <子系统名称>

//可以再查看是否注销：
wsl -l -v

//导入子系统
wsl --import <子系统名称> <新路径(不能有空格)> <tar文件路径> --version 子系统版本号
```