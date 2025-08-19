import torch
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

def get_video_id(url_link):
    video_id_and_timestamp = url_link.split('watch?v=')[-1]
    return video_id_and_timestamp.split('&')[0]

# 1️. Get transcript
video_link = input('Enter a YouTube link: ')
video_id = get_video_id(video_link)
print("video_id: " + video_id)
print(type(video_id))

ytt_api = YouTubeTranscriptApi()
fetched_transcript = ytt_api.fetch(video_id)

raw_text = ""
for snippet in fetched_transcript:
    raw_text += snippet.text + " "
raw_text = raw_text[:-1]

# transcript = YouTubeTranscriptApi.fetch(video_id).to_raw_data()
# raw_text = " ".join([entry['text'] for entry in transcript])

# 2️. Restore punctuation
# model, example_texts, languages, punct, apply_te = torch.hub.load('snakers4/silero-models', 'silero_te')
# if not raw_text: 
#     print("Error: raw_text is empty!")
# else: 
#     print(raw_text)
#     punctuated_text = apply_te(raw_text, lan='en')
#     print("\n Preview of punctuated text:\n")
#     print(punctuated_text[:300])
punctuated_text = raw_text


# 3️. Generate summary
print("\n⏳ Generating summary...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

max_chunk = 1000
summary_texts = []
for i in range(0, len(punctuated_text), max_chunk):
    chunk = punctuated_text[i:i+max_chunk]
    summary = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
    summary_texts.append(summary[0]['summary_text'])

full_summary = " ".join(summary_texts)

print("\n Summary:\n")
print(full_summary)

# 4️. Unlimited Q&A loop
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

print("\n Ask me anything about the video! Type 'quit' to exit.\n")

while True:
    question = input("Your question: ")
    if question.lower() == 'quit':
        print("Goodbye!")
        break

    result = qa_pipeline({
        'question': question,
        'context': punctuated_text
    })
    print("Answer:", result['answer'])