import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# BLOG GENERATOR FUNCTION
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
Introduction:
Why This Topic Matters Now:
Concept Explained Simply:
Business Benefits:
Industry Use Cases:
Technical Deep Dive:
ROI and Business Impact:
Future Trends:
Challenges and Solutions:
Conclusion:

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

#  STREAMLIT UI
def main():
    st.title("Software Development & AI Companies Blog Generator")

    st.write("Enter your topic below and generate a professional blog designed for both business and developer audiences.")

    topic = st.text_input("Enter Blog Topic")

    if st.button("Generate Blog"):
        if not topic.strip():
            st.error("Please enter a topic first.")
        else:
            st.write("Generating content... Please wait.")
            blog = generate_hybrid_blog(topic)
            st.text_area("Generated Blog Content", blog, height=600)


if __name__ == "__main__":
    main()
