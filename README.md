# Secret-Tools
该仓库包含了各种安全工程实践工具集合，供用户使用

## 随机数规范检测工具

随机数规范检测工具是一个用于随机数质量检测的程序，实现了多种随机性检验算法，并提供直观简洁的图形用户界面。

文档：[随机数规范检测工具文档](Random%20number%20specification%20testing/README.md)

---
### 1. 克隆仓库

```bash
git clone https://github.com/Sec-Secret-SEU/Secret-Tools.git
cd Secret-Tools
```

安装依赖

```bash
pip install -r "Random number specification testing/requirements.txt"
```

依赖说明：
- `PyQt6` — 图形界面框架
- `numpy` — 随机数生成与数值计算
- `scipy` — 统计检验数学函数

运行

```bash
cd "Random number specification testing"
python mainUI.py
```
---