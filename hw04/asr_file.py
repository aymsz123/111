import whisper
import os

def transcribe_audio(audio_path, model_name="base", language="zh"):
    """
    音频文件离线识别
    :param audio_path: 音频文件路径（支持mp3/wav等格式）
    :param model_name: Whisper模型名称(tiny/base/small/medium/large-v3)
    :param language: 识别语言，zh=中文
    :return: 识别结果文本
    """
    # 加载模型
    print(f"正在加载{model_name}模型...")
    model = whisper.load_model(model_name)
    
    # 执行识别
    print(f"正在识别音频：{audio_path}")
    result = model.transcribe(audio_path, language=language)
    
    return result["text"]

if __name__ == "__main__":
    # 配置参数
    AUDIO_PATH = "voiceover/voiceover.mp3"  # 任务二配音文件路径
    MODEL_NAME = "base"  # 笔记本CPU推荐base，GPU可换large-v3
    LANGUAGE = "zh"
    
    # 执行识别
    result_text = transcribe_audio(AUDIO_PATH, MODEL_NAME, LANGUAGE)
    
    # 输出结果
    print("\n=== 识别结果 ===")
    print(result_text)
    
    # 保存结果到文件
    output_path = "asr_result.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result_text)
    print(f"\n识别结果已保存到：{output_path}")
