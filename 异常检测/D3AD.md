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
[[Anomaly Detection with Conditioned Denoising Diffusion Models]]