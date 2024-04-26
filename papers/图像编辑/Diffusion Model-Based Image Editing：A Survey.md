---
Title: "Diffusion Model-Based Image Editing: A Survey"
Publish: arXiv2024
Year: "2024"
Month: "02"
Url: https://arxiv.org/pdf/2402.17525
---
表1给出了详尽的图像编辑文章。

图像编辑的 3 种类型
- 语义编辑
	- 目标添加
	- 目标移除
	- 目标替换
	- 背景改变
	- 情感表达修改
- 风格编辑
- 结构编辑

图像编辑的 10 种不同输入：
- 文本
- 蒙版
- 参考 (Ref.) 图像
- 类别
- 布局
- 姿势
- 草图
- 分割 (Seg.) 映射
- 音频
- 拖动点
### 基于扩散模型的图像编辑：一项调查

黄毅∗，黄建成∗，刘一帆∗，闫明复∗，吕佳希∗，刘建壮∗，IEEE 高级会员，

熊伟，张赫，陈仕峰，曹亮亮，IEEE 高级会员

摘要——去噪扩散模型已成为各种图像生成和编辑任务的强大工具，以无条件或输入条件的方式促进视觉内容的合成。它们背后的核心理念是学习逆转逐渐向图像添加噪声的过程，从而使它们能够从复杂的分布中生成高质量的样本。在本调查中，我们全面概述了现有的使用扩散模型进行图像编辑的方法，涵盖了该领域的理论和实践方面。我们从多个角度对这些工作进行了深入的分析和分类，包括学习策略、用户输入条件和可以完成的特定编辑任务的范围。此外，我们特别关注图像修复和外推，并探索了早期传统的上下文驱动方法和当前的多模态条件方法，对其方法进行了全面的分析。为了进一步评估文本引导图像编辑算法的性能，我们提出了一个系统化的基准，即 EditEval，其特点是采用了一种创新的指标，即 LMM 分数。最后，我们讨论了当前的局限性，并展望了未来研究的一些潜在方向。随附的存储库发布在 [https://github.com/SiatMMLab/](https://github.com/SiatMMLab/) Awesome-Diffusion-Model-Based-Image-Editing-Methods。

索引词——扩散模型，图像编辑，AIGC

1 引言

在人工智能生成内容 (AIGC) 领域，人工智能被用于创建和修改数字内容，图像编辑被认为是一个重要的创新和实际应用领域。与图像生成不同，图像编辑涉及改变图像的外观、结构或内容，包括从细微调整到重大转换的一系列变化。这项研究是数字媒体、广告和科学研究等各个领域的基础，在这些领域中，改变视觉内容至关重要。图像编辑的演变反映了数字技术的进步，从手动、劳动密集型的过程发展到由基于学习的算法驱动的先进数字技术。这一演变的一个关键进步是引入了生成对抗网络 (GAN) [1]–[6]，它极大地增强了创意图像处理的可能性。

最近，AIGC 中出现了扩散模型 [1]、[7]–[15]，导致视觉生成任务取得了显著突破。扩散模型的灵感来自非平衡热力学原理 [15]，其工作原理是逐渐向数据添加噪声，然后学习逆转从随机噪声开始的过程，直到生成与源数据分布匹配的所需数据。它们可以大致分为基于去噪扩散的 [15]–[18] 和基于分数匹配的 [19]–[23]。它们的适应性和有效性导致了在各种任务中的广泛应用，如图像生成 [24]–[38]、视频生成 [39]–[56]、图像恢复 [57]–[71] 和图像编辑。

扩散模型在图像编辑中的应用引起了人们的极大兴趣，近年来该领域大量研究出版物证明了这一点。这种日益增长的关注突出了扩散模型在提高图像编辑性能方面的潜力和多功能性，使其优于以往的工作。鉴于这一重大进展，系统地审查和总结这些贡献至关重要。然而，现有的关于扩散模型的调查文献集中于其他特定的视觉任务 [72]–[75]，如视频应用 [73] 或图像恢复和增强 [74]、[75]。一些提到图像编辑的调查往往只提供粗略的概述 [76]–[83]，缺乏对这些方法的详细和集中探索。

为了弥合这一差距，我们进行了一项调查，提供了一个深入而全面的分析，特别关注图像编辑。我们深入研究了该领域中扩散模型的方法、输入条件和广泛的编辑任务。该调查批判性地审查了 100 多篇研究论文，根据学习策略将它们分为三个主要类别：
- 基于训练的方法
- 测试时微调方法
- 无需训练和微调的方法

每个类别根据其核心技术进一步细分，第 4、5 和 6 节分别详细讨论了这些技术。我们还探讨了这些方法中使用的 **10 种不同类型的输入条件，包括文本、蒙版、参考 (Ref.) 图像、类别、布局、姿势、草图、分割 (Seg.) 映射、音频和拖动点**，以显示扩散模型在各种图像编辑场景中的适应性。

此外，我们的调查提出了一个新的图像编辑任务分类，分为三个大类，即：
- 语义编辑
- 风格编辑
- 结构编辑

涵盖了 12 种特定类型。图 1 直观地表示了研究在学习策略、输入条件和编辑任务类别中的统计分布。此外，我们特别关注修复和外推，它们共同构成了一种独特的编辑类型。我们在第 7 节中探讨了早期传统方法和当前多模态条件方法，并对其方法进行了全面的分析。我们还介绍了 EditEval，这是一个旨在评估文本引导图像编辑算法的基准，详见第 8 节。特别是，通过利用大型多模态模型 (LMM) 的高级视觉语言理解能力，提出了一种有效的评估指标，即 LMM 分数。最后，我们在第 9 节中介绍了一些当前的挑战和潜在的未来趋势，并进行了展望。

总之，本调查旨在系统地分类和批判性地评估基于扩散模型的图像编辑的大量研究。我们的目标是提供一个全面的资源，不仅综合当前的研究成果，而且指导这一快速发展领域的未来研究方向。

## 2 背景

### 2.1 扩散模型

扩散模型对生成式 AI 领域产生了深远的影响，催生了大量属于其范畴的方法。从本质上讲，这些模型基于一个称为扩散的关键原则，它逐渐向某种分布的数据样本添加噪声，将其转换为预定义的典型简单分布（例如高斯分布），然后迭代地逆转此过程以生成与原始分布匹配的数据。扩散模型与早期生成模型的区别在于它们在迭代时间步长中的动态执行，涵盖了时间上的向前和向后移动。

对于每个时间步长 t，噪声潜变量 zt 描绘了当前状态。时间步长 t 在正向扩散过程中逐渐增加，而在逆向扩散过程中逐渐减小至 0。值得注意的是，文献中缺乏对正向扩散中的 zt 和逆向扩散中的 zt 的明确区分。在正向扩散的上下文中，令 zt ∼ q(zt|zt−1)，在逆向扩散中，令 zt−1 ∼ p(zt−1|zt)。在此，我们将 0 < t ≤ T 的 T 表示为有限情况下的最大时间步长。t = 0 时的初始数据分布由 z0 ∼ q(z0) 表示，缓慢地被添加到 z0 的噪声污染。扩散模型通过参数化模型 pθ(zt−1|zt) 在逆时间方向上逐渐消除噪声。该模型近似于理想的（尽管无法实现的）去噪分布 p(zt−1|zt)。正如 Ho 等人 [16] 中介绍的，去噪扩散概率模型 (DDPM) 有效地利用马尔可夫链来促进有限时间步长序列上的正向和逆向过程。正向扩散过程。此过程将数据分布转换为预定义的分布，例如高斯分布。转换表示为：

$q(z_t|z_{t-1}) = N(z_t|\sqrt{1-\beta_t}z_{t-1}, \beta_tI)$, (1)

其中超参数集 0 < β1:T < 1 表示在每个连续步骤中引入的噪声方差。正如 Sohl-Dickstein 等人 [15] 中详细阐述的，此扩散过程可以通过单步方程简要表示：

$q(z_t|z_0) = N(z_t|\sqrt{\bar{\alpha}_t}z_0, (1-\bar{\alpha}_t)I)$, (2)

其中 $α_t = 1 - β_t$ 且 $\bar{\alpha}t = \prod{i=1}^t α_i$。因此，zt 可以直接通过以下公式采样，而无需考虑中间时间步长：

$z_t = \sqrt{\bar{\alpha}_t} \cdot z_0 + \sqrt{1-\bar{\alpha}_t} \cdot \epsilon, \epsilon \sim N(0, I)$. (3)

逆向扩散过程。这里的主要目标是学习正向扩散过程的逆过程，目的是生成一个与原始未更改数据样本 z0 紧密对齐的分布。在图像编辑的上下文中，z0 表示编辑后的图像。实际上，这是通过使用 UNet 架构来学习 p 的参数化版本来实现的。假设正向扩散过程近似于 q(zT ) ≈ N(0, I)，则可学习过渡的公式表示为：

$p_\theta(z_{t-1}|z_t) = N(z_{t-1}|\mu_\theta(z_t, \bar{\alpha}t), \Sigma\theta(z_t, \bar{\alpha}_t))$, (4)

其中函数 µθ 和 Σθ 是可学习的参数。此外，对于以外部变量 c 为条件的条件公式 pθ(zt−1|zt, c)（在图像编辑中，c 可以是源图像），模型变为 µθ(zt, c, ᾱt) 和 Σθ(zt, c, ᾱt)。优化。指导逆向扩散以学习正向过程的优化策略涉及最小化正向和逆向序列的联合分布之间的 Kullback-Leibler (KL) 散度。这些在数学上定义为：

$p_\theta(z_0, ..., z_T) = p(z_T)\prod_{t=1}^T p_\theta(z_{t-1}|z_t)$, (5)

$q(z_0, ..., z_T) = q(z_0)\prod_{t=1}^T q(z_t|z_{t-1})$, (6)
  
导致最小化：

$KL(q(z_0, ..., z_T)||p_\theta(z_0, ..., z_T))$ (7)

$\geq E_{q(z_0)}[-\log p_\theta(z_0)] + c$,

Ho 等人 [16] 中详细介绍了这一点，常数 c 与优化 θ 无关。公式 7 中的 KL 散度表示数据对数似然 (log pθ(z0)) 的变分界。此 KL 散度用作损失，并在 DDPM 中最小化。实际上，Ho 等人 [16] 采用此损失的重新加权版本作为更简单的去噪损失：

$E_{t\sim U(1,T),z_0\sim q(z_0), \epsilon \sim N(0,I)}[\lambda(t)||\epsilon - \epsilon_\theta(z_t, t)||^2]$, (8)

其中 λ(t) > 0 表示加权函数，zt 使用公式 3 获得，εθ 表示一个网络，旨在根据 zt 和 t 预测噪声 ε。DDIM 采样和反演。在处理真实图像 z0 时，流行的编辑方法 [84]、[85] 首先使用特定的反演方案将此 z0 反演为相应的 zT。随后，采样从此 zT 开始，采用某种编辑策略来生成编辑后的结果 z̃0。在理想情况下，直接从 zT 采样（不进行任何编辑）应该会产生与 z0 非常相似的 z̃0。z̃0 与 z0 的显着偏差（称为重建失败）表示编辑后的图像无法保持 z0 中未更改区域的完整性。因此，使用确保 z̃0 ≈ z0 的反演方法至关重要。

DDIM 采样方程 [18] 为：

$z_{t-1} = \sqrt{\bar{\alpha}{t-1}}z_t - \sqrt{1-\bar{\alpha}t}\epsilon\theta(z_t, t)\sqrt{\bar{\alpha}t} + \sqrt{1-\bar{\alpha}{t-1}}\epsilon\theta(z_t, t)$, (9)

或者表示为：

$z_t = \sqrt{\bar{\alpha}t}z{t-1} - \sqrt{1-\bar{\alpha}{t-1}}\epsilon\theta(z_t, t)\sqrt{\bar{\alpha}_{t-1}} + \sqrt{1-\bar{\alpha}t}\epsilon\theta(z_t, t)$. (10)

虽然公式 10 似乎提供了一种从 zt−1 到 zt 的理想反演，但问题在于 zt 的未知性质，它也用作网络 εθ(zt, t) 的输入。为了解决这个问题，DDIM 反演 [18] 在 zt−1 ≈ zt 的假设下运行，并将公式 10 右侧的 zt 替换为 zt−1，从而得到以下近似：

$z_t = \sqrt{\bar{\alpha}t}z{t-1} - \sqrt{1-\bar{\alpha}{t-1}}\epsilon\theta(z_{t-1}, t)\sqrt{\bar{\alpha}{t-1}} + \sqrt{1-\bar{\alpha}t}\epsilon\theta(z{t-1}, t)$.

(11) 文本条件和无分类器指导。文本条件扩散模型旨在合成由文本提示 P 引导的随机噪声 zT 的结果。在采样过程中的推理过程中，噪声估计网络 εθ(zt, t, C) 用于预测噪声 ε，其中 C = ψ(P) 表示文本嵌入。此过程在 T 步中系统地从 zt 中去除噪声，直到获得最终结果 z0。

在文本条件图像生成领域，确保对生成输出进行实质性的文本影响和控制至关重要。为此，Ho 等人 [86] 引入了无分类器指导的概念，这是一种将条件和无条件预测结合起来的技术。更具体地说，令 ∅ = ψ("")1 表示空文本嵌入。当与指导比例 w 结合使用时，无分类器指导预测形式化为：

$\epsilon_\theta(z_t, t, C, \emptyset) = w\epsilon_\theta(z_t, t, C) + (1-w)\epsilon_\theta(z_t, t, \emptyset)$. (12)

1. 占位符 ∅ 通常用于负面提示，以防止某些属性在生成的图像中出现。
    

在此公式中，εθ(zt, t, C,∅) 替换了采样公式 9 中的 εθ(zt, t)。w 的值（通常在 [1, 7.5] 范围内，如 [26]、[27] 中所建议的）决定了文本控制的程度。较高的 w 值与生成过程中更强的文本驱动影响相关。

### 2.2 相关任务

#### 2.2.1 条件图像生成

虽然我们的主要关注点是图像编辑中的扩散模型，但重要的是要了解相关领域，如条件图像生成。与涉及改变现有图像某些部分的图像编辑不同，条件图像生成是从头开始创建新图像，并以指定的条件为指导。早期的努力 [31]、[32]、[87]–[90] 通常涉及类别条件图像生成，这通常在采样过程中通过一个额外的预训练分类器结合类别诱导的梯度。然而，Ho 等人 [86] 引入了无分类器指导，它不依赖于外部分类器，并允许更通用的条件（例如文本）作为指导。文本到图像 (T2I) 生成。GLIDE [34] 是第一个使用文本直接从高维像素级别指导图像生成的工作，它取代了类别条件扩散模型中的标签。类似地，Imagen [27] 使用级联框架在像素空间中更高效地生成高分辨率图像。另一条研究路线首先将图像投影到低维空间，然后在该潜空间中应用扩散模型。代表性作品包括稳定扩散 (SD) [26]、VQ-diffusion [91] 和 DALL-E 2 [25]。在这些开创性研究之后，在过去的两年中，提出了大量工作 [37]、[92]–[97]，推动了该领域的发展。其他条件。除了文本之外，更具体的条件也用于在图像合成中实现更高的保真度和更精确的控制。GLIGEN [98] 在预训练的 T2I 扩散模型的每个块中原有的自注意力层和交叉注意力层之间插入了一个门控自注意力层，用于生成以地面框为条件的图像。Make-A-Scene [99] 和 SpaText [100] 使用分割蒙版来指导生成过程。除了分割映射之外，ControlNet [101] 还可以结合其他类型的输入，例如深度映射、法线映射、canny 边缘、姿势和草图作为条件。UniControlNet [102]、UniControl [103]、Composer [104] 和 T2I-Adapter [105] 等其他方法集成了各种条件输入，并包含额外的层，增强了由这些条件控制的生成过程。定制图像生成。在条件图像生成中与图像编辑密切相关的是创建个性化图像的任务。此任务专注于生成保持某种身份的图像，通常以同一主题的几个参考图像为指导。通过少样本图像解决此定制生成的两种早期方法是文本反演 [106] 和 DreamBooth [107]。具体来说，文本反演学习一个唯一的标识词来表示一个新主题，并将该词并入文本编码器的字典中。另一方面，Dream-Booth 通过使用一些参考图像微调整个 Imagen [27] 模型，将一个新的、罕见的词与特定主题绑定在一起。为了有效地组合多个新概念，CustomDiffusion [108] 仅优化稳定扩散 [26] 中的交叉注意力参数，表示新概念并对多概念组合进行联合训练。

在这些基础工作的基础上，后续方法 [109]–[117] 对生成的图像提供了更精细的控制，提高了输出的精度和准确性。

#### 2.2.2 图像恢复和增强

图像恢复 (IR) 是低级视觉中的一项关键任务，旨在提高受各种退化污染的图像的质量。扩散模型的最新进展促使研究人员调查它们在图像恢复方面的潜力。开创性工作将扩散模型集成到此任务中，超越了以前的基于 GAN 的方法。输入图像作为条件。生成模型对各种图像恢复任务做出了重大贡献，例如超分辨率 (SR) 和去模糊 [12]、[13]、[29]、[118]、[119]。通过重复细化进行超分辨率 (SR3) [57] 利用 DDPM 通过随机迭代去噪过程进行条件图像生成。级联扩散模型 [31] 采用多个扩散模型按顺序排列，每个模型生成分辨率越来越高的图像。SRDiff [118] 遵循 SR3 的紧密实现。SRDiff 和 SR3 之间的主要区别在于 SR3 直接预测目标图像，而 SRDiff 预测输入和输出图像之间的差异。非空间空间中的恢复。一些基于扩散模型的 IR 方法专注于其他空间。例如，Refusion [63]、[120] 采用均值回归图像恢复 (IR)-SDE 将目标图像转换为其退化对应物。它们利用自动编码器将输入图像压缩为其潜表示，并使用跳过连接来访问多尺度细节。Chen 等人 [121] 采用类似的方法，提出了一种称为层次集成扩散模型的两阶段策略。从空间域到小波域的转换是无损的，并提供了显着的优势。例如，WaveDM [67] 修改低频带，而 WSGM [122] 或 ResDiff [60] 相对于低分辨率图像调节高频带。BDCE [123] 设计了一种深度曲线空间中的自举扩散模型，用于高分辨率低光图像增强。T2I 先验使用。结合 T2I 信息 terbukti menguntungkan，因为它允许使用预训练的 T2I 模型。这些模型可以通过添加针对 IR 任务定制的特定层或编码器来进行微调。Wang 等人将这一概念付诸实践，提出了 StableSR [124]。StableSR 的核心是一个与冻结的稳定扩散模型 [26] 串联训练的时间感知编码器。此设置无缝集成了可训练的空间特征变换层，从而能够基于输入图像进行调节。DiffBIR [125] 使用预训练的 T2I 扩散模型进行盲图像恢复，具有两阶段管道和可控模块。CoSeR [126] 引入了认知超分辨率，融合了图像外观和语言理解。SUPIR [127] 利用生成先验、模型缩放和一个包含 2000 万张图像的数据集，用于由文本提示引导的 advanced 恢复，具有负质量提示和恢复引导的采样方法。基于投影的方法。这些方法旨在从输入图像中提取固有的结构或纹理，以在每个步骤中补充生成的图像并确保数据一致性。ILVR [65] 将低频信息从输入图像投影到输出图像，确保了数据一致性并建立了改进的条件。为了解决这个问题并增强数据一致性，一些最近的工作 [70]、[71]、[128] 采用了一种不同的方法，旨在使用贝叶斯定理估计后验分布。基于分解的方法。这些方法将 IR 任务视为线性逆问题。去噪扩散恢复模型 (DDRM) [66] 利用预训练的去噪扩散生成模型来解决线性逆问题，展示了在不同测量噪声水平下超分辨率、去模糊、修复和着色方面的多功能性。去噪扩散零空间模型 (DDNM) [68] 代表了另一种基于分解的零样本方法，适用于图像 SR 之外的各种线性 IR 问题，例如着色、修复和去模糊。它利用范围-零空间分解方法 [129]、[130] 有效地解决各种 IR 挑战。

## 3 图像编辑的分类

除了扩散模型在图像生成、恢复和增强方面取得的重大进步之外，它们还通过提供比先前占主导地位的 GAN 更强的可控性，在图像编辑方面取得了显著突破。与专注于从头开始创建新图像的图像生成以及旨在修复和提高退化图像质量的图像恢复和增强不同，图像编辑涉及修改现有图像的外观、结构或内容，包括添加对象、替换背景和改变纹理等任务。

在本调查中，我们根据学习策略将图像编辑论文分为三个主要类别：基于训练的方法、测试时微调方法以及无需训练和微调的方法，这些方法将在第 4、5 和 6 节中详细阐述。此外，我们探索了这些方法采用的 10 种输入条件来控制编辑过程，包括文本、蒙版、参考 (Ref.) 图像、类别、布局、姿势、草图、分割 (Seg.) 映射、音频和拖动点。此外，我们调查了可以通过这些方法完成的 12 种最常见的编辑类型，这些类型分为以下三个大类。

- 语义编辑：此类别包括对图像内容和叙事的更改，影响所描绘场景的故事、背景或主题元素。此类别中的任务包括添加对象 (Obj. Add.)、删除对象 (Obj. Remo.)、替换对象 (Obj. Repl.)、更改背景 (Bg. Chg.) 和修改情绪表达 (Emo. Expr. Mod.)。
    
- 风格编辑：此类别专注于增强或转换图像的视觉风格和美学元素，而不会改变其叙事内容。此类别中的任务包括更改颜色 (Color Chg.)、更改纹理 (Text. Chg.) 和整体风格更改 (Style Chg.)，包括艺术风格和现实风格。
    
- 结构编辑：此类别涉及图像中元素的空间排列、位置、视点和特征的变化，强调场景中对象的组织和呈现方式。此类别中的任务包括移动对象 (Obj. Move.)、更改对象大小和形状 (Obj. Size. Chg.)、更改对象动作和姿势 (Obj. Act. Chg.) 以及更改视角/视点 (Persp./View. Chg.)。
    

表 1 全面总结了调查论文的多视角分类，提供快速搜索功能。

## 4 基于训练的方法

在基于扩散模型的图像编辑领域，基于训练的方法获得了显著的关注。这些方法不仅以其对扩散模型的稳定训练和对数据分布的有效建模而著称，而且还以其在各种编辑任务中的可靠性能而著称。为了全面检查这些方法，我们根据它们的应用范围、训练所需的条件和监督类型将它们分为四个主要类别，如图 2 所示。此外，在这些主要类别中的每一个类别中，我们根据其核心编辑方法将方法分为不同的类型。这种分类说明了这些方法的范围，从有针对性的特定领域应用到更广泛的开放世界应用。

### 4.1 弱监督下的特定领域编辑

在过去的几年中，生成对抗网络 (GAN) 由于其生成高质量图像的能力，在图像编辑中得到了广泛的探索。然而，扩散模型凭借其先进的图像生成能力，成为该领域的新焦点。扩散模型的一个挑战是，当在大数据集上训练时，它们需要大量的计算资源。为了解决这个问题，早期的研究通过对较小的专门数据集进行弱监督来训练这些模型。这些数据集高度集中于特定领域，例如用于人脸处理的 CelebA [236] 和 FFHQ [2]、用于动物面部编辑和转换的 AFHQ [237]、用于对象修改的 LSUN [238] 以及用于风格迁移的 WikiArt [239]。为了彻底理解这些方法，我们根据它们的弱监督类型对它们进行组织。

CLIP 指导。受使用 CLIP [242] 进行文本引导图像编辑的基于 GAN 的方法 [240]、[241] 的启发，一些研究将 CLIP 纳入扩散模型。一个关键示例是 DiffusionCLIP [131]，它允许使用 CLIP 在训练过的和新的领域中进行图像处理。具体来说，它首先使用 DDIM 反演将真实图像转换为潜噪声，然后在逆向扩散过程中微调预训练的扩散模型，以调整受源文本提示和目标文本提示之间的 CLIP 损失约束的图像属性。Asyrp [132] 没有微调整个扩散模型，而是专注于内部的语义潜空间（称为 h 空间），它在其中定义了一个由小型神经网络参数化的额外隐函数。然后，它在 CLIP 损失的指导下训练网络，同时保持扩散模型冻结。图 3 显示了 DiffusionCLIP 和 Asyrp 的简化管道的视觉比较。为了解决 DiffusionCLIP 中多步优化耗时的问题，EffDiff [133] 引入了一种更快的单步训练和高效处理的方法。

除了上述方法主要关注的面部编辑之外，DiffStyler [134] 和 StyleDiffusion [135] 还针对艺术风格迁移。DiffStyler 使用 CLIP 指令损失来对齐目标文本描述和生成的图像，并使用 CLIP 美学损失来增强视觉质量。另一方面，StyleDiffusion 引入了一种基于 CLIP 的风格解耦损失，以改善风格内容的协调。

循环正则化。由于扩散模型能够进行域转换，因此在 CycleGAN [5] 等方法中常用的循环框架也在其中得到了探索。例如，UNIT-DDPM [136] 在扩散模型中定义了一个双域马尔可夫链，使用循环一致性来规范化非配对图像到图像转换的训练。类似地，CycleNet [137] 采用 ControlNet [101]，并使用预训练的稳定扩散 [26] 作为文本调节的主干。它还在整个图像转换周期中采用一致性正则化，该周期包括从源域到目标域的正向转换以及反向的逆向转换。

投影和插值。GAN [243]、[244] 中经常使用的另一种技术涉及将两个真实图像投影到 GAN 潜空间中，然后在它们之间进行插值以实现平滑的图像处理，这也被一些扩散模型用于图像编辑。例如，扩散自动编码器 [138] 引入了一个语义编码器，将输入图像映射到语义上有意义的嵌入，然后将其用作扩散模型进行重建的条件。在训练了语义编码器和条件扩散模型之后，可以将任何图像投影到此语义空间中进行插值。然而，HDAE [139] 指出，这种方法往往会遗漏丰富的低级和中级特征。它通过增强框架来解决这个问题，以分层方式利用语义编码器和基于扩散的解码器的从粗到细的特征，旨在获得更全面的表示。

分类器指导。一些研究通过引入额外的预训练分类器进行指导来增强图像编辑性能。例如，EGSDE [140] 使用能量函数来指导逼真的非配对图像到图像转换的采样。该函数由时间相关的特定领域分类器和低通滤波器分别指定的两个对数势函数组成。对于细粒度图像编辑，像素引导扩散 [141] 训练了一个像素级分类器，以估计分割映射并使用其梯度指导采样。

### 4.2 自监督下的参考和属性指导

这类工作从单个图像中提取属性或其他信息，作为以自监督方式训练基于扩散的图像编辑模型的条件。它们可以分为两种类型：基于参考的图像合成和属性控制的图像编辑。

基于参考的图像合成。为了学习如何合成图像，PbE [142] 以自监督方式进行训练，使用图像中对象边界框内的内容作为参考图像，并将此边界框外的内容作为源图像。为了防止简单的复制粘贴解决方案，它对参考图像应用强增强，基于边界框创建任意形状的蒙版，并使用 CLIP 图像编码器压缩参考图像的信息作为扩散模型的条件。

在此基础上，RIC [143] 将蒙版区域的草图作为控制条件进行训练，允许用户通过草图微调参考图像合成的效果。ObjectStitch [144] 设计了一个内容适配器，以更好地保留参考图像的关键身份信息。同时，PhD [145] 在冻结的预训练扩散模型上训练了一个修复和协调模块，用于有效地指导蒙版区域的修复。为了保留参考图像的低级细节以进行修复，DreamInpainter [146] 利用 U-Net 的下采样网络来提取其特征。在训练过程中，它向整个图像添加噪声，要求扩散模型学习如何在详细文本描述的指导下恢复清晰的图像。此外，Anydoor [147] 使用视频帧中的图像对作为训练样本，以提高图像合成质量，并引入了用于捕获身份特征、保留纹理和学习外观变化的模块。

属性控制的图像编辑。这类论文通常涉及使用特定的图像特征作为控制条件来增强预训练的扩散模型，以学习生成相应的图像。这种方法允许通过更改这些特定的控制条件来进行图像编辑。在对年龄-文本-面部对进行训练后，FADING [148] 通过空文本反演和注意力控制进行面部图像编辑，以进行年龄处理。PAIR 扩散 [149] 将图像视为对象的集合，学习调节每个对象的属性，特别是结构和外观。SmartBrush [150] 使用不同粒度的蒙版作为控制条件，使扩散模型能够根据文本和蒙版的形状修复蒙版区域。为了更好地保留与编辑文本无关的图像信息，IIR-Net [151] 在所需区域执行颜色和纹理擦除。然后，将擦除后的图像用作扩散模型的控制条件之一。

### 4.3 全监督下的指令编辑

使用指令（例如“移除帽子”）来驱动图像编辑过程，而不是使用编辑后图像的描述（例如“一只戴着帽子微笑的小狗”），似乎更自然、更人性化，并且更准确地满足用户的需求。InstructPix2Pix [156] 是第一个学习根据人类指令编辑图像的研究。随后的工作在模型架构、数据集质量、多模态等方面对其进行了改进。因此，我们首先描述 InstructPix2Pix，然后根据其最突出的贡献对后续工作进行分类和介绍。相应地，图 4 描绘了这些基于指令的方法的通用框架。

InstructPix2Pix 框架。使扩散模型能够根据指令编辑图像的主要挑战之一是构建指令-图像配对数据集。InstructPix2Pix 通过两个步骤生成这些图像对。首先，给定图像标题（例如“一个女孩骑马的照片”），它使用微调的 GPT-3 [245] 生成指令（例如“让她骑龙”）和编辑后的图像标题（例如“一个女孩骑龙的照片”）。其次，它使用稳定扩散和 Prompt-to-Prompt 算法 [212] 生成编辑后的图像，收集超过 450,000 个训练图像对。然后，它以完全监督的方式训练指令图像编辑扩散模型，同时考虑输入图像和指令的条件。

模型架构增强。MoEController [157] 引入了一种混合专家 (MOE) 架构，其中包括三个专门的专家，用于细粒度的局部转换、全局风格迁移和复杂的局部编辑任务。另一方面，FoI [158] 利用 InstructPix2Pix 的隐式接地能力来识别和关注特定的编辑区域。它还采用交叉条件注意力调制来确保每个指令都针对其相应的区域，减少多个指令之间的干扰。

数据质量增强。LOFIE [159] 通过利用分割 [246]、思维链提示 [247] 和视觉问答 (VQA) [248] 的最新进展来提高训练数据集的质量。MagicBrush [249] 雇佣来自亚马逊 Mechanical Turk (AMT) 的众包工作者，使用 DALL-E 2 [25] 手动执行连续编辑。它包括 5,313 个编辑会话和 10,388 个编辑回合，从而为指令图像编辑建立了一个全面的基准。InstructDiffusion [160] 是一个统一的框架，将各种视觉任务视为人类直观的图像处理过程，即关键点检测、分割、图像增强和图像编辑。对于图像编辑，它不仅利用现有数据集，还使用用于对象移除和替换的工具以及通过从互联网上收集真实世界的 Photoshop 请求中的图像编辑对来增强它们。Emu Edit [161] 也在图像编辑和识别数据上进行训练，利用一个包含 16 个不同任务的数据集，其中包含 1000 万个示例。该数据集是使用 Llama 2 [250] 和上下文学习创建的，以生成多样化和创造性的编辑指令。在训练过程中，模型与其权重一起学习任务嵌入，从而能够仅使用几个示例即可有效地适应新任务。

DialogPaint [162] 旨在在多轮对话过程中提取用户的编辑意图，并相应地编辑图像。它在 GPT-3 上采用自指令技术 [251] 来创建多轮对话数据集，并结合四个图像编辑模型生成指令图像编辑数据集。此外，作者还微调了 Blender 对话模型 [252]，以根据对话数据生成相应的编辑指令，然后驱动训练后的指令编辑模型来编辑图像。

Inst-Inpaint [163] 允许用户仅通过文本命令指定要从图像中移除的对象，而无需二进制蒙版。它基于图像和场景图数据集 GQA [253] 构建了一个名为 GQA-Inpaint 的数据集。它首先从场景图中选择对象及其对应关系，然后使用 Detectron2 [254] 和 Detic [255] 提取这些对象的分割蒙版。之后，它使用 CRFill [256] 生成修复的目标图像。编辑指令是通过固定模板生成的。在构建数据集之后，Inst-Inpaint 经过训练以执行指令图像修复。

人类反馈增强学习。为了改进编辑图像与人类指令之间的一致性，HIVE [164] 在指令图像编辑中引入了人类反馈强化学习 (RLHF)。在获得基于 [156] 的基础模型后，在人类排名数据集上训练奖励模型。奖励模型的估计被集成到训练过程中，以微调扩散模型，使其与人类反馈保持一致。

视觉指令。ImageBrush [165] 被提出来学习一对转换图像中的视觉指令，这些转换图像说明了所需的处理，并将此指令应用于编辑新图像。该方法将示例图像、源图像和空白图像连接成一个网格，使用扩散模型根据示例图像提供的上下文信息迭代地对空白图像进行去噪。此外，还提出了一种视觉提示编码器，从视觉指令中提取特征以增强扩散过程。

利用多模态大规模模型。InstructAny2Pix [166] 使用户能够通过集成音频、图像和文本的指令来编辑图像。它使用多模态编码器 ImageBind [257] 将各种输入转换为统一的潜空间表示。大型语言模型 (LLM) Vicuna-7b [258] 对多模态输入序列进行编码，以预测两个特殊标记作为条件，使多模态输入与扩散模型的编辑结果保持一致。

MGIE [167] 将图像和指令以及多个 [IMG] 标记输入多模态大型语言模型 (MLLM) LLaVA [259]。然后，它将倒数第二层中 [IMG] 的隐藏状态投影到稳定扩散中 UNet 的交叉注意力层。在训练过程中，LLaVA 和稳定扩散的权重被联合优化。

类似地，SmartEdit [168] 采用 LLaVA，并额外引入了双向交互模块 (BIM) 以在复杂场景中执行图像编辑。它首先使用 QFormer [248] 将 MLLM 的隐藏状态与 CLIP 文本编码器对齐，然后通过 BIM 促进图像特征与 QFormer 输出的融合。此外，它利用感知相关数据（例如分割数据）来增强模型对空间和概念属性的理解。此外，它在复杂的理解和推理场景中合并了合成的编辑数据，以激活 MLLM 的推理能力。

### 4.4 弱监督下的伪目标检索

由于获得准确表示真实情况的编辑图像具有挑战性，因此此类别中的方法旨在检索伪目标图像或直接使用 CLIP 分数 [242] 作为优化模型参数的目标。iEdit [169] 使用弱监督训练扩散模型，利用 CLIP 检索和编辑与编辑文本最相似的数据集图像，作为编辑后的伪目标图像。此外，它将蒙版合并到图像编辑过程中，以通过 CLIPSeg [260] 实现局部保留。为了有效地处理基于区域的图像编辑，TDIELR [170] 首先使用 DINO [261] 处理输入图像，以生成用于锚点初始化的注意力映射和特征。它学习了一个区域生成网络 (RGN) 来选择最合适的区域建议。然后，将选择的区域和文本描述输入预训练的文本到图像模型进行编辑。TDIELR 使用 CLIP 计算分数，评估文本描述和编辑结果之间的相似性，为 RGN 提供训练信号。此外，ChatFace [171] 还利用 CLIP 分数作为学习如何编辑真实面部图像的指标。
## 5 测试时微调方法

在图像生成和编辑中，测试时微调代表着朝着精度和控制迈出的重要一步。本节探讨了各种微调策略（图 5），这些策略增强了图像编辑功能。如图 6 所示，这些方法的范围从微调整个去噪模型到专注于特定层或嵌入。我们研究了微调整个模型、针对特定参数和优化基于文本的嵌入的方法。此外，我们还讨论了超网络的集成和直接图像表示优化。这些方法共同展示了图像编辑中微调技术的不断发展的复杂性和有效性，满足了各种编辑需求和用户意图。

### 5.1 去噪模型微调

去噪模型是图像生成和编辑的核心组件。直接微调它是一种简单有效的方法。因此，许多编辑方法都基于这种微调过程。其中一些涉及微调整个去噪模型，而另一些则专注于微调模型中的特定层。

微调整个去噪模型。微调整个去噪模型可以让模型更好地学习图像的特定特征，更准确地解释文本提示，从而使编辑更符合用户意图。UniTune [172] 在调整阶段对单个基础图像上的扩散模型进行微调，鼓励模型生成与基础图像相似的图像。在采样阶段，使用修改后的采样过程来平衡对基础图像的保真度和对编辑提示的一致性。这包括从基础图像的噪声版本开始采样，并在采样过程中应用无分类器指导。Custom-Edit [173] 使用一小组参考图像来自定义扩散模型，增强编辑图像与参考图像的相似性，同时保持与源图像的相似性。

去噪模型中的部分参数微调。一些方法专注于微调去噪模型的特定部分，例如自注意力层、交叉注意力层、编码器或解码器。这种类型的微调更加精确，在很大程度上保留了预训练模型的功能并在其基础上进行构建。KV Inversion [174] 通过学习键 (K) 和值 (V)，设计了一种增强的自注意力版本，称为内容保留自注意力 (CP-attn)。这有效地解决了对真实图像进行动作编辑的问题，同时保持了原始图像的内容和结构。它为图像编辑提供了一种高效且灵活的解决方案，无需模型微调或在大规模数据集上进行训练。

### 5.2 嵌入微调

许多微调方法选择以文本或空文本嵌入为目标进行细化，从而可以更好地将嵌入与生成过程集成，以实现增强的编辑结果。

空文本嵌入微调。空文本嵌入微调的目标是解决 DDIM Inversion [18] 中的重建失败问题，从而提高与原始图像的一致性。在 Null-Text Inversion [175] 中，首先将 DDIM Inversion 应用于原始图像以获得反演轨迹。然后，在采样过程中，微调空文本嵌入以减少采样轨迹与反演轨迹之间的距离，以便采样过程可以重建原始图像。这种方法的优点是 U-Net 权重和文本嵌入都不会改变，因此可以在不改变用户设置的目标提示的情况下提高重建性能。类似地，DPL [176] 使用泄漏修复损失动态更新文本提示中的名词，以解决交叉注意力泄漏问题。微调空文本嵌入以确保高质量的交叉注意力图和准确的图像重建。

文本嵌入微调。微调来自输入文本的嵌入可以增强图像编辑，使编辑后的图像更符合条件特征。DiffusionDisentanglement [177] 引入了一种简单轻量级的图像编辑算法，通过优化两个文本嵌入的混合权重来实现风格匹配和内容保留。此过程涉及优化大约 50 个参数，优化后的权重在不同的图像中具有良好的泛化能力。Prompt Tuning Inversion [178] 设计了一种用于基于文本的图像编辑的精确且快速的^{-1}演技术，包括重建阶段和编辑阶段。在重建阶段，它将输入图像的信息编码为可学习的文本嵌入。在编辑阶段，通过线性插值计算新的文本嵌入，将目标嵌入与优化后的嵌入相结合，以在保持高保真度的同时实现有效的编辑。

### 5.3 超网络指导

除了传统的生成框架之外，一些方法还结合了自定义网络，以更好地与特定的编辑意图保持一致。StyleDiffusion [179] 引入了一个映射网络，将输入图像的特征映射到与文本提示的嵌入空间对齐的嵌入空间，从而有效地生成提示嵌入。交叉注意力层用于将文本提示嵌入与图像特征表示相结合。这些层通过计算键、值和查询的注意力图来实现文本-图像交互。InST [180] 在其文本^{-1}演部分中集成了多层交叉注意力机制来处理图像嵌入。学习到的关键信息被转换为文本嵌入，可以将其视为代表艺术品独特风格的“新词”，有效地表达其独特的风格。

### 5.4 潜变量优化

图像潜变量的直接优化也是微调过程中采用的一种技术。这种方法涉及通过引入某些损失函数关系和某些中间层的特征来直接优化噪声潜变量，而不是优化生成器或嵌入的条件参数。利用预训练的扩散模型，大多数方法获得了执行图像翻译的能力，而无需配对训练数据。

人类引导的潜变量优化。这种方法允许用户参与图像编辑过程，指导图像的生成。以 Drag-GAN [262] 为代表，这种交互式编辑过程使用户能够指定图像中的特定点并将它们移动到新位置，同时保持图像的其余部分不变。DragGAN 通过优化 GAN 的潜空间来实现这种编辑。随后，基于扩散模型进行了一些开发，例如 DragonDiffusion [181]，它在扩散模型的中间特征中构建了一个能量函数来指导编辑。这使得可以直接通过图像特征进行图像编辑指导，而无需文本描述。DragDiffusion [182] 专注于优化特定时间步长下的扩散潜表示，而不是跨多个时间步长。这种设计基于这样的观察结果，即特定时间步长下的 U-Net 特征图提供了充足的语义和几何信息，以促进拖放编辑。

利用网络层和输入来优化潜变量。一些优化方法利用来自输入条件的嵌入或网络特征来构建损失函数，从而能够直接优化潜变量。DDS [183] 方法利用两个图像-文本对：一个包含源图像及其描述性文本，另一个包含目标图像及其对应的描述性文本。DDS 计算这两个图像-文本对之间的差异，并通过这种比较得出损失。DiffuseIT [184] 中的损失函数还结合使用了 CLIP 模型的文本和图像编码器来计算目标文本与源图像之间的相似性。CDS [185] 将对比学习损失函数集成到 DDS 框架中，利用 LDM [26] 的自注意力层的空间丰富特征，通过对比损失计算来指导图像编辑。

### 5.5 混合微调

一些工作结合了上述各种微调方法，这些方法可以是顺序的，其中调整阶段按顺序进行，也可以作为单个集成工作流的一部分同时进行。这种复合微调方法可以实现有针对性和有效的图像编辑。

文本嵌入和去噪模型微调。Imagic [187] 分阶段实现其目标，首先将目标文本转换为文本嵌入，然后通过最小化嵌入与图像之间的差异来优化该嵌入以重建输入图像。同时，微调扩散模型以实现更好的图像重建。通过优化后的文本嵌入和目标文本之间的线性插值找到一个中间点，结合两者的特征。然后，微调后的扩散模型使用此嵌入来生成最终的编辑图像。LayerDiffusion [188] 优化文本嵌入以匹配输入图像的背景，并采用分层扩散策略来微调模型，增强其保持主体和背景一致性的能力。Forgedit [189] 专注于快速图像重建和找到合适的文本嵌入进行编辑，分别利用扩散模型的编码器和解码器来学习图像布局和纹理细节。

文本编码器和去噪模型微调。SINE [190] 首先微调文本编码器和去噪模型，以更好地理解单个图像的内容和几何结构。它引入了一种基于补丁的微调策略，允许模型生成任何分辨率的图像，而不仅仅是预训练模型的固定分辨率。通过这种微调和补丁训练，SINE 能够处理单图像编辑任务，包括但不限于风格迁移、内容添加和对象处理。

## 参考文献

| Title                                                                                                       | Year | Publish                                                                                          |
| ----------------------------------------------------------------------------------------------------------- | ---- | ------------------------------------------------------------------------------------------------ |
| Generative adversarial nets                                                                                 | 2014 | NeurIPS                                                                                          |
| A style-based generator architecture for generative adversarial networks                                    | 2019 | CVPR                                                                                             |
| Conditional generative adversarial nets                                                                     | 2014 | arXiv preprint arXiv:1411.1784                                                                   |
| Image-to-image translation with conditional adversarial networks                                            | 2017 | CVPR                                                                                             |
| Unpaired image-to-image translation using cycle-consistent adversarial networks                             | 2017 | ICCV                                                                                             |
| Large scale gan training for high fidelity natural image synthesis                                          | 2019 | ICLR                                                                                             |
| Auto-encoding variational bayes                                                                             | 2013 | arXiv preprint arXiv:1312.6114                                                                   |
| Pixel recurrent neural networks                                                                             | 2016 | ICML                                                                                             |
| Variational inference with normalizing flows                                                                | 2015 | ICML                                                                                             |
| Neural discrete representation learning                                                                     | 2017 | NeurIPS                                                                                          |
| Masked autoregressive flow for density estimation                                                           | 2017 | NeurIPS                                                                                          |
| Taming transformers for high-resolution image synthesis                                                     | 2021 | CVPR                                                                                             |
| Zero-shot text-to-image generation                                                                          | 2021 | ICML                                                                                             |
| Energy-based generative adversarial network                                                                 | 2016 | arXiv preprint arXiv:1609.03126                                                                  |
| Deep unsupervised learning using nonequilibrium thermodynamics                                              | 2015 | ICML                                                                                             |
| Denoising diffusion probabilistic models                                                                    | 2020 | NeurIPS                                                                                          |
| Improved denoising diffusion probabilistic models                                                           | 2021 | ICML                                                                                             |
| Denoising diffusion implicit models                                                                         | 2021 | ICLR                                                                                             |
| Estimation of non-normalized statistical models by score matching.                                          | 2005 | JMLR                                                                                             |
| A connection between score matching and denoising autoencoders                                              | 2011 | Neural computation                                                                               |
| Generative modeling by estimating gradients of the data distribution                                        | 2019 | NeurIPS                                                                                          |
| Score-based generative modeling through stochastic differential equations                                   | 2021 | ICLR                                                                                             |
| Improved techniques for training score-based generative models                                              | 2020 | NeurIPS                                                                                          |
| Divae: Photorealistic images synthesis with denoising diffusion decoder                                     | 2022 | arXiv preprint arXiv:2206.00386                                                                  |
| Hierarchical text-conditional image generation with clip latents                                            | 2022 | arXiv preprint arXiv:2204.06125                                                                  |
| High-resolution image synthesis with latent diffusion models                                                | 2022 | CVPR                                                                                             |
| Photorealistic text-to-image diffusion models with deep language understanding                              | 2022 | NeurIPS                                                                                          |
| Classifier-free diffusion guidance                                                                          | 2022 | arXiv preprint arXiv:2207.12598                                                                  |
| Conditional image generation with score-based diffusion models                                              | 2021 | arXiv preprint arXiv:2111.13606                                                                  |
| Analytic-dpm: an analytic estimate of the optimal reverse variance in diffusion probabilistic models        | 2022 | ICLR                                                                                             |
| Cascaded diffusion models for high fidelity image generation                                                | 2022 | JMLR                                                                                             |
| Diffusion models beat gans on image synthesis                                                               | 2021 | NeurIPS                                                                                          |
| More control for free! image synthesis with semantic diffusion guidance                                     | 2023 | WACV                                                                                             |
| Glide: Towards photorealistic image generation and editing with text-guided diffusion models                | 2022 | ICML                                                                                             |
| Text-guided synthesis of artistic images with retrieval-augmented diffusion models                          | 2022 | arXiv preprint arXiv:2207.13038                                                                  |
| Cold diffusion: Inverting arbitrary image transforms without noise                                          | 2022 | arXiv preprint arXiv:2208.09392                                                                  |
| On distillation of guided diffusion models                                                                  | 2023 | CVPR                                                                                             |
| Wavelet diffusion models are fast and scalable image generators                                             | 2023 | CVPR                                                                                             |
| Video diffusion models                                                                                      | 2022 | NeurIPS                                                                                          |
| Make-a-video: Text-to-video generation without text-video data                                              | 2023 | ICLR                                                                                             |
| Imagen video: High definition video generation with diffusion models                                        | 2022 | arXiv preprint arXiv:2210.02303                                                                  |
| Preserve your own correlation: A noise prior for video diffusion models                                     | 2023 | ICCV                                                                                             |
| Align your latents: High-resolution video synthesis with latent diffusion models                            | 2023 | CVPR                                                                                             |
| Magicvideo: Efficient video generation with latent diffusion models                                         | 2022 | arXiv preprint arXiv:2211.11018                                                                  |
| Nuwa-xl: Diffusion over diffusion for extremely long video generation                                       | 2023 | arXiv preprint arXiv:2303.12346                                                                  |
| Structure and content-guided video synthesis with diffusion models                                          | 2023 | ICCV                                                                                             |
| Latent-shift: Latent diffusion with temporal shift for efficient text-to-video generation                   | 2023 | arXiv preprint arXiv:2304.08477                                                                  |
| Modelscope text-to-video technical report                                                                   | 2023 | arXiv preprint arXiv:2308.06571                                                                  |
| Videogen: A reference-guided latent diffusion approach for high definition text-to-video generation         | 2023 | arXiv preprint arXiv:2309.00398                                                                  |
| Latent video diffusion models for high-fidelity video generation with arbitrary lengths                     | 2022 | arXiv preprint arXiv:2211.13221                                                                  |
| Lavie: High-quality video generation with cascaded latent diffusion models                                  | 2023 | arXiv preprint arXiv:2309.15103                                                                  |
| Tune-a-video: One-shot tuning of image diffusion models for text-to-video generation                        | 2023 | ICCV                                                                                             |
| Gpt4motion: Scripting physical motions in text-to-video generation via blender-oriented gpt planning        | 2023 | arXiv preprint arXiv:2311.12631                                                                  |
| Show-1: Marrying pixel and latent diffusion models for text-to-video generation                             | 2023 | arXiv preprint arXiv:2309.15818                                                                  |
| Stable video diffusion: Scaling latent video diffusion models to large datasets                             | 2023 | arXiv preprint arXiv:2311.15127                                                                  |
| Emu video: Factorizing text-to-video generation by explicit image conditioning                              | 2023 | arXiv preprint arXiv:2311.10709                                                                  |
| Image super-resolution via iterative refinement                                                             | 2022 | IEEE TPAMI                                                                                       |
| Palette: Image-to-image diffusion models                                                                    | 2022 | ACM SIGGRAPH                                                                                     |
| Restoring vision in adverse weather conditions with patch-based denoising diffusion models                  | 2023 | IEEE TPAMI                                                                                       |
| Resdiff: Combining cnn and diffusion model for image super-resolution                                       | 2023 | arXiv preprint arXiv:2303.08714                                                                  |
| Implicit diffusion models for continuous super-resolution                                                   | 2023 | CVPR                                                                                             |
| Shadowdiffusion: When degradation prior meets diffusion model for shadow removal                            | 2023 | CVPR                                                                                             |
| Image restoration with mean-reverting stochastic differential equations                                     | 2023 | ICML                                                                                             |
| Diffir: Efficient diffusion model for image restoration                                                     | 2023 | arXiv preprint arXiv:2303.09472                                                                  |
| Ilvr: Conditioning method for denoising diffusion probabilistic models                                      | 2021 | CVPR                                                                                             |
| Denoising diffusion restoration models                                                                      | 2022 | NeurIPS                                                                                          |
| Wavedm: Wavelet-based diffusion models for image restoration                                                | 2024 | IEEE TMM                                                                                         |
| Zero-shot image restoration using denoising diffusion null-space model                                      | 2023 | ICLR                                                                                             |
| Difface: Blind face restoration with diffused error contraction                                             | 2022 | arXiv preprint arXiv:2212.06512                                                                  |
| Improving diffusion models for inverse problems using manifold constraints                                  | 2022 | NeurIPS                                                                                          |
| Diffusion posterior sampling for general noisy inverse problems                                             | 2023 | ICLR                                                                                             |
| A survey on video diffusion models                                                                          | 2023 | arXiv preprint arXiv:2310.10647                                                                  |
| Diffusion models for image restoration and enhancement– a comprehensive survey                              | 2023 | arXiv preprint arXiv:2308.09388                                                                  |
| Diffusion models, image super-resolution and everything: A survey                                           | 2024 | arXiv preprint arXiv:2401.00736                                                                  |
| Diffusion models: A comprehensive survey of methods and applications                                        | 2023 | ACM Computing Surveys                                                                            |
| A survey on generative diffusion model                                                                      | 2022 | arXiv preprint arXiv:2209.02646                                                                  |
| Diffusion models in vision: A survey                                                                        | 2023 | IEEE TPAMI                                                                                       |
| Efficient diffusion models for vision: A survey                                                             | 2022 | arXiv preprint arXiv:2210.09292                                                                  |
| Text-to-image diffusion model in generative ai: A survey                                                    | 2023 | arXiv preprint arXiv:2303.07909                                                                  |
| A survey of diffusion based image generation models: Issues and their solutions                             | 2023 | arXiv preprint arXiv:2308.13142                                                                  |
| State of the art on diffusion models for visual computing                                                   | 2023 | arXiv preprint arXiv:2310.07204                                                                  |
| A comprehensive survey on generative diffusion models for structured data                                   | 2023 | ArXiv, abs/2306.04139 v2                                                                         |
| Sdedit: Image synthesis and editing with stochastic differential equations                                  | 2022 | ICLR                                                                                             |
| Masactrl: Tuning-free mutual self-attention control for consistent image synthesis and editing              | 2023 | arXiv preprint arXiv:2304.08465                                                                  |
| Classifier-free diffusion guidance                                                                          | 2021 | NeurIPS 2021 Workshop on Deep Generative Models and Downstream Applications                      |
| Denoising likelihood score matching for conditional score-based data generation                             | 2022 | ICLR                                                                                             |
| Elucidating the design space of diffusion-based generative models                                           | 2022 | NeurIPS                                                                                          |
| Dpm-solver: A fast ode solver for diffusion probabilistic model sampling in around 10 steps                 | 2022 | NeurIPS                                                                                          |
| Progressive distillation for fast sampling of diffusion models                                              | 2022 | ICLR                                                                                             |
| Vector quantized diffusion model for text-to-image synthesis                                                | 2022 | CVPR                                                                                             |
| Sdxl: Improving latent diffusion models for high-resolution image synthesis                                 | 2023 | arXiv preprint arXiv:2307.01952                                                                  |
| Pixart-α: Fast training of diffusion transformer for photorealistic text-to-image synthesis                 | 2023 | arXiv preprint arXiv:2310.00426                                                                  |
| Emu: Enhancing image generation models using photogenic needles in a haystack                               | 2023 | arXiv preprint arXiv:2309.15807                                                                  |
| Styledrop: Text-to-image generation in any style                                                            | 2023 | arXiv preprint arXiv:2306.00983                                                                  |
| ediffi: Text-to-image diffusion models with an ensemble of expert denoisers                                 | 2022 | arXiv preprint arXiv:2211.01324                                                                  |
| Gligen: Open-set grounded text-to-image generation                                                          | 2023 | CVPR                                                                                             |
| Make-a-scene: Scene-based text-to-image generation with human priors                                        | 2022 | ECCV                                                                                             |
| Spatext: Spatio-textual representation for controllable image generation                                    | 2023 | CVPR                                                                                             |
| Adding conditional control to text-to-image diffusion models                                                | 2023 | ICCV                                                                                             |
| Uni-controlnet: All-in-one control to text-to-image diffusion models                                        | 2023 | arXiv preprint arXiv:2305.16322                                                                  |
| Unicontrol: A unified diffusion model for controllable visual generation in the wild                        | 2023 | arXiv preprint arXiv:2305.11147                                                                  |
| Composer: Creative and controllable image synthesis with composable conditions                              | 2023 | ICML                                                                                             |
| T2i-adapter: Learning adapters to dig out more controllable ability for text-to-image diffusion models      | 2023 | arXiv preprint arXiv:2302.08453                                                                  |
| An image is worth one word: Personalizing text-to-image generation using textual inversion                  | 2023 | ICLR                                                                                             |
| Dreambooth: Fine tuning text-to-image diffusion models for subject-driven generation                        | 2023 | CVPR                                                                                             |
| Multi-concept customization of text-to-image diffusion                                                      | 2023 | CVPR                                                                                             |
| Is this loss informative? faster text-to-image customization by tracking objective dynamics                 | 2023 | NeurIPS                                                                                          |
| Elite: Encoding visual concepts into textual embeddings for customized text-to-image generation             | 2023 | arXiv preprint arXiv:2302.13848                                                                  |
| Cones: Concept neurons in diffusion models for customized generation                                        | 2023 | ICML                                                                                             |
| Subject-driven text-to-image generation via apprenticeship learning                                         | 2023 | arXiv preprint arXiv:2304.00186                                                                  |
| Instantbooth: Personalized text-to-image generation without test-time finetuning                            | 2023 | arXiv preprint arXiv:2304.03411                                                                  |
| Key-locked rank one editing for text-to-image personalization                                               | 2023 | ACM SIGGRAPH                                                                                     |
| Disenbooth: Identity-preserving disentangled tuning for subject-driven text-to-image generation             | 2023 | arXiv preprint arXiv:2305.03374                                                                  |
| Photoswap: Personalized subject swapping in images                                                          | 2023 | arXiv preprint arXiv:2305.18286                                                                  |
| Customnet: Zero-shot object customization with variable-viewpoints in text-to-image diffusion models        | 2023 | arXiv preprint arXiv:2310.19784                                                                  |
| Srdiff: Single image super-resolution with diffusion probabilistic models                                   | 2022 | Neurocomputing                                                                                   |
| Unsupervised medical image translation with adversarial diffusion models                                    | 2022 | arXiv preprint arXiv:2207.08208                                                                  |
| Image restoration with mean-reverting stochastic differential equations                                     | 2023 | CVPR                                                                                             |
| Hierarchical integration diffusion model for realistic image deblurring                                     | 2023 | arXiv preprint arXiv:2305.12966                                                                  |
| Wavelet score-based generative modeling                                                                     | 2022 | NeurIPS                                                                                          |
| Bootstrap diffusion model curve estimation for high resolution low-light image enhancement                  | 2023 | arXiv preprint arXiv:2309.14709                                                                  |
| Exploiting diffusion prior for real-world image super-resolution                                            | 2023 | arXiv preprint arXiv:2305.07015                                                                  |
| Diffbir: Towards blind image restoration with generative diffusion prior                                    | 2023 | arXiv preprint arXiv:2308.15070                                                                  |
| Coser: Bridging image and language for cognitive super-resolution                                           | 2023 | arXiv preprint arXiv:2311.16512                                                                  |
| Scaling up to excellence: Practicing model scaling for photo-realistic image restoration in the wild        | 2024 | arXiv preprint arXiv:2401.13627                                                                  |
| Pseudoinverse-guided diffusion models for inverse problems                                                  | 2022 | ICLR                                                                                             |
| Deep null space learning for inverse problems: convergence analysis and rates                               | 2019 | Inverse Problems                                                                                 |
| Gan prior based null-space learning for consistent super-resolution                                         | 2023 | AAAI                                                                                             |
| Diffusionclip: Text-guided diffusion models for robust image manipulation                                   | 2022 | CVPR                                                                                             |
| Diffusion models already have a semantic latent space                                                       | 2023 | ICLR                                                                                             |
| Towards real-time text-driven image manipulation with unconditional diffusion models                        | 2023 | arXiv preprint arXiv:2304.04344                                                                  |
| Diffstyler: Controllable dual diffusion for text-driven image stylization                                   | 2024 | IEEE TNNLS                                                                                       |
| Stylediffusion: Controllable disentangled style transfer via diffusion models                               | 2023 | ICCV                                                                                             |
| Unit-ddpm: Unpaired image translation with denoising diffusion probabilistic models                         | 2021 | arXiv preprint arXiv:2104.05358                                                                  |
| Cyclenet: Rethinking cycle consistency in text-guided diffusion for image manipulation                      | 2023 | NeurIPS                                                                                          |
| Diffusion autoencoders: Toward a meaningful and decodable representation                                    | 2022 | CVPR                                                                                             |
| Hierarchical diffusion autoencoders and disentangled image manipulation                                     | 2024 | WACV                                                                                             |
| Egsde: Unpaired image-to-image translation via energy-guided stochastic differential equations              | 2022 | NeurIPS                                                                                          |
| Fine-grained image editing by pixel-wise guidance using diffusion models                                    | 2023 | CVPR workshop                                                                                    |
| Paint by example: Exemplar-based image editing with diffusion models                                        | 2023 | CVPR                                                                                             |
| Reference-based image composition with sketch via structure-aware diffusion model                           | 2023 | CVPR workshop                                                                                    |
| Objectstitch: Object compositing with diffusion model                                                       | 2023 | CVPR                                                                                             |
| Paste, inpaint and harmonize via denoising: Subject-driven image editing with pre-trained diffusion model   | 2023 | arXiv preprint arXiv:2306.07596                                                                  |
| Dreaminpainter: Text-guided subject-driven image inpainting with diffusion models                           | 2023 | arXiv preprint arXiv:2312.03771                                                                  |
| Anydoor: Zero-shot object-level image customization                                                         | 2024 | CVPR                                                                                             |
| Face aging via diffusion-based editing                                                                      | 2023 | BMCV                                                                                             |
| Pair-diffusion: Object-level image editing with structure-and-appearance paired diffusion models            | 2023 | arXiv preprint arXiv:2303.17546                                                                  |
| Smartbrush: Text and shape guided object inpainting with diffusion model                                    | 2023 | CVPR                                                                                             |
| Text-to-image editing by image information removal                                                          | 2024 | WACV                                                                                             |
| A task is worth one word: Learning with task prompts for high-quality versatile image inpainting            | 2023 | arXiv preprint arXiv:2312.03594                                                                  |
| Imagen editor and editbench: Advancing and evaluating text-guided image inpainting                          | 2023 | CVPR                                                                                             |
| Smartmask: Context aware high-fidelity mask generation for fine-grained object insertion and layout control | 2024 | CVPR                                                                                             |
| Uni-paint: A unified framework for multimodal image inpainting with pretrained diffusion model              | 2023 | ACM MM                                                                                           |
| Instructpix2pix: Learning to follow image editing instructions                                              | 2023 | CVPR                                                                                             |
| Moecontroller: Instruction-based arbitrary image manipulation with mixture-of-expert controllers            | 2023 | arXiv preprint arXiv:2309.04372                                                                  |
| Focus on your instruction: Fine-grained and multi-instruction image editing by attention modulation         | 2024 | CVPR                                                                                             |
| Learning to follow object-centric image editing instructions faithfully                                     | 2023 | EMNLP                                                                                            |
| Instructdiffusion: A generalist modeling interface for vision tasks                                         | 2024 | CVPR                                                                                             |
| Emu edit: Precise image editing via recognition and generation tasks                                        | 2023 | arXiv preprint arXiv:2311.10089                                                                  |
| Dialogpaint: A dialog-based image editing model                                                             | 2023 | arXiv preprint arXiv:2303.10073                                                                  |
| Inst-inpaint: Instructing to remove objects with diffusion models                                           | 2023 | arXiv preprint arXiv:2304.03246                                                                  |
| Hive: Harnessing human feedback for instructional visual editing                                            | 2024 | CVPR                                                                                             |
| Imagebrush: Learning visual in-context instructions for exemplar-based image manipulation                   | 2023 | NeurIPS                                                                                          |
| Instructany2pix: Flexible visual editing via multimodal instruction following                               | 2023 | arXiv preprint arXiv:2312.06738                                                                  |
| Guiding instruction-based image editing via multimodal large language models                                | 2024 | ICLR                                                                                             |
| Smartedit: Exploring complex instruction-based image editing with multimodal large language models          | 2024 | CVPR                                                                                             |
| iedit: Localised text-guided image editing with weak supervision                                            | 2023 | arXiv preprint arXiv:2305.05947                                                                  |
| Text-driven image editing via learnable regions                                                             | 2024 | CVPR                                                                                             |
| Chatface: Chat-guided real face editing via diffusion latent space manipulation                             | 2023 | arXiv preprint arXiv:2305.14742                                                                  |
| Unitune: Text-driven image editing by fine tuning an image generation model on a single image               | 2023 | ACM TOG                                                                                          |
| Custom-edit: Text-guided image editing with customized diffusion models                                     | 2023 | CVPR workshop                                                                                    |
| Kv inversion: Kv embeddings learning for text-conditioned real image action editing                         | 2023 | arXiv preprint arXiv:2309.16608                                                                  |
| Null-text inversion for editing real images using guided diffusion models                                   | 2023 | CVPR                                                                                             |
| Dynamic prompt learning: Addressing cross-attention leakage for text-based image editing                    | 2023 | NeurIPS                                                                                          |
| Uncovering the disentanglement capability in text-to-image diffusion models                                 | 2023 | CVPR                                                                                             |
| Prompt tuning inversion for text-driven image editing using diffusion models                                | 2023 | ICCV                                                                                             |
| Stylediffusion: Prompt-embedding inversion for text-based editing                                           | 2023 | arXiv preprint arXiv:2303.15649                                                                  |
| Inversion-based style transfer with diffusion models                                                        | 2023 | CVPR                                                                                             |
| Dragondiffusion: Enabling drag-style manipulation on diffusion models                                       | 2024 | ICLR                                                                                             |
| Dragdiffusion: Harnessing diffusion models for interactive point-based image editing                        | 2024 | CVPR                                                                                             |
| Delta denoising score                                                                                       | 2023 | ICCV                                                                                             |
| Diffusion-based image translation using disentangled style and content representation                       | 2023 | ICLR                                                                                             |
| Contrastive denoising score for text-guided latent diffusion image editing                                  | 2024 | CVPR                                                                                             |
| Magicremover: Tuning-free text-guided image inpainting with diffusion models                                | 2023 | arXiv preprint arXiv:2310.02848                                                                  |
| Imagic: Text-based real image editing with diffusion models                                                 | 2023 | CVPR                                                                                             |
| Layerdiffusion: Layered controlled image editing with diffusion models                                      | 2023 | SIGGRAPH Asia 2023 Technical Communications                                                      |
| Forgedit: Text guided image editing via learning and forgetting                                             | 2023 | arXiv preprint arXiv:2309.10556                                                                  |
| Sine: Single image editing with text-to-image diffusion models                                              | 2023 | CVPR                                                                                             |
| Preditor: Text guided image editing with diffusion prior                                                    | 2023 | arXiv preprint arXiv:2302.07979                                                                  |
| Regeneration learning of diffusion models with rich prompts for zero-shot image translation                 | 2023 | arXiv preprint arXiv:2305.04651                                                                  |
| User-friendly image editing with minimal text input: Leveraging captioning and injection techniques         | 2023 | arXiv preprint arXiv:2306.02717                                                                  |
| Instructedit: Improving automatic masks for diffusion-based image editing with user instructions            | 2023 | arXiv preprint arXiv:2305.18047                                                                  |
| Direct inversion: Optimization-free text-driven real image editing with diffusion models                    | 2022 | arXiv preprint arXiv:2211.07825                                                                  |
| An edit friendly ddpm noise space: Inversion and manipulations                                              | 2024 | CVPR                                                                                             |
| The blessing of randomness: Sde beats ode in general diffusion-based image editing                          | 2024 | ICLR                                                                                             |
| Ledits++: Limitless image editing using text-to-image models                                                | 2024 | CVPR                                                                                             |
| Fec: Three finetuning-free methods to enhance consistency for real image editing                            | 2023 | arXiv preprint arXiv:2309.14934                                                                  |
| Iterative multi-granular image editing using diffusion models                                               | 2024 | WACV                                                                                             |
| Negative-prompt inversion: Fast image inversion for editing with text-guided diffusion models               | 2023 | arXiv preprint arXiv:2305.16807                                                                  |
| Proxedit: Improving tuning-free real image editing with proximal guidance                                   | 2024 | WACV                                                                                             |
| Null-text guidance in diffusion models is secretly a cartoon-style creator                                  | 2023 | ACM MM                                                                                           |
| Edict: Exact diffusion inversion via coupled transformations                                                | 2023 | CVPR                                                                                             |
| Effective real image editing with accelerated iterative diffusion inversion                                 | 2023 | ICCV                                                                                             |
| A latent space of stochastic diffusion models for zero-shot image editing and guidance                      | 2023 | ICCV                                                                                             |
| Training-free content injection using h-space in diffusion models                                           | 2024 | WACV                                                                                             |
| Fixed-point inversion for text-to-image diffusion models                                                    | 2023 | arXiv preprint arXiv:2312.12540                                                                  |
| Tuning-free inversion-enhanced control for consistent image editing                                         | 2023 | arXiv preprint arXiv:2312.14611                                                                  |
| Diffusion brush: A latent diffusion model-based editing tool for ai-generated images                        | 2023 | arXiv preprint arXiv:2306.00219                                                                  |
| Diffusion self-guidance for controllable image generation                                                   | 2023 | NeurIPS                                                                                          |
| Prompt-to-prompt image editing with cross-attention control                                                 | 2023 | ICLR                                                                                             |
| Zero-shot image-to-image translation                                                                        | 2023 | ACM SIGGRAPH                                                                                     |
| Plug-and-play diffusion features for text-driven image-to-image translation                                 | 2023 | CVPR                                                                                             |
| Tf-icon: Diffusion-based training-free cross-domain image composition                                       | 2023 | ICCV                                                                                             |
| Localizing object-level shape variations with text-to-image diffusion models                                | 2023 | ICCV                                                                                             |
| Conditional score guidance for text-driven image-to-image translation                                       | 2023 | NeurIPS                                                                                          |
| Energy-based cross attention for bayesian context update in text-to-image diffusion models                  | 2023 | NeurIPS                                                                                          |
| Shape-guided diffusion with inside-outside attention                                                        | 2024 | WACV                                                                                             |
| Hd-painter: High-resolution and prompt-faithful text-guided image inpainting with diffusion models          | 2023 | arXiv preprint arXiv:2312.14091                                                                  |
| Fisedit: Accelerating text-to-image editing via cache-enabled sparse diffusion inference                    | 2024 | AAAI                                                                                             |
| Blended latent diffusion                                                                                    | 2023 | ACM TOG                                                                                          |
| Pfb-diff: Progressive feature blending diffusion for text-driven image editing                              | 2023 | arXiv preprint arXiv:2306.16894                                                                  |
| Diffedit: Diffusion-based semantic image editing with mask guidance                                         | 2023 | ICLR                                                                                             |
| Region-aware diffusion for zero-shot text-driven image editing                                              | 2023 | arXiv preprint arXiv:2302.11797                                                                  |
| Text-guided mask-free local image retouching                                                                | 2023 | ICME                                                                                             |
| Differential diffusion: Giving each pixel its strength                                                      | 2023 | arXiv preprint arXiv:2306.00950                                                                  |
| Watch your steps: Local image and scene editing by text instructions                                        | 2023 | arXiv preprint arXiv:2308.08947                                                                  |
| Blended diffusion for text-driven editing of natural images                                                 | 2022 | CVPR                                                                                             |
| Zone: Zero-shot instruction-guided local editing                                                            | 2024 | CVPR                                                                                             |
| Inpaint anything: Segment anything meets image inpainting                                                   | 2023 | arXiv preprint arXiv:2304.06790                                                                  |
| The stable artist: Steering semantics in diffusion latent space                                             | 2022 | arXiv preprint arXiv:2212.06013                                                                  |
| Sega: Instructing text-to-image models using semantic guidance                                              | 2023 | NeurIPS                                                                                          |
| Ledits: Real image editing with ddpm inversion and semantic guidance                                        | 2023 | arXiv preprint arXiv:2307.00522                                                                  |
| Object-aware inversion and reassembly for image editing                                                     | 2024 | ICLR                                                                                             |
| Progressive growing of gans for improved quality, stability, and variation                                  | 2018 | ICLR                                                                                             |
| Stargan v2: Diverse image synthesis for multiple domains                                                    | 2020 | CVPR                                                                                             |
| Lsun: Construction of a large-scale image dataset using deep learning with humans in the loop               | 2015 | arXiv preprint arXiv:1506.03365                                                                  |
| Stylegan-nada: Clip-guided domain adaptation of image generators                                            | 2022 | ACM TOG                                                                                          |
| Styleclip: Text-driven manipulation of stylegan imagery                                                     | 2021 | ICCV                                                                                             |
| Learning transferable visual models from natural language supervision                                       | 2021 | ICML                                                                                             |
| Interpreting the latent space of gans for semantic face editing                                             | 2020 | CVPR                                                                                             |
| Image2stylegan++: How to edit the embedded images?                                                          | 2020 | CVPR                                                                                             |
| Language models are few-shot learners                                                                       | 2020 | NeurIPS                                                                                          |
| Segment anything                                                                                            | 2023 | ICCV                                                                                             |
| Chain-of-thought prompting elicits reasoning in large language models                                       | 2022 | NeurIPS                                                                                          |
| Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models      | 2023 | ICML                                                                                             |
| Magicbrush: A manually annotated dataset for instruction-guided image editing                               | 2023 | arXiv preprint arXiv:2306.10012                                                                  |
| Llama 2: Open foundation and fine-tuned chat models                                                         | 2023 | arXiv preprint arXiv:2307.09288                                                                  |
| Self-instruct: Aligning language model with self generated instructions                                     | 2022 | arXiv preprint arXiv:2212.10560                                                                  |
| Recipes for building an open-domain chatbot                                                                 | 2021 | ACL                                                                                              |
| Gqa: A new dataset for real-world visual reasoning and compositional question answering                     | 2019 | CVPR                                                                                             |
| Detectron2                                                                                                  | 2019 | [https://github.com/facebookresearch/detectron2](https://github.com/facebookresearch/detectron2) |
| Detecting twenty-thousand classes using image-level supervision                                             | 2022 | ECCV                                                                                             |
| Cr-fill: Generative image in-painting with auxiliary contextual reconstruction                              | 2021 | ICCV                                                                                             |
| Imagebind: One embedding space to bind them all                                                             | 2023 | CVPR                                                                                             |
| Vicuna: An open-source chatbot impressing gpt-4 with 90%* chatgpt quality                                   | 2023 | See [https://vicuna.lmsys.org](https://vicuna.lmsys.org/)                                        |
| Visual instruction tuning                                                                                   | 2023 | NeurIPS                                                                                          |
| Image segmentation using text and image prompts                                                             | 2022 | CVPR                                                                                             |
| Dino: Detr with improved denoising anchor boxes for end-to-end object detection                             | 2023 | ICLR                                                                                             |
| Drag your gan: Interactive point-based manipulation on the generative image manifold                        | 2023 | ACM SIGGRAPH                                                                                     |
| Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation    | 2022 | ICML                                                                                             |
| Sud2: Supervision by denoising diffusion models for image reconstruction                                    | 2023 | arXiv preprint arXiv:2303.09642                                                                  |
| Supervision by denoising                                                                                    | 2023 | IEEE TPAMI                                                                                       |
| Repaint: Inpainting using denoising diffusion probabilistic models                                          | 2022 | CVPR                                                                                             |
| Gradpaint: Gradient-guided inpainting with diffusion models                                                 | 2023 | arXiv preprint arXiv:2309.09614                                                                  |
| Improving diffusion models for inverse problems using manifold constraints                                  | 2023 | ICLR                                                                                             |
| Pseudoinverse-guided diffusion models for inverse problems                                                  | 2023 | ICLR                                                                                             |
| Generative diffusion prior for unified image restoration and enhancement                                    | 2023 | CVPR                                                                                             |
| Towards coherent image inpainting using denoising diffusion implicit models                                 | 2023 | ICML                                                                                             |
| Diracdiffusion: Denoising and incremental reconstruction with assured data-consistency                      | 2023 | arXiv preprint arXiv:2303.14353                                                                  |
| Mobilenetv2: Inverted residuals and linear bottlenecks                                                      | 2018 | CVPR                                                                                             |
| Personalized face inpainting with diffusion models by parallel visual attention                             | 2024 | WACV                                                                                             |
| Resolution-robust large mask inpainting with fourier convolutions                                           | 2022 | WACV                                                                                             |
| Editval: Benchmarking diffusion based text-guided image editing methods                                     | 2023 | arXiv preprint arXiv:2310.02426                                                                  |
| Microsoft coco: Common objects in context                                                                   | 2014 | ECCV                                                                                             |
| Improving image generation with better captions                                                             | 2023 | Computer Science                                                                                 |
| Clipscore: A reference-free evaluation metric for image captioning                                          | 2021 | EMNLP                                                                                            |
| Adversarial diffusion distillation                                                                          | 2023 | arXiv preprint arXiv:2311.17042                                                                  |
| One-step diffusion distillation via deep equilibrium models                                                 | 2023 | arXiv preprint arXiv:2306.06104                                                                  |
| Consistency models                                                                                          | 2023 | ICML                                                                                             |