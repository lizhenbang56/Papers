---
Url: https://arxiv.org/pdf/2404.05595.pdf
Publish: arXiv2024
Year: "2024"
Month: "04"
Title: "UniFL: Improve Stable Diffusion via Unified Feedback Learning"
创新点: 扩散模型
Author: 字节跳动
---
## 摘要

扩散模型已经彻底改变了图像生成领域，导致高质量模型和多样化的下游应用的大量涌现。然而，尽管取得了这些重大进展，当前的竞争性解决方案仍然存在一些限制，包括视觉质量较差、缺乏审美吸引力以及推断效率低下，没有一个全面的解决方案在视野中。为了解决这些挑战，我们提出了UniFL，这是一个利用反馈学习全面增强扩散模型的统一框架。UniFL作为一个通用、有效和可泛化的解决方案，适用于各种扩散模型，如SD1.5和SDXL。值得注意的是，UniFL包括三个关键组成部分：感知反馈学习，增强视觉质量；解耦反馈学习，提高美学吸引力；以及对抗性反馈学习，优化推断速度。深入的实验和广泛的用户研究验证了我们提出的方法在提高生成模型质量和加速方面的优越性能。例如，UniFL在生成质量方面超过了ImageReward 17%的用户偏好，在4步推断中超过了LCM和SDXL Turbo分别为57%和20%。此外，我们已经验证了我们方法在包括Lora、ControlNet和AnimateDiff在内的下游任务中的功效。

关键词：扩散模型 · 反馈学习 · 加速

## 1 介绍 

扩散模型的出现使得文本到图像（T2I）领域进入了一个空前的进步时代，其中有一些显著的贡献，比如DALLE-3 [34]、Imagen [38]、Midjourney [49]等等。特别是，开源图像生成模型的引入，比如稳定的扩散[35]，开启了一个变革性的文本到图像时代，催生了许多下游应用，如T2I个性化[15, 21, 37, 60]、可控生成[29, 33, 61]和文本到视频（T2V）生成[16, 18, 53]。尽管迄今取得了显著的进展，但目前基于稳定扩散的图像生成模型仍存在一定的局限性。i) 质量较差：生成的图像往往质量较差，缺乏真实性。例如，角色的四肢不完整或身体部分扭曲，以及在风格表示方面的有限保真度。ii) 缺乏美感：生成的图像在美学吸引力方面存在明显的偏差，因为它们往往无法与人类的偏好相一致。关键方面的不足，如细节、光线和氛围进一步加剧了这种美学差异。iii) 推断效率低下：扩散模型采用的迭代去噪过程引入了显著的推断速度低下，从而限制了这些模型在各种应用场景中的实用性。 最近，许多研究致力于解决上述挑战。例如，SDXL [32]通过改进训练策略提高了扩散模型的生成质量，而RAPHAEL [59]则采用了混合专家（MoE）[14, 44, 63]技术。RAFT [11]、HPS [54, 55]、ImageReward [57]和DPO [50]提出将人类反馈纳入扩散模型，以引导其与人类偏好相一致。另一方面，SDXL Turbo [40]、PGD [39]和LCM [27, 28]等则通过诸如蒸馏和一致性模型[46]的技术来解决推断加速的问题。 然而，这些方法主要集中于通过专门设计来解决单个问题，这给这些技术的直接集成带来了重大挑战。例如，MoE显著地复杂化了流程，使加速方法变得不可行，而一致性模型[46]改变了扩散模型的去噪过程，使得直接应用ImageReward [57]提出的ReFL框架变得艰难。自然而然地，一个相关的问题出现了：我们能否设计出一种更有效的方法，全面提高扩散模型在图像质量、美学外观和生成速度方面的表现呢？ 在本文中，我们提出了UniFL，这是一种创新的方法，通过统一的反馈学习为扩散模型提供全面的改进。UniFL旨在提高视觉生成质量、增强偏好美学并加速推断过程。为了实现这些目标，我们提出了三个关键组成部分。首先，我们引入了开创性的感知反馈学习（PeFL）框架，有效地利用了各种现有感知模型中蕴含的丰富知识来提高视觉生成质量。该框架使得能够提供更精确和有针对性的反馈信号，最终在各个方面提高了视觉生成的质量。 其次，我们采用解耦反馈学习来优化美学质量。通过将粗略的美学概念分解为色彩、氛围和质地等不同方面，UniFL简化了美学优化的挑战。此外，我们引入了一种主动提示选择策略，选择更具信息性和多样性的提示，以促进更有效的美学偏好反馈学习。 最后，UniFL开发了对抗性反馈学习，在这种学习中，奖励模型和扩散模型进行对抗训练，使得在低去噪步骤下的样本通过奖励反馈得到了很好的优化，最终实现了优越的推断加速。UniFL提出了一个统一的反馈学习公式，既简单又多才多艺，使其适用于各种模型，并取得了令人印象深刻的改进。我们的贡献总结如下：

- 新的见解：我们提出的方法UniFL，引入了一种统一的反馈学习框架，以优化扩散模型的视觉质量、美学和推断速度。据我们所知，UniFL是首次尝试同时解决生成质量和速度问题的工作，在该领域提供了新的视角。
- 新颖和开创性：在我们的工作中，我们阐明了利用现有感知模型在扩散模型反馈学习中的潜力。我们强调了解耦奖励模型的重要性，并通过对抗训练阐明了推断加速的基本机制。我们相信我们的消融实验提供了有价值的见解，丰富了社区对这些技术的理解。
- 高效性：通过大量实验，我们展示了UniFL在多种类型的扩散模型（包括SD1.5和SDXL）上取得的显著改进，无论是在生成质量还是加速方面。此外，UniFL优于竞争性现有方法，并在各种下游任务上展现了强大的泛化能力。