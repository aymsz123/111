# hw04 课程作业说明
## 一、目录结构说明
hw04/
├── text_gen.md # 任务一：大模型生成文稿（含标题、正文、模型与 Prompt）
├── jianying.md # 任务二：剪映声音克隆说明（步骤、导出格式、替代方案）
├── asr_report.md # 任务三：ASR 调研对比报告（3 种方案对比、选型理由）
├── experiment_log.md # 任务三：实验过程与结果记录（环境、测试、性能）
├── requirements.txt # 任务三：代码依赖清单
├── asr_file.py # 任务三：音频文件识别代码
├── asr_realtime.py # 任务三：实时麦克风识别代码
├── README.md # 本文件：总览、运行说明
└── voiceover/
└── voiceover.mp3 # 任务二：剪映导出的配音音频（文件过大可替换为网盘链接）
## 二、各任务对应文件
| 任务 | 对应文件 |
| :--- | :--- |
| 任务一：大模型生成文稿 | `text_gen.md` |
| 任务二：剪映声音克隆 | `jianying.md` + `voiceover/voiceover.mp3` |
| 任务三：开源语音识别调研与实现 | `asr_report.md` + `experiment_log.md` + `asr_file.py` + `asr_realtime.py` + `requirements.txt` |

## 三、环境安装与运行说明
### 1. 环境准备
- 安装Python 3.9-3.11，配置好pip环境
- 安装系统依赖FFmpeg：
  - Windows：下载FFmpeg并配置环境变量
  - macOS：`brew install ffmpeg`
  - Linux：`sudo apt install ffmpeg`

### 2. 安装依赖
```bash
pip install -r requirements.txt
