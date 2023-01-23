import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Mildew is an fungus that can infect the leafs of the cherry tree."
        f"A leaf from the cherry tree is collected. Visual criteria are used to detect mildew infection."
        f"The mildew infection is devistating to the cherry tree farmers and takes alot of time for the farm workers to detect and handle project Dataset"
        f"*The mildew is detected through the dots on the leaves of the tree that got the fungus. It is detected by the eye and experience of the worker.\n"
        f"**Project Dataset**\n"
        f"*The dataset provided contains a total of 4208 images where half is mildew infected and the rest is healthy")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/AlbinHall/mildew-detection/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"The client is interested in a study to differentiate between a Mildew contained leaf and a healthy leaf.\n"
        f"The client is interested in telling whether a given leaf(tree) contains mildew or not\n"
        )