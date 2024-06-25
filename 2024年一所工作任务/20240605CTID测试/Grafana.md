## 安装

运行 `smi` 安装包。

复制 `C:\Program Files\GrafanaLabs\grafana\conf\sample.ini` 到 `custom.ini`

将 `custom.ini` 中的 `;http_port = 3000` 改为 `http_port = 8080`

在命令行进入路径 `C:\Program Files\GrafanaLabs\grafana\bin` 并运行 `.\grafana-server.exe` 

## 浏览器界面

- 在浏览器访问 http://localhost:9090
- 用户名：admin 密码：admin
- 配置数据源：Connections -> Data sources -> Add data source -> Prometheus
- Dashboards -> Create Dashboard -> Import dashboard -> 11074