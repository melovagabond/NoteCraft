import os
import tempfile
from tkinter import Tk, filedialog, Button, Label, messagebox, StringVar
from tkinter import ttk
from pydub import AudioSegment
from music21 import converter, instrument

# Optional imports: Use try/except so the script doesn't crash if models are not installed
try:
    from basic_pitch.inference import predict_and_save as basic_pitch_transcribe
except ImportError:
    basic_pitch_transcribe = None

try:
    from magenta.models.onsets_frames_transcription.transcribe import transcribe_audio as of_transcribe
except ImportError:
    of_transcribe = None

# Add other models (e.g. MT3) as needed

def convert_audio_to_wav(input_path):
    ext = os.path.splitext(input_path)[1].lower()
    audio = AudioSegment.from_file(input_path, format=ext[1:])
    wav_path = os.path.join(tempfile.gettempdir(), os.path.basename(input_path).replace(ext, ".wav"))
    audio.export(wav_path, format="wav")
    return wav_path

def transcribe_audio_to_midi(wav_path, model_name):
    output_dir = tempfile.mkdtemp()
    midi_path = os.path.join(output_dir, os.path.basename(wav_path).replace(".wav", ".mid"))

    if model_name == "Basic Pitch":
        if basic_pitch_transcribe is None:
            raise ImportError("Basic Pitch is not installed.")
        basic_pitch_transcribe([wav_path], output_directory=output_dir, save_midi=True)
    elif model_name == "Onsets and Frames":
        if of_transcribe is None:
            raise ImportError("Onsets and Frames is not installed.")
        # Placeholder: Implement OF transcription with Magenta TF graph
        raise NotImplementedError("Onsets and Frames support needs TensorFlow setup.")
    elif model_name == "MT3":
        raise NotImplementedError("MT3 support not implemented yet.")
    else:
        raise ValueError(f"Unsupported model: {model_name}")

    return midi_path

def convert_midi_to_pdf(midi_path, output_pdf_path):
    score = converter.parse(midi_path)
    parts = instrument.partitionByInstrument(score)

    piano_part = None
    if parts:  # MIDI contains instrument parts
        for p in parts.parts:
            if 'Piano' in str(p.getInstrument()):
                piano_part = p
                break
        if not piano_part:
            piano_part = parts.parts[0]
    else:
        piano_part = score

    piano_part.write("lily.pdf", fp=output_pdf_path)
    return output_pdf_path

def handle_file_selection():
    file_path = filedialog.askopenfilename(
        title="Select a music file",
        filetypes=[("Audio files", "*.mp3 *.wav *.flac")]
    )
    if not file_path:
        return

    model_name = model_choice.get()

    try:
        status_label.config(text="Converting audio...")
        wav_path = convert_audio_to_wav(file_path)

        status_label.config(text=f"Transcribing to MIDI using {model_name}...")
        midi_path = transcribe_audio_to_midi(wav_path, model_name)

        status_label.config(text="Generating sheet music PDF...")
        out_pdf = os.path.splitext(file_path)[0] + f"_{model_name.replace(' ', '_')}_sheet.pdf"
        convert_midi_to_pdf(midi_path, out_pdf)

        status_label.config(text="Done!")
        messagebox.showinfo("Success", f"Sheet music saved to:\n{out_pdf}")
    except Exception as e:
        status_label.config(text="Error occurred")
        messagebox.showerror("Error", str(e))

def start_gui():
    root = Tk()
    root.title("Audio to Piano Sheet Music")
    root.geometry("450x250")

    Label(root, text="Convert Audio to Sheet Music", font=("Helvetica", 14)).pack(pady=10)

    # Model selection dropdown
    Label(root, text="Choose transcription model:").pack(pady=5)
    global model_choice
    model_choice = StringVar()
    model_dropdown = ttk.Combobox(root, textvariable=model_choice, state="readonly")
    model_dropdown['values'] = ("Basic Pitch", "Onsets and Frames", "MT3")
    model_dropdown.current(0)
    model_dropdown.pack(pady=5)

    Button(root, text="Upload Music File", command=handle_file_selection, width=30).pack(pady=20)

    global status_label
    status_label = Label(root, text="", fg="blue")
    status_label.pack()

    root.mainloop()

if __name__ == "__main__":
    start_gui()
