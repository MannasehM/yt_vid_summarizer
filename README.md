# 🎥 YouTube Video Summarizer & Q&A (Local, Free)

This Python project lets you:
- Download a YouTube video transcript
- Restore punctuation (Silero)
- Summarize the video (local transformer)
- Ask unlimited questions about the content

Runs 100% locally — no paid API keys.

---

## 🚀 Features

- Transcript pulled via [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/)
- Punctuation restored using [Silero Models](https://github.com/snakers4/silero-models) (runs locally with `torch.hub.load`)
- Summarization powered by [Hugging Face Transformers](https://huggingface.co/facebook/bart-large-cnn)
- Unlimited Q&A using [deepset/roberta-base-squad2](https://huggingface.co/deepset/roberta-base-squad2)


## ✅ How to Run

1. **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    # OR
    venv\Scripts\activate     # Windows
    ```
2. **Install requirements:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Download Silero model once:**
    ```bash
    python setup_silero.py
    ```
4. **Run the app:**
    ```bash
    python main.py
    ```
