# HW07：胸部X光肺炎检测

## 目录结构
- `train.ipynb`：完整训练与评估代码，含运行输出
- `requirements.txt`：依赖库列表
- `report.md`：实验报告
- `figures/`：训练曲线、混淆矩阵等结果图片

## 运行说明
1. 数据集获取：从Kaggle下载Chest X-Ray Images (Pneumonia)数据集，解压到`./chest_xray`目录下。
2. 环境配置：`pip install -r requirements.txt`
3. 运行：在Jupyter/Kaggle/Colab中打开`train.ipynb`，按顺序执行所有单元格。

## 测试结果摘要
- 测试准确率：~93%
- 测试召回率：~97%
