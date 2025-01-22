import streamlit as st

from utils import generate_xiaohongshu


st.header("爆紅Youtub腳本助手 ✏️")
with st.sidebar:
    openai_api_key = st.text_input("請輸入OpenAI API Key：", type="password")
    st.markdown("[獲取OpenAI API Key](https://platform.openai.com/account/api-keys)")

theme = st.text_input("主題")
submit = st.button("開始寫作")

openai_api_key = st.secrets["OPENAI_API_KEY"]
#if submit and not openai_api_key:
#    st.info("請輸入你的OpenAI API Key")
#    st.stop()
if submit and not theme:
    st.info("請輸入生成內容的主題")
    st.stop()
if submit:
    with st.spinner("AI正在努中寫作中, 請稍候..."):
        result = generate_xiaohongshu(theme, openai_api_key)
    st.divider()
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("##### Youtube標題1")
        st.write(result.titles[0])
        st.markdown("##### Youtube標題2")
        st.write(result.titles[1])
        st.markdown("##### Youtube標題3")
        st.write(result.titles[2])
        st.markdown("##### Youtube標題4")
        st.write(result.titles[3])
        st.markdown("##### Youtube標題5")
        st.write(result.titles[4])
    with right_column:
        st.markdown("##### Youtube正文")
        st.write(result.content)
