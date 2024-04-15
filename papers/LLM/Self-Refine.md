- Self-Refine: Iterative Refinement with Self-Feedback
- [Self-Refine: Iterative Refinement with Self-Feedback (selfrefine.info)](https://selfrefine.info/)
- [madaan/self-refine: LLMs can generate feedback on their work, use it to improve the output, and repeat this process iteratively. (github.com)](https://github.com/madaan/self-refine)
	- 462 stars
- [[2303.17651 Self-Refine.pdf]]
### Abstract
现有的LLM通常不能再第一次就能给出最好的答案。对于人类来说，也是如此。
```mermaid
graph TD;
	请生成计算阶乘的代码-->LLM1;
	LLM1-->低效的阶乘代码;
	低效的阶乘代码-->LLM2;
	请指出上述代码的缺陷并生成更好的代码-->LLM2;
	LLM2-->高效的阶乘代码;
```