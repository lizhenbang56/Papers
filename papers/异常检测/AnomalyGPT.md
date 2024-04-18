---
Publish: AAAI2024
Year: "2023"
Month: "08"
文档链接: "[[2308.15366 AnomalyGPT.pdf]]"
代码: https://github.com/CASIA-IVA-Lab/AnomalyGPT
Stars: "523"
I-AUROC-MVTecAD-4shot: "96.3"
创新点: 基于多模态大模型和上下文学习进行异常检测（会不会计算效率太低了？）
---
```mermaid
graph LR;
	AnomalyGPT-->上下文学习InContextLearning;
	AnomalyGPT-->图像编码器用于提取图像特征向量-->ImageBind-Huge;
	AnomalyGPT-->图像解码器分为4个阶段;
	AnomalyGPT-->LLM-->Vicuna-7B;
```
#### Related Work
##### Industrial Anomaly Detection
- Reconstruction-based methods
	- [[RIAD]]
	- [[SCADN]]
	- [[InTra]]
	- [[AnoDDPM]]
- Feature embedding-based methods
	- [[PatchSVDD]]
	- [[Cflow-AD]]
	- [[PyramidFlow]]
	- [[PatchCore]]
	- [[CFA]]
#### Method
##### Model Architecture
一幅查询图像：$x\in \mathbb{R}^{H\times W\times C}$
图像特征向量：$F_{img} \in \mathbb{R}^{C_1}$
将图像特征向量送入线性层得到图像嵌入：$E_{img} \in \mathbb{R}^{C_{emb}}$，被送入 LLM