# YouTube Video Summarizer & Q&A

This Python project lets you:

- Pull YouTube video transcripts without an API key
- Summarize the video content using a powerful local LLM (Falcon 7B)
- Ask unlimited questions about the video content
- Run entirely on your machine or in Google Colab (no paid APIs required)

## Features

- **Transcript extraction:** [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/)
- **Summarization & Q&A:** [Hugging Face Transformers](https://huggingface.co/tiiuae/falcon-7b-instruct)
- **Local execution:** Works without cloud API calls
- **Interactive Q&A loop:** Ask any question about the video transcript

## 🛠 Technologies Used

- Python 3.10+
- PyTorch
- Hugging Face Transformers (`tiiuae/falcon-7b-instruct`)
- `youtube-transcript-api`

## How to Run

### **Option 1: Local Machine**

1. **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    # OR
    venv\Scripts\activate     # Windows
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app:**
    ```bash
    python main.py
    ```

4. **Follow prompts:**
   - Enter a YouTube video link
   - Wait for the transcript fetch
   - Get a summary and interact with Q&A

### **Option 2: Google Colab**

1. Open a new notebook in [Google Colab](https://colab.research.google.com/).
2. **Download the `.ipynb` file** in this github repo. 
2. **Upload the `.ipynb` file** you downloaded in Colab. 
3. **Switch to GPU runtime**:
    - Go to `Runtime` → `Change runtime type` → `Hardware accelerator` → `GPU`.
4. **Run the notebook cells** step by step.
5. Follow prompts to enter a YouTube video link, get a summary, and ask questions.