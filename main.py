import torch
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def get_video_id(url_link):
    video_id_and_timestamp = url_link.split('watch?v=')[-1]
    return video_id_and_timestamp.split('&')[0]

# Initialize Falcon model for summarization
model_name = "tiiuae/falcon-7b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)

# 1. Get transcript
video_link = input('Enter a YouTube link: ')
video_id = get_video_id(video_link)
print("video_id: " + video_id)

try:
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(video_id)

    text = ""
    for snippet in fetched_transcript:
        text += snippet.text + " "
    text = text[:-1]

    print(f"Transcript length: {len(text)} characters")

    # 2. Generate summary using Falcon
    print("\n⏳ Generating summary with Falcon...")

    # Create a prompt for summarization
    summary_prompt = f"""Please provide a comprehensive summary of the following text:
                        {text[:500]}  # Using first 500 chars to avoid token limits
                        Summary:"""

    # Generate summary
    summary_result = generator(
        summary_prompt,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.9,
        num_return_sequences=1,
        return_full_text=False,
        pad_token_id=tokenizer.pad_token_id,
        use_cache=False,
    )

    full_summary = summary_result[0]['generated_text'].strip()

    print("\n Summary:\n")
    print(full_summary)

    # 3. Q&A using Falcon
    print("\n Ask me anything about the video! Type 'quit' to exit.\n")

    while True:
        question = input("Your question: ")
        if question.lower() == 'quit':
            print("Goodbye!")
            break

        # Create Q&A prompt for Falcon
        qa_prompt = f"""Based on the following context, answer the question:
                        Context: {text[:500]}  # Using first 2000 chars for context
                        Question: {question}
                        Answer:"""

        try:
            # Generate answer
            answer_result = generator(
                qa_prompt,
                max_new_tokens=100,
                do_sample=True,
                temperature=0.5,
                top_k=30,
                num_return_sequences=1,
                return_full_text=False,
                pad_token_id=tokenizer.pad_token_id,
                use_cache=False,
            )

            answer = answer_result[0]['generated_text'].strip()
            print("Answer:", answer)

        except Exception as e:
            print(f"Error generating answer: {e}")

except Exception as e:
    print(f"Error fetching transcript: {e}")