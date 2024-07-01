## 进行压力测试

一开始打算在一个台式机上连接服务器进行压力测试，结果台式机和服务器的带宽达到上限，无法准确反映CTID的性能，因此改为直接在服务器上进行压力测试，对应命令如下：

```bash
bin/jmeter.sh -n -t /home/lhb/algo/jmx/sjzl3-face-localhost.jmx -l /home/lhb/algo/jmx-report/sjzl3-face/2024040317041712135341/log.log -e -o /home/lhb/algo/jmx-report/sjzl3-face/2024040317041712135341
```

压力测试持续时间为 48h，希望运行结束后能够生成测试报告，但是 log 文件超过 30 GB，导致服务器磁盘空间满了， jmeter 程序崩溃。
## 根据 log 生成报告

log 文件很大，有数十 GB。使用 `jmeter -g` 命令根据 log 文件生成报告。但是报错：

```
F:\zhbli\apache-jmeter-5.5>.\bin\jmeter.bat -g C:\Users\root\Desktop\face-feature\log.log -o C:\Users\root\Desktop\face-feature-report
java.lang.OutOfMemoryError: Java heap space
Dumping heap to java_pid14532.hprof ...
Heap dump file created [1009297342 bytes in 1.054 secs]
An error occurred: Java heap space
errorlevel=1
```

解决方案：新健 setenv.bat，内容如下。

```bash
set HEAP='-Xmx5g -Xms5g -XX:MaxMetaspaceSize=300m'  # Xms 的含义是：为 Java 虚拟机分配的最小内存。Xmx 的含义是：为 Java 虚拟机分配的最大内存
```

然后再正常执行命令即可：

```bash
F:\zhbli\apache-jmeter-5.5>.\bin\jmeter.bat -g C:\Users\root\Desktop\face-feature\log.log -o C:\Users\root\Desktop\face-feature-report
```