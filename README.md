
# Delta-TTS

Delta-TTS is a controllable and efficient zero-shot text-to-speech (TTS) system based on IndexTTS. It supports high-quality speech synthesis for both English and Chinese, with advanced pronunciation correction and pause control.

## Features
- Zero-shot voice cloning and high-quality speech synthesis
- Supports both English and Chinese text
- Punctuation-based pause and prosody control
- Efficient inference pipeline, suitable for research and production

## Installation
1. Clone the repository and install dependencies:
   ```bash
   git clone https://github.com/Delta-Zero-Games/delta-tts.git
   cd delta-tts
   pip install -r requirements.txt
   ```
   Or install as a package:
   ```bash
   pip install .
   ```

2. Download or place the required model checkpoints in the `checkpoints/` directory (see your team lead for access).

## Usage
Run TTS inference from the command line:
```bash
python -m indextts.infer --text "Your text here" --audio_prompt path/to/input.wav --output_path out.wav
```

Or use the Python API:
```python
from indextts.infer import IndexTTS

tts = IndexTTS(cfg_path="checkpoints/config.yaml", model_dir="checkpoints")
tts.infer(audio_prompt="input.wav", text="Hello world!", output_path="out.wav")
```

## Project Info
- Repository: https://github.com/Delta-Zero-Games/delta-tts
- License: See `DELTA_TTS_LICENSE`

> **Note:** Model checkpoints are required for inference. Contact the team lead for access or location.

---

## Acknowledgments
- [IndexTTS](https://github.com/index-tts/index-tts)
- [tortoise-tts](https://github.com/neonbjb/tortoise-tts)
- [XTTSv2](https://github.com/coqui-ai/TTS)
- [BigVGAN](https://github.com/NVIDIA/BigVGAN)
- [wenet](https://github.com/wenet-e2e/wenet/tree/main)
- [icefall](https://github.com/k2-fsa/icefall)

