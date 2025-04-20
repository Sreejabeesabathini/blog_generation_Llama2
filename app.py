import streamlit as st  # type: ignore
from langchain.llms import CTransformers  # type: ignore
import re

# ---------------------- Blog Generation Function ----------------------

def get_Llama_response(input_text, num_words, blog_style):
    try:
        # Load the LLaMA model
        llm = CTransformers(
            model=r'D:\NLP Practice\Blog Genertion using Llama2\models\llama-2-7b-chat.ggmlv3.q8_0.bin',
            model_type='llama',
            config={
                'max_new_tokens': 256,
                'temperature': 0.01
            }
        )
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

    # Prompt with instruction to finish the blog
    formatted_prompt = f"""
    Write a blog for a {blog_style} job profile on the topic "{input_text}". 
    The blog should be approximately {num_words} words. 
    End with a clear and meaningful concluding sentence that summarizes the blog.
    """

    try:
        response = llm(formatted_prompt)
        return response
    except Exception as e:
        st.error(f"❌ Error generating response: {e}")
        return None

# ---------------------- Force Full Sentence Ending ----------------------

def force_clean_ending(text):
    sentences = re.findall(r'[^.!?]*[.!?]', text.strip(), re.DOTALL)
    clean_sentences = [s.strip() for s in sentences if len(s.split()) > 5]

    strong_blog = []
    for i, sentence in enumerate(clean_sentences):
        # Prevent ending with incomplete trailing phrases
        if re.search(r'\b(this|these|they|which|that|who|it)\s*$', sentence.lower()):
            break

        strong_blog.append(sentence)

        # Stop if the next sentence looks vague or repetitive
        if i + 1 < len(clean_sentences):
            next_sentence = clean_sentences[i + 1].lower()
            if next_sentence.startswith((
                "in conclusion", "therefore", "this shows", 
                "to summarize", "it is important to note", "may be"
            )):
                continue
            if any(end in next_sentence for end in ["to conclude", "overall", "in summary"]):
                break

    result = ' '.join(strong_blog).strip()
    if result and result[-1] not in '.!?':
        result += '.'

    return result

# ---------------------- Streamlit UI ----------------------

st.set_page_config(
    page_title="Blog Generator",
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.header("📝 AI Blog Generator")

# Input fields
input_text = st.text_input("Enter the Topic to generate the Blog")

col1, col2 = st.columns([1, 1])

with col1:
    num_words = st.text_input('Number of Words', value='300')

with col2:
    blog_style = st.selectbox(
        'Blog for Profession',
        ('Researchers', 'Data Scientists', 'Recent Graduates', 'Freshers', 'Common People'),
        index=0
    )

# Generate button
submit = st.button("Generate")

# On Submit
if submit:
    if not input_text or not num_words:
        st.warning("⚠️ Please fill in all fields before generating.")
    else:
        st.write("📨 Submitting request...")
        st.write(f"**Topic:** {input_text}  \n**Words:** {num_words}  \n**Style:** {blog_style}")

        with st.spinner("Generating blog using LLaMA..."):
            output = get_Llama_response(input_text, num_words, blog_style)

        if output:
            final_blog = force_clean_ending(output)
            st.subheader("📄 Generated Blog:")
            st.write(final_blog)
        else:
            st.warning("⚠️ No output was generated. Please check the model path or inputs.")
