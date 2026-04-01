import whisper
import pyaudio
import numpy as np
import time

def realtime_transcribe(model_name="base", language="zh", interval=3):
    """
    麦克风实时语音识别
    :param model_name: Whisper模型名称，实时推荐tiny/base
    :param language: 识别语言，zh=中文
    :param interval: 识别间隔（秒）
    """
    # 加载模型
    print(f"正在加载{model_name}模型...")
    model = whisper.load_model(model_name)
    
    # 音频配置（Whisper要求16kHz单声道）
    CHUNK = 1024 * 4
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    
    # 初始化音频流
    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )
    
    print(f"\n开始实时语音识别（识别间隔{interval}秒，按Ctrl+C停止）...")
    audio_buffer = np.array([], dtype=np.float32)
    
    try:
        while True:
            # 读取麦克风数据
            data = stream.read(CHUNK)
            audio_chunk = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0
            audio_buffer = np.concatenate((audio_buffer, audio_chunk))
            
            # 达到间隔时长，执行识别
            if len(audio_buffer) >= RATE * interval:
                result = model.transcribe(audio_buffer, language=language)
                print(f"\r实时识别：{result['text']}", end="", flush=True)
                # 保留最后0.5秒，避免断句错误
                audio_buffer = audio_buffer[int(RATE * 0.5):]
            
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n\n识别结束")
    finally:
        # 释放资源
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    # 配置参数
    MODEL_NAME = "base"
    LANGUAGE = "zh"
    INTERVAL = 3  # 秒
    
    realtime_transcribe(MODEL_NAME, LANGUAGE, INTERVAL)
