import streamlit as st


st.header("File uploader in chat input prototype demo!")
st.write("Upload images and see them in the chat!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

x = st.chat_input(
    "Say something nice or upload it!", accept_file="multiple", file_type=["png", "jpg"]
)

if x is not None:
    st.session_state.chat_history.append(x)

for message in st.session_state.chat_history:
    with st.chat_message("human"):
        st.write(message["text"])

        for file in message["files"]:
            st.image(file)
