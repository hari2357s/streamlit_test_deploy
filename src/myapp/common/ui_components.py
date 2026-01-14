"""
Docstring for myapp.Common.ui_components
"""

import streamlit as st


def my_text(text, size="h3", alignment="left", color="white", padding=True):
    """
    Docstring for my_text

    :param text: Description
    :param size: Description
    :param alignment: Description
    :param color: Description
    :param padding: Description
    """
    data = f"""<{size} style = "text-align: {alignment} ; color : {color};
        padding : {"20px" if padding else "0px"} ">{text}</{size}>"""
    return st.markdown(data, unsafe_allow_html=True)


def toast_warning(msg):
    """
    Docstring for toast_warning

    :param msg: Description
    """
    st.toast(msg, icon=":material/warning:")


def toast_success(msg):
    """
    Docstring for toast_success

    :param msg: Description
    """
    st.toast(msg, icon=":material/verified:")


def success(msg):
    """
    Docstring for success

    :param msg: Description
    """
    st.success(msg, icon=":material/verified:")
