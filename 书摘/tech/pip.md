## 输入

```bash
pip3 install -U insightface
```

## 错误

```bash
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 10: ordinal not in range(128)
```

## 解决方案

```bash
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```