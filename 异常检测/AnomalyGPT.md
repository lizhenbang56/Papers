- [[2308.15366 AnomalyGPT.pdf]]
- [CASIA-IVA-Lab/AnomalyGPT: [AAAI 2024 Oral] AnomalyGPT: Detecting Industrial Anomalies Using Large Vision-Language Models (github.com)](https://github.com/CASIA-IVA-Lab/AnomalyGPT)
- AAAI2024
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