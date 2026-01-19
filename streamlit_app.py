import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_hybrid_blog(topic):
    prompt = f"""
You are a senior Generative AI engineer and professional content strategist.

Write a high-quality long-form blog for BOTH:
1. Software development company website (professional, business-focused)
2. Medium readers (engaging, story-driven)

Topic: {topic}

STRICT RULES:
- Do NOT use hashtags (#)
- Do NOT use markdown symbols such as **, *, __, or bullet characters
- Use clean plain text
- Use section titles written normally with blank lines between sections
- Maintain readability without formatting symbols

CONTENT STRUCTURE:
Introduction
Why This Topic Matters Now
Concept Explained Simply
Business Benefits
Industry Use Cases
Technical Deep Dive
ROI and Business Impact
Future Trends
Challenges and Solutions
Conclusion

CONTENT REQUIREMENTS:
- Begin with a relatable narrative introduction
- Explain why the topic is important in current market trends
- Add simple explanation for beginners
- Add deep technical insights for developers
- Explain architecture and workflow without code blocks
- Show industry-wise use cases (healthcare, finance, retail, logistics, manufacturing, education)
- Include ROI benefits with realistic numbers
- Provide challenges and practical solutions
- End with a strong conclusion and subtle call-to-action
- Use paragraph spacing for readability
- Avoid markdown formatting completely

Generate the full article now.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=2500
    )
    return response.choices[0].message.content


def main():
    st.title("Hybrid Blog Generator for Software Development & AI Companies")

    topic = st.text_input("Enter Blog Topic")

    # Initialize session state variable if not exists
    if "blog_content" not in st.session_state:
        st.session_state.blog_content = ""

    if st.button("Generate Blog"):
        if not topic.strip():
            st.error("Please enter a topic first.")
        else:
            with st.spinner("Generating content... Please wait."):
                blog = generate_hybrid_blog(topic)
                st.session_state.blog_content = blog

    if st.session_state.blog_content:
        st.text_area("Generated Blog Content", st.session_state.blog_content, height=600)


if __name__ == "__main__":
    main()
