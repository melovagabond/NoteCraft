# 🎼 NoteCraft

**NoteCraft** is a desktop app that converts audio files (MP3, WAV, FLAC) into **piano sheet music**. It uses AI models to transcribe the audio into MIDI and renders the results into printable PDF sheet music.

Perfect for musicians, arrangers, and hobbyists looking to turn melodies into musical notation.

---

## ✨ Features

- 🖱️ **GUI interface** — no command-line needed!
- 🎵 Supports `.mp3`, `.wav`, `.flac` audio input
- 🎼 Converts audio to **sheet music** (PDF)
- 🤖 Built-in AI model: **Basic Pitch**
- 📄 LilyPond rendering via `music21`
- 🔌 Easily extendable to support other models (e.g. Onsets and Frames, MT3)

---

## 🖥️ Installation

### ✅ Using Conda (Recommended)

Install Conda via [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/).

Then run:

```bash
conda env create -f environment.yml
conda activate notecraft
python notecraft.py
```

---

## 🧱 Dependencies

- `Python 3.10`
- `ffmpeg` – audio decoding
- `lilypond` – sheet music rendering
- `basic-pitch` – audio-to-MIDI transcription
- `music21`, `pydub`, `ffmpeg-python`, `tkinter` – audio handling and GUI

---

## 📂 Project Structure

```
notecraft/
├── notecraft.py             # Main application
├── environment.yml          # Conda env config
├── requirements.txt         # pip fallback
├── README.md                # This file
├── .gitignore
└── assets/
    └── logo.png             # Optional UI branding
```

---

## 🧠 Model Support

### Default: **Basic Pitch**
- Fast and reliable monophonic/polyphonic transcription.
- Trained on real-world audio samples.

### Coming Soon:
- 🎹 **Onsets and Frames** (Magenta TensorFlow model)
- 🎼 **MT3** (Multi-track transformer for polyphonic music)

---

## 📄 Usage

1. Launch the app:
   ```bash
   python notecraft.py
   ```

2. Upload an audio file via the GUI.

3. Select your desired transcription model.

4. Wait for processing — your PDF sheet music will be generated in the same folder as your audio file.

---

## 🧪 Development Tips

- To add a new model: extend `transcribe_audio_to_midi()` in `notecraft.py`
- To support MIDI playback or audio preview: integrate `pygame.midi` or `pyaudio`

---

## 🤝 Contributing

Got an idea for a new model or feature? Open an issue or submit a PR!

---

## 📄 License

MIT License