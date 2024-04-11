- [[Long-Tailed Anomaly Detection with Learnable Class Names.pdf]]
- CVPR2024
- Long-Tailed Anomaly Detection with Learnable Class Names
- [Long-Tailed Anomaly Detection (LTAD) Dataset (zenodo.org)](https://zenodo.org/records/10854201)
	- 数据集
### Introduction
两类异常检测方法：
1. 为每个类别训练一个模型：single class AD
2. 一个模型处理所有类别：multi-class AD

两类异常检测方法：
1. AD by reconstruction methods：重建正常图像
2. semantic AD methods：显式训练正常/异常二分类器
### Related Work
#### Long-tailed recognition
现有的长尾识别算法分为三类：
1. data re-sampling
2. loss re-weighting
3. representation learning
### Long-tailed anomaly detection
以往的异常检测工作通常假设不同的图像类别具有相同的样本数量。广泛的研究，如分类领域，表明没有考虑这种类别不平衡的系统倾向于在流行类别上过拟合，而忽视不流行的类别。为了测试这是否也适用于异常检测，我们使用MVTec数据集和通过图像重采样得到的长尾版本进行了一些初步实验。
### The LTAD anomaly score
#### AD by reconstruction
重构模块：$\Pi(\cdot)$
输入图像的特征：$\{p_i\}_{i=1}^{W_1 \times H_1}$，是重构模块的输入
异常得分：$\mathcal{S}_{rec}(p_i) = ||\Pi(p_i) - p_i||^2$
#### Semantic AD (SAD)
#### LTAD score
$\mathcal{S}(p_i, c) = \mathcal{S}_{rec}(p_i) + \lambda \mathcal{S}_{sem}(p_i, c)$
### 参考文献
[[CPR]]