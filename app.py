import streamlit as st
import google.generativeai as genai

# ---------- Configure API ----------
genai.configure(api_key="AIzaSyDdyGAVEVKb4mwu3yQXjcPXr69Qdf0sxUs")

model = genai.GenerativeModel("gemini-1.5-flash")

# ---------- UI ----------
st.title("Legal Draft AI Tool")

uploaded_file = st.file_uploader("Upload Draft (.txt)", type=["txt"])
draft_text_input = st.text_area("Or type your draft here")

draft = ""

if uploaded_file:
    draft = uploaded_file.read().decode("utf-8")

elif draft_text_input:
    draft = draft_text_input

# ---------- Generate ----------
if draft:
    if st.button("Generate Improved Draft"):

        prompt = f"""
        Improve the following legal draft professionally:

        {draft}
        """

        response = model.generate_content(prompt)
        improved_text = response.text

        st.subheader("Improved Draft")
        st.write(improved_text)

        st.download_button(
            label="Download Improved Draft",
            data=improved_text,
            file_name="improved_draft.txt",
            mime="text/plain"
        )
