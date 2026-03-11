# AI 交互日志

## 1. 需求描述
- 初始 Prompt：实现八皇后问题的 Python 求解器，要求标准工程结构（含 src/ 和 tests/），并编写单元测试验证 N=4 和 N=8 的解数量。
- 补充要求：需要包含 README.md 和 requirements.txt，后续要演示引入 Bug 并由 AI 辅助修复的过程。

## 2. Bug 发现与处理
- 引入 Bug：在 `eight_queens.py` 中修改判断条件，遗漏副对角线 `diag2` 检查：
  ```python
  # 错误代码
  if c not in col and (row - c) not in diag1:
