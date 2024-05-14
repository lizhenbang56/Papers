```
\section{conda}

\begin{lstlisting}

conda env list  // 列出环境

conda create -n 环境名 python=3.8  // 创建新环境

\end{lstlisting}

\subsection{conda与pip的冲突}

\verb|conda install| 和 \verb|pip install| 均可以安装包，但若在一个环境中同时用conda和pip安装包，则可能产生问题。

比如，用conda安装了pytorch，再用pip安装\verb|pytorch_lighting|就会出现问题。此外，如果用conda安装\verb|pytorch_lighting|，则会安装很低的版本。
```

## Conda 环境迁移 

```bash
// 在源计算机上
pip install conda-pack
conda pack -n <env_name>
# 若报错CondaPackError, 再该环境中执行一遍 conda list，再执行conda pack命令即可。

// 在目标计算机上
conda info  // 获得conda所在路径
cd conda路径/envs
mkdir <env_name>
tar -zxvf <env_name>.tar.gz -C <env_name>
```