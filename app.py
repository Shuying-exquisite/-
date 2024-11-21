import streamlit as st
import streamlit.components.v1 as components
import os

# 设置页面布局为宽屏模式
st.set_page_config(layout="wide")

# 使用相对路径访问 HTML 文件
html_file_path = os.path.join(os.path.dirname(__file__), "新建文本文档.HTML")

try:
    with open(html_file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    
    # 显示 HTML 内容，占满整个 Streamlit 界面
    components.html(html_content, height=800, scrolling=True)  # 根据需要调整 height
except FileNotFoundError:
    st.error(f"找不到指定的 HTML 文件：{html_file_path}")
