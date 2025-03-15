from transformers import pipeline
import gradio as gr

# Load the GPT-2 model
chatbot_pipeline = pipeline("text-generation", model="gpt2")

# Function to generate chatbot response
def chatbot_response(user_input, chat_history, max_length):
    try:
        # Generate response using the pipeline
        response = chatbot_pipeline(
            user_input,
            max_length=max_length,
            pad_token_id=50256  # GPT-2's pad token ID
        )
        bot_message = response[0]['generated_text'].strip()
    except Exception as e:
        bot_message = f"Sorry, an error occurred: {str(e)}"

    # Update chat history
    chat_history.append((user_input, bot_message))
    return chat_history

# Gradio interface with a chat-like UI and a different theme
with gr.Blocks(theme="soft") as demo:  # Change the theme here
    gr.Markdown("# 🤖 GPT-2 Chatbot")
    gr.Markdown("Chat with a GPT-2 based chatbot! Customize the response length below.")

    # Chatbot interface
    chatbot = gr.Chatbot(label="Conversation", height=400)
    msg = gr.Textbox(label="Your Message", placeholder="Type your message here...")
    clear = gr.Button("Clear Chat")

    # Max Length slider
    max_length = gr.Slider(minimum=10, maximum=200, value=50, label="Max Length")

    # Submit action
    msg.submit(
        chatbot_response,
        inputs=[msg, chatbot, max_length],
        outputs=chatbot
    )
    clear.click(lambda: [], None, chatbot, queue=False)

# Launch the Gradio app
demo.launch()