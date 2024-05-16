#VLM #arXiv2023 #ChatBot

[THUDM/CogVLM: a state-of-the-art-level open visual language model | 多模态预训练模型 (github.com)](https://github.com/THUDM/CogVLM)
![[Pasted image 20240515111746.png]]

我们介绍了CogVLM，一个强大的开源视觉语言基础模型。与将图像特征映射到语言模型的输入空间的流行的浅层对齐方法不同，CogVLM通过在注意力和FFN层中引入可训练的视觉专家模块来弥合冻结的预训练语言模型和图像编码器之间的差距。因此，CogVLM能够在不牺牲任何NLP任务性能的情况下实现视觉语言特征的深度融合。CogVLM-17B在17个经典的跨模态基准上取得了最先进的性能，包括1）图像字幕数据集：NoCaps、Flicker30k，2）VQA数据集：OKVQA、TextVQA、OCRVQA、ScienceQA，3）LVLM基准：MMVet、MMBench、SEED-Bench、LLaVABench、POPE、MMMU、MathVista，4）视觉定位数据集：RefCOCO、RefCOCO+、RefCOCOg、Visual7W。代码和检查点可在[https://github.com/THUDM/CogVLM获得。](https://github.com/THUDM/CogVLM%E8%8E%B7%E5%BE%97%E3%80%82)

## Introduction 

视觉语言模型是多才多艺且强大的。许多视觉和跨模态任务可以被制定为下一个令牌预测，例如图像字幕(Agrawal et al., 2019)、视觉问答(Antol et al., 2015)、视觉定位(Yu et al., 2016)甚至分割(Chen et al., 2022a)。有用的能力，如上下文学习(Tsimpoukelli et al., 2021; Sun et al., 2023a; Alayrac et al., 2022)，也随着VLM的扩展而出现，当扩展VLM时，下游任务的改进也随之而来。然而，训练一个大型语言模型已经不是一件简单的事情了，使用相同的NLP性能从头开始训练一个VLM更具挑战性。因此，研究如何从现成的预训练语言模型中训练VLM是很自然的。

流行的浅层对齐方法，如 [[InstructBLIP]] (Li et al., 2023b)和 [[MiniGPT-4]] (Zhu et al., 2023)，通过一个可训练的Q-Former或线性层将冻结的预训练视觉编码器和语言模型连接起来，将图像特征映射到语言模型的输入嵌入空间。这种方法收敛迅速，但其性能明显低于具有可训练语言参数的LLaVA-1.5，尽管它们的模型大小和训练数据集几乎相同。

在VLM中浅层对齐方法的性能主要挑战可以归因于视觉和语言数据之间缺乏深度融合。浅层对齐方法的困难在于它们依赖于“冻结”的语言模型权重，这些权重本质上是训练用于处理文本标记的。这导致了显著的不匹配。