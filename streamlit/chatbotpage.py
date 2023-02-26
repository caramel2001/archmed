import streamlit as st
from streamlit_chat import message
import requests
from st_pages import add_page_title
from archmed.summarization_and_qna_transformers import *
import time

st.set_page_config(page_title="ArchMed ChatBot", page_icon=":robot:")
# model = getModel_QNA()
add_page_title()

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []

response = [
    "Hi",
    "The sex bias in autism diagnosis suggests the involvement of sex-specific endocrine mechanisms during prenatal development, but these hormones affect health throughout life. Therefore, the current study examined the association of autism and autistic traits with conditions and symptoms related to the sex-steroid system in adult women. In total, 1230 women (361 autistic), aged 15–77 years, reported on autistic traits and medical history. Medical diagnoses and symptoms were grouped by unsupervised factor analysis, and associations with autism diagnosis and autistic traits were explored. Higher rates of reproductive system diagnoses (odds ratio = 1.035, p = 0.024), prediabetes symptoms (odds ratio = 1.319, p = 0.001), irregular puberty onset (odds ratio = 1.458, p = 0.009), and menstrual length (odds ratio = 1.368, p = 0.034) and lower rates of metabolic and vascular conditions (odds ratio = 0.654, p = 0.013) were associated with diagnosis. Reproductive system diagnoses (β = 0.114, p = 0.000), prediabetes symptoms (β = 0.188, p = 0.000), menstrual length (β = 0.071, p = 0.014), irregular puberty onset (β = 0.149, p = 0.000), excessive menstruation symptoms (β = 0.097, p = 0.003), and hyperandrogenism symptoms (β = 0.062, p = 0.040) were also associated with autistic traits. Many of the conditions and symptoms found to be associated with autism or autistic traits are also related to conditions of steroid hormones and, specifically, the sex-steroid system. The study suggests an important role for steroids in autistic women, beyond prenatal development. Clinical implications are discussed",
    "Participants completed the following questionnaires online: a demographic questionnaire where participants reported on their date of birth and birth sex, the Autism Spectrum Quotient (AQ), and a self-report questionnaire, assessing autistic traits (Baron-Cohen et al., 2001). The questionnaire contains 50 items, each of them scores 1 if the respondent records the autistic-like behavior either mildly or strongly.",
    "What methods did they use to measure the autistic traits in a person ?",
    "The current study examined the link between sex-steroid-related conditions among women with and without an autism diagnosis. It focused on four main indications of sex-steroid imbalance: medical conditions, symptoms of sex-steroid imbalance, puberty onset, and reproductive health. Many of the conditions and symptoms, such as puberty onset, menstrual length, and prediabetes symptoms, were found to be associated with having an autism diagnosis or autistic traits. The study suggests an important lifetime function of sex-steroids for autistic women and promotes our understanding of the physical symptoms and medical conditions co-occurring within autistic women. These findings have important im- plications for healthcare awareness. Prior knowledge of  sex-steroid-related conditions could facilitate early diagnosis and improved prognosis for children and youths diagnosed with autism and contribute to better health outcomes in adulthood. Future studies should further investigate this association and provide a roadmap on how best to introduce these findings into healthcare protocols.",
]


def get_text():
    input_text = st.text_input("You: ", "Hello, how are you?", key="input")
    return input_text


user_input = get_text()
st.session_state["curr"] = 0
if user_input:
    # output = query(
    #     {
    #         "inputs": {
    #             "past_user_inputs": st.session_state.past,
    #             "generated_responses": st.session_state.generated,
    #             "text": user_input,
    #         },
    #         "parameters": {"repetition_penalty": 1.33},
    #     }
    # )
    time.sleep(2)
    # resp = response.pop(st.session_state["curr"])
    # st.session_state["curr"] += 1
    st.session_state.past.append(user_input)
    st.session_state.generated.append("try")

if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(response[i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
