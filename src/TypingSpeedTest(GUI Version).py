!pip install gradio --quiet

import gradio as gr
import random
import time

# Sample sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed tests help improve your accuracy.",
    "Python is a fun programming language to learn.",
    "Practice makes perfect when it comes to typing.",
    "Fast typing requires good hand-eye coordination."
]

# Global variable to store start time
start_time = 0
chosen_sentence = ""

def start_test():
    global start_time, chosen_sentence
    chosen_sentence = random.choice(sentences)
    start_time = time.time()
    return chosen_sentence, ""

def evaluate_typing(user_input):
    global start_time, chosen_sentence
    end_time = time.time()
    time_taken = end_time - start_time
    time_in_minutes = time_taken / 60

    word_count = len(user_input.split())
    wpm = word_count / time_in_minutes

    
    # Calculate correct characters and total characters typed
    correct_chars = sum(1 for i, c in enumerate(user_input) if i < len(chosen_sentence) and c == chosen_sentence[i])
    total_chars = max(len(user_input), len(chosen_sentence))
    accuracy = (correct_chars / total_chars) * 100


    result = f"""⏱️ Time Taken: {round(time_taken, 2)} sec
📝 Words Per Minute: {round(wpm, 2)} WPM
✅ Accuracy: {round(accuracy, 2)}%
"""
    return result

with gr.Blocks() as app:
    gr.Markdown("## 🧠 Typing Speed Test")
    sentence_output = gr.Textbox(label="Type this sentence:", interactive=False)
    input_box = gr.Textbox(label="Start typing here...")
    result_box = gr.Textbox(label="Results", lines=4, interactive=False)

    start_btn = gr.Button("🎯 Start Test")
    submit_btn = gr.Button("✅ Submit")

    start_btn.click(start_test, outputs=[sentence_output, input_box])
    submit_btn.click(evaluate_typing, inputs=input_box, outputs=result_box)

app.launch()