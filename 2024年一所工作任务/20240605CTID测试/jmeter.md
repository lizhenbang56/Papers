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