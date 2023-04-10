import streamlit as st
import tensorflow as tf
import os
import asyncio
from PIL import Image

image_icon = Image.open('temp/image/icon-side.png')

st.set_page_config(
    page_title='Text Generator Tugas Akhir', 
    layout='wide', 
    initial_sidebar_state='auto', 
    page_icon=image_icon)

@st.cache(allow_output_mutation=True)
def load_model():
    model_path = 'temp/model/10_32_GRU-biLSTM_16_16_64'
    model = tf.saved_model.load(model_path)
    return model

model = load_model()

with st.sidebar:
    st.image(image_icon)
    st.title('Text Generator Tugas Akhir')
    st.sidebar.caption("Tell your data story with style.")
    choice = st.selectbox('Main Menu', ['Home', 'Generate Text', 'About'])
    st.info('This web application helps you generate text freely!')
    st.sidebar.markdown("Developed by [Bastian Armananta](https://www.linkedin.com/in/bastian-armananta/)")

if choice == 'Home':
    st.image(os.path.join('temp/image','subheader-home.png'), use_column_width  = True)
    st.markdown('<h1>Home Page</h1>', unsafe_allow_html=True)
    st.markdown("---")
    with st.container():
        st.caption('This website application is implementation of NLP project for generating text with thesis dataset, We used deep learning model such as [LSTM](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM) and [GRU](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GRU) for making Text Generate.') 
        st.caption('Dataset is taken from thesis that has been published in the [IT Telkom Purwokerto repository](https://repository.ittelkom-pwt.ac.id/) from 2017 to 2022.')
    
if choice == 'Generate Text':
    async def generate_text(start_word, model, num_words):
        states1 = None
        states2 = None
        states3 = None
        states4 = None
        next_char = tf.constant([start_word])

        list_kalimat = []

        result = [next_char]

        for n in range(num_words):
            next_char, states = model.generate_one_step(next_char, 
                                                        states1=states1, 
                                                        states2=states2, 
                                                        states3=states3, 
                                                        states4=states4)
            result.append(next_char)

            states1 = states[0]
            states2 = states[1]
            states3 = states[2]
            states4 = states[3]

        result = tf.strings.join(result, separator=" ")

        list_kalimat.append(result[0].numpy().decode('utf-8'))

        return list_kalimat

    st.title("Generate Text")
    st.markdown('This app generate text using Deep Learning LSTM and GRU. You can find the code on [GitHub](https://github.com/bastianarmananta).')

    if 'start_word' not in st.session_state:
        st.session_state['start_word'] = ''
    
    if 'num_words' not in st.session_state:
        st.session_state['num_words'] = 15
    
    start_word = st.text_area(label='Insert some text', 
                           placeholder="Insert some text", 
                           label_visibility='hidden',
                           value=st.session_state['start_word'])
    
    st.session_state['start_word'] = start_word
    
    num_words = st.number_input('Maximum length', min_value=1, max_value=100, value=st.session_state['num_words'])
    st.session_state['num_words'] = num_words
    
    generate_button = st.button('Generate Text', type='primary')
    st.markdown("---")

    if generate_button:
        with st.spinner():
            progress_bar = st.progress(0)
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            generated_text = loop.run_until_complete(generate_text(start_word, model, num_words))
            text_length = len(generated_text[0])
            height_factor = 0.32
            st.text_area('Generated Text',
                        height=int(text_length*height_factor),
                        value=generated_text[0])
            progress_bar.progress(100)

if choice == 'About':
    st.image(os.path.join('temp/image','subheader-about.png'), use_column_width  = True)
    st.title('About')
    st.markdown("---")
    with st.container():
        st.caption('This project resulting text generation model build by LSTM and GRU and using bidirectional architecture.') 
        st.caption('Model resulting val_loss 1.1427 and val_acc 0.8680, due to high loss text generated by model still be absurd and can be random sentence.')
        st.caption('This project can be improved by adding more dataset make some fine tunning model.')
        st.write('\n')
        st.caption('<center><footer>&copy; Bastian Armananta</footer><center>', unsafe_allow_html=True)