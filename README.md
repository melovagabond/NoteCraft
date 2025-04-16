# 🎹 NoteCraft

**NoteCraft** is a Python-based application that converts audio files (MP3, WAV, FLAC) into piano sheet music. It leverages advanced AI transcription models to analyze audio and generate corresponding sheet music in PDF format.

---

## 🚀 Features

- **Audio Format Support**: Accepts MP3, WAV, and FLAC files.
- **Transcription Models**: Choose between multiple AI models:
  - *Basic Pitch* (default)
  - *Onsets and Frames*
  - *MT3*
- **Sheet Music Generation**: Converts transcribed MIDI files into sheet music PDFs using LilyPond.
- **User-Friendly GUI**: Simple interface for uploading files and selecting transcription models.

---

## 🖥️ Installation

### Prerequisites

- Python 3.8 or higher
- [LilyPond](https://lilypond.org/) installed and added to system PATH
- [FFmpeg](https://ffmpeg.org/) installed and added to system PATH

### Install Dependencies

```bash
pip install -r requirements.txt
```

*`requirements.txt` should include:*
- `pydub`
- `music21`
- `basic-pitch`
- `tkinter` (usually included with Python)

---

## 🎛️ Usage

1. **Run the Application**:

   ```bash
   python notecraft.py
   ```

2. **Using the GUI**:
   - Click on "Upload Music File" to select an audio file.
   - Choose a transcription model from the dropdown menu.
   - The application will process the file and generate a PDF sheet music file in the same directory.

---

## 🧠 Transcription Models

- **Basic Pitch**: Lightweight and fast; suitable for monophonic and simple polyphonic audio.
- **Onsets and Frames**: TensorFlow-based; excels with piano music.
- **MT3**: Transformer-based model; handles multiple instruments and complex compositions.

*Note: Ensure the selected model is properly installed and configured.*

---

## 📂 Project Structure

```
notecraft/
├── notecraft.py
├── requirements.txt
├── README.md
└── assets/
    └── icon.png
```

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

---

## 📄 License

This project is licensed under the MIT License.
