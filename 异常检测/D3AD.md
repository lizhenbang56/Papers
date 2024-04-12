---
Year: "2024"
Month: "01"
文档链接: "[[arXiv2401_D3AD.pdf]]"
标题: "D3AD: Dynamic Denoising Diffusion Probabilistic Model for Anomaly Detection"
Publish: arXiv
---

#### D3AD: Dynamic Denoising Diffusion Probabilistic Model for Anomaly Detection

[[arXiv2401_D3AD.pdf]]
本文基于扩散模型解决异常检测问题。
创新点：对于一个测试样本，在训练样本中搜索最近邻。
#### 扩散模型
扩散模型执行 $T$ 步的去噪过程，初始为随机噪声，每执行一步，噪声逐渐减少，直至生成一幅人类可理解的图像。

#### Bin Construction
$b\in B$
对于数据点 $\boldsymbol{x}_0 \in \mathcal{X}_{Train}$，进行特征提取得到 $\boldsymbol{y}_0=\phi(x_0)$，其中 $\boldsymbol{y}_0 \in Y_{Train}$
#### Dynamic Implicit Conditioning (DIC)
最大隐式条件水平 $T_{max} \in \{1,\cdots, T\}$，是一个标量。
DIC是一个函数 $g(\boldsymbol{x}_0, \mathcal{X}_{Train}, T_{max})$
DIC模块的输出：动态时间步/动态噪声步 $\hat{T} = \frac{b}{|B|}T_{max}$
#### Dynamic Reconstruction
根据 DIC 得到 $\hat T$
对 $\boldsymbol{x}_0$ 的特征 $\boldsymbol{z}_0$ 进行缩放：$\boldsymbol{z}_{\hat{T}} = \sqrt{\bar{\alpha}_{\hat{T}}} \cdot \boldsymbol{z}_0$ 

#### References
[[PaDiM]]
[[Anomaly detection via reverse distillation from one-class embedding]]
[[DDAD]]

## 5 EXPERIMENTS

### Datasets

我们采用两个广泛使用的基准数据集来评估我们方法的准确性，即 [[VisA]]（Zou等人，2022年）和BTAD（Mishra等人，2021年）数据集。VisA数据集包含10,821张高分辨率RGB图像，分为9,621个常规实例和1,200个异常实例。该数据集提供了全面的注释，包括图像级和像素级标签。数据集包括12个不同类别，具有各种规模和类型的异常。BTAD数据集包含展示三种独特工业产品的RGB图像。总共有2540张图片，其中每张异常图片都与一个像素级地面真实掩膜配对。
