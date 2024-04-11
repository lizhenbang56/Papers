- [[2011.10678 Open-Vocabulary Object Detection Using Captions.pdf]]
- [alirezazareian/ovr-cnn: A new framework for open-vocabulary object detection, based on maskrcnn-benchmark (github.com)](https://github.com/alirezazareian/ovr-cnn)
	- 209 stars
#### Introduction
目标词汇（目标类别）：$\mathcal{V}_T$，是一个集合，集合中的元素是单词（word）。用于测试。
基础词汇（基础类别）：$\mathcal{V}_{B}$，用于训练。
全部词汇：$V_{\Omega}$
#### Experiments
##### Data and metrics
训练：COCO 2017 目标检测数据集的训练集。
评估：COCO 2017 目标检测数据集的验证集。
划分成48个基础类别和17个目标类别。