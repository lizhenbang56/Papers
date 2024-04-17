---
Publish: arXiv2024
Year: "2024"
创新点: 使用扩散模型BLDM生成异常样本
Title: A Novel Approach to Industrial Defect Generation through Blended Latent Diffusion Model with Online Adaptation
I-AUROC-MVTecAD单类无监督: "?"
---


- [[2402.19330 A Novel Approach to Industrial Defect Generation through Blended Latent Diffusion Model with Online Adaptation.pdf]]
- [GrandpaXun242/AdaBLDM: The implement for paper : "A Novel Approach to Industrial Defect Generation through Blended Latent Diffusion Model with Online Adaptation" (github.com)](https://github.com/GrandpaXun242/AdaBLDM)
	- 21 stars
### Abstract
使用扩散模型BLDM生成异常样本。
### RELATED WORK
#### Synthetic Defect Generation
- 不基于GAN/扩散模型
	- [[DRAEM]]
	- [[DeSTseg]]
	- [[MegSeg]]
	- [[ReSynthDetect]]
- 基于GAN/扩散模型
	- [[SDGAN]]
	- [[Defect-GAN]]
#### Diffusion Probabilistic Models for Image Editing
- RePaint
- DCFace

## 摘要

有效解决工业异常检测（AD）挑战需要充足的缺陷样本，而这在工业环境中往往受到稀缺的制约。本文介绍了一种新颖的算法，旨在增强缺陷样本，从而提高AD性能。所提出的方法定制了混合潜在扩散模型用于缺陷样本生成，采用扩散模型在潜在空间中生成缺陷样本。由“trimap”掩码和文本提示控制的特征编辑过程，精细化生成的样本。图像生成推理过程分为三个阶段：自由扩散阶段、编辑扩散阶段和在线解码器适应阶段。这种复杂的推理策略产生了高质量的合成缺陷样本，具有多样的模式变化，从而基于增强的训练集显著提高了AD准确性。具体来说，在广泛认可的MVTec AD数据集上，所提出的方法将基于增强数据的AD最新技术(SOTA)性能提高了1.5%、1.9%和3.1%，分别为AD指标AP、IAP和IAP90。本文的实现代码可以在GitHub存储库[https://github.com/GrandpaXun242/AdaBLDM.git中找到。](https://github.com/GrandpaXun242/AdaBLDM.git%E4%B8%AD%E6%89%BE%E5%88%B0%E3%80%82)

索引术语—异常检测、混合潜在扩散模型、在线适应。 

## I. 引言 

在实际的制造工作流程中，获取缺陷样本比获取无缺陷样本要困难得多。因此，最近提出的大多数工业缺陷检测算法，如[1]–[10]，将该问题视为异常检测（AD）问题——一个已经确立的机器学习挑战[11]，[12]。在这些工业AD算法中，假设所有无异常样本，无论是完整图像还是图像补丁，都属于单一分布。与此同时，将缺陷样本识别为“异常值”。采用异常检测方法进行工业缺陷检测的战略选择是明显的：在训练阶段不需要缺陷样本，这使得这些基于AD的算法与实际的制造场景兼容。

然而，实现这种兼容性的同时要付出极度不平衡的数据分布的代价，这一特征在大多数判别式算法的背景下被认为是不可接受的。因此，一些研究人员建议使用传统方法[1]，[3]，[5]来生成人造缺陷模式，以促进后续的判别式学习过程。最近的最新技术(SOTA)算法[13]–[15]表明，在训练阶段结合一些真实的异常样本可以显著提高AD准确性，如果这些样本与合成样本结合使用。例如，一些开创性的作品[16]，[17]展示了使用更复杂的方法生成这些“逼真”的缺陷的好处。图I的前两行说明了两种不同类型的缺陷生成。

本文提出将尖端人工智能生成算法——扩散概率模型（DPM）[18]，融入到缺陷生成领域中。具体地，我们利用混合潜在扩散模型[19]–[21]来创建我们的框架。为了增强缺陷样本的生成，我们创新地将混合潜在扩散模型（BLDM）[21]分为三个模块。首先，我们设计了一个新颖的“缺陷trimap”来描绘生成图像上的目标对象掩码和缺陷区域，并将其作为控制信息的新形式与稳定扩散模型内的语言提示一起结合使用。其次，为了确保生成样本的真实性，在BLDM中引入了级联的“编辑”阶段，分别在潜在空间和像素空间进行。最后，提出了一种创新的在线适应图像编码器的方法，以提高生成图像的质量。因此，定制的BLDM算法，在本文中称为AdaBLDM，能够生成具有模式变化的高质量缺陷样本。图I的第三行简要说明了基于BLDM的所提出的方法。总之，本文的贡献如下所述。

• 就我们所知，这是首次将扩散模型用于工业缺陷生成任务。BLDM的优势，如生成稳定性、高图像质量和可控内容，都有助于与SOTA方法相比获得更好的缺陷生成器。 
• 为了将BLDM算法定制为缺陷生成场景，我们在控制信息、预热阶段和在线适应方面完善了BLDM。这一努力导致了所提出的算法AdaBLDM，与现有SOTA方法生成的合成样本相比，能够获得显著改进的缺陷样本。 
• 在利用所提出的方法生成的缺陷样本的基础上，我们在MVTec AD数据集[22]上取得了新的SOTA性能。具体来说，所提出的AdaBLDM在AD指标AP、IAP和IAP90上分别比迄今最佳方法DeSTseg[6]提高了1.5%、1.9%和3.1%。

本文的其余部分安排如下。在第二节中，我们讨论了文献中的相关工作。第三节详细介绍了所提出的方法。实验结果和消融研究在第四节中讨论。我们在第五节总结本文。

### E.在线解码器调整 

考虑到合成的有缺陷样本的图像质量可能会受到图像解码器Φ(·)的显著影响，我们建议为每个生成的样本微调解码器。一旦从算法1中获得了混合的潜在特征z∗NG∈RHz×Wz×Cz，并且给定了有缺陷的掩模M∗NG∈B Hx×Wx和源图像xOK∈RHx×Wx×3，则我们可以通过进行在线更新算法来微调解码器模型Φ(·)，该算法如算法2所述，显示出在线适应策略鼓励解码器Φ(·)生成组装到xOK的无缺陷像素，并同时输出由原始解码器引导的有缺陷像素。保守比例λcon平衡了两个目标。在本文的实验中，我们证明了这种在线更新的解码器可以为AD训练生成更逼真的样本，从而导致更高的AD性能。