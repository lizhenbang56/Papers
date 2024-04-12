---
Publish: ECCV2022
Year: "2022"
Month: "07"
文档链接: https://arxiv.org/pdf/2207.14315.pdf
代码: https://github.com/amazon-science/spot-diff
Stars: "108"
---
## 摘要

视觉异常检测通常用于工业质量检验。在本文中，我们提出了一个新的数据集以及一种新的自监督学习方法，用于ImageNet预训练，以改进1类和2类5/10/high-shot 训练设置中的异常检测和分割。我们发布了包含10,821张高分辨率彩色图像（9,621张正常样本和1,200张异常样本）的Visual Anomaly（VisA）数据集，涵盖了3个领域中的12个对象，使其成为迄今为止最大的工业异常检测数据集。提供图像和像素级标签。我们还提出了一个新的自监督框架 - SPot-the-difference（SPD），它可以使对比度自监督预训练，如SimSiam、MoCo和SimCLR等，更适合于异常检测任务。我们在VisA和MVTec-AD数据集上的实验表明，SPD始终改善了这些对比度预训练基线，甚至是监督预训练。例如，在 2类 high-shot 设置中，SPD分别比SimSiam和监督预训练提高了5.9%和6.8%的异常分割精度-召回曲线（AU-PR）。我们在http://github.com/amazon-research/spot-diff上开源了该项目。