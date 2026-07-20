# import gradio as gr
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# def llm_call(message,history):
#     load_dotenv()
#     api_key = os.getenv("GEMINI_API_KEY")

#     genai.configure(api_key=api_key)

#     model=genai.GenerativeModel("gemini-3.5-flash")

#     response = model.generate_content(message+" generate a story based on this prompt 0f 250 words ")
#     print(response)
#     return response.text

    
# demo = gr.ChatInterface(fn=llm_call,title ="Nivi's ai story generator")
# demo.launch(share=True) 

#--------------------------------------------------------
import gradio as gr
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.5-flash")


def generate_story(plot):

    prompt = f"""
You are a professional story writer.

Generate a creative story of around 250 words based on the following plot.

Plot:
{plot}

After generating the story, provide the output in the following format.

Story:
<Story>

Characters:
- Character 1
- Character 2
- ...

Summary:
<2-3 sentence summary>

Return only the above format.
"""

    response = model.generate_content(prompt)

    text = response.text

    story = ""
    characters = ""
    summary = ""

    try:
        story = text.split("Characters:")[0].replace("Story:", "").strip()

        characters = text.split("Characters:")[1].split("Summary:")[0].strip()

        summary = text.split("Summary:")[1].strip()

    except:
        story = text
        characters = "Not Found"
        summary = "Not Found"

    return story, characters, summary


# ---------------- UI ---------------- #

with gr.Blocks(
    theme=gr.themes.Soft(),
    title="📚 Nivi's AI Story Generator"
) as demo:

    gr.Markdown(
        """
        # 📚 Nivi's AI Story Generator
        ### Enter a story idea and let AI create a beautiful story for you.
        """
    )

    with gr.Row():

        with gr.Column(scale=1):

            plot = gr.Textbox(
                label="📝 Story Plot",
                placeholder="Example: A lonely astronaut discovers an abandoned alien city on Mars...",
                lines=8
            )

            generate = gr.Button(
                "✨ Generate Story",
                variant="primary"
            )

        with gr.Column(scale=2):

            story = gr.Textbox(
                label="📖 Generated Story",
                lines=18,
                interactive=False
            )

    with gr.Row():

        with gr.Column():

            characters = gr.Textbox(
                label="👥 Characters",
                lines=8,
                interactive=False
            )

        with gr.Column():

            summary = gr.Textbox(
                label="📄 Story Summary",
                lines=8,
                interactive=False
            )

    generate.click(
        fn=generate_story,
        inputs=plot,
        outputs=[story, characters, summary]
    )

demo.launch(share=True)
