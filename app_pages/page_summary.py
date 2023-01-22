import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Mildew is fungus transmitted by spores "
        f"*The mildew is detected through the dots on the leaves of the tree that got the fungus. It is detected by the eye and experience of the worker.\n"
        f"**Project Dataset**\n"
        f"*The dataset provided contains a total of 4208 images where half is mildew infected and the rest is healthy")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file]().")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"a parasitized and uninfected cell visually.\n"
        f"* 2 - The client is interested in telling whether a given cell contains a malaria parasite or not. "
        )