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

st.title("How did this sentence look like back then?")
st.write("This little program here will take a sentence you've provided it with.")
st.write("And turn it into a sentence from various period.")
client = openai.OpenAI(api_key=st.text_input("OpenAI API Key", key="chatbot_api_key", type="password"))
agree = st.checkbox("Api Key Inserted")
if agree:
    output = chat(client)
    agree2 = st.checkbox("Sentence Inserted")
    if agree2 :
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

        st.dataframe(df, use_container_width=True)
    else:
        pass
else:
    pass