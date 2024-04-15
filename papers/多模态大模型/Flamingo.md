[[2204.14198 Flamingo.pdf]]
#### 术语英汉对译
Few-Shot In-Context Learning：小样本上下文学习
Few-Shot Adaption：小样本适应
In-Context Examples：上下文示例
#### Related work
##### Language modelling and few-shot adaptation
执行小样本适应的方法有：
1. 增加小的适应模块
2. 微调LLM的一小部分
3. 在提示中展示上下文示例
4. 通过梯度下降优化提示

```mermaid
graph TD;
	Flamingo-->基础模型是Chinchilla;
	Flamingo-->本文收集了一个数据集-->M3W数据集;
	Flamingo-->图文对数据集-->ALIGN数据集-->18亿个图文对;
	图文对数据集-->本文收集的图文对数据集-->LTIP-->3.12亿个图文对;
	本文收集的图文对数据集-->VTP-->视频文本对数据集;
	VTP-->2700万短视频;
	VTP-->视频平均长度22秒;
```