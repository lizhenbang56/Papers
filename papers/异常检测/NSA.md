---
创新点: 使用 Cut-Paste 方法生成异常图像
Publish: ECCV2022
Year: "2021"
Month: "09"
合成异常的方式: 将泊松图像编辑与缩放其他正常图像中各种大小的正常补丁无缝融合
监督方式: 无监督
标题: Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization
Citation: "55"
文档链接: "[[2109.15222 NSA.pdf]]"
代码: github.com/hmsch/natural-synthetic-anomalies
Stars: "38"
方法类别: 基于合成
类别数: 单类
I-AUROC-MVTecAD单类无监督: "97.2"
P-AUROC-MVTecAD单类无监督: "96.3"
---

- 使用 Cut-Paste 方法生成异常样本。——[[AnomalyGPT]]
### Related Work
#### Reconstruction-based anomaly detection
由于使用正常样本训练，所以希望模型不会重建异常区域。
#### Embedding-based anomaly detection
