import streamlit as st
import helper
import pickle

# Page config
st.set_page_config(
    page_title="Quora Duplicate Question Detector",
    page_icon="🔍",
    layout="centered"
)

# Load model
@st.cache_resource
def load_model():
    return pickle.load(open("model.pkl", "rb"))

model = load_model()

# UI
st.title("🔍 Quora Duplicate Question Detector")
st.markdown("Enter two questions below to check if they are semantically duplicate.")

st.divider()

q1 = st.text_area("Question 1", placeholder="e.g. What is the best way to learn Python?", height=100)
q2 = st.text_area("Question 2", placeholder="e.g. How can I start learning Python effectively?", height=100)

if st.button("🔎 Check for Duplicate", use_container_width=True):
    if not q1.strip() or not q2.strip():
        st.warning("Please enter both questions before checking.")
    else:
        with st.spinner("Analyzing..."):
            query = helper.query_point_creator(q1, q2)
            result = model.predict(query)[0]

        st.divider()
        if result:
            st.success("✅ These questions are **Duplicate**")
            st.markdown("The two questions are asking the same thing in different ways.")
        else:
            st.error("❌ These questions are **Not Duplicate**")
            st.markdown("The two questions are semantically different.")

st.divider()
st.caption("Built with ❤️ using Streamlit · Trained on Quora Question Pairs dataset")