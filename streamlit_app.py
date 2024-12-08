import streamlit as st
import pandas as pd
import openai 

def chat(client):
    input_sentence = st.text_input("Enter your sentence here")
    prompt = "Here is a sentence" + input_sentence + """ 
    I want you to turn this into Old English, Middle English, Early Modern English and Modern English.
    The response should only include the type and the sentences
    It should look like this -> Old English: "Sentence" """
    messages_so_far = [
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages_so_far,
        temperature=0.8,
        )
    return response.choices[0].message.content
client = openai.OpenAI(api_key=st.text_input("OpenAI API Key", key="chatbot_api_key", type="password"))


if st.button("Submit Api Key"):
    output = chat(client)
    output_list = output.split('"')
    key_list = []
    value_list = []
    list_index = 0
    for element in output_list:
        if len(element)!=0:
            for i in range(5):
                element = element.lstrip(' ')
            for i in range(5):
                element = element.strip(' ')
        element = element.lstrip('\n')
        element = element.strip('\n')
        element = element.lstrip(':')
        element = element.strip(':')
        if element != '':
            if list_index %2 == 0:
                key_list.append(element)
            else:
                value_list.append(element)
            list_index +=1
    display_dict = {"Type": key_list, "Sentence": value_list}
    df = pd.DataFrame(display_dict)

    df
else:
    pass