import streamlit as st
from generator import password_generator
from generator import passphrase
from strength import feedback_suggestions,feedback_warning,score,cracking_time_offline,cracking_time_online,pattern,attempts,password_strength,score1
import base64

def get_base64(path):
    with open(path, "rb") as image:
        return base64.b64encode(image.read()).decode()

background = get_base64("assets/background.webp")

with open("styles.css") as f:
    css = f.read()

css = css.replace("{background_image}", background)

st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True
)


st.title("Password Security Toolkit")
 #section-1

st.header("Instant Password Generator")
button_col, password_col = st.columns([1,5])
with button_col:
    generate_instant=st.button("Generate",key="12@3")
    st.write("")
if generate_instant:
    generated_password=password_generator()
    while score1(generated_password)<=2:
        generated_password=password_generator()
    with password_col:
        st.code(generated_password) #gives the copy_to_clipboard option
st.divider()

#section-2

st.header("Custom Password Generator")
st.caption("Specify your preferred password length below.")

col_text,col_input,col_spacer=st.columns([2,1,3])
with col_text:
    st.markdown("Enter password length:")
with col_input:
    password_length=st.text_input(label="length",value=20,label_visibility="collapsed")
custom_generate_col, custom_password_col = st.columns([1,5])
with custom_generate_col:
    generate_custom = st.button("Generate", key="12@4")
    st.write("")
if generate_custom:
    if password_length.isdigit():
        length=int(password_length)
        if length>8:
            custom_password =password_generator(length)
            while score1(custom_password)<=2:
                custom_password =password_generator(length)
            with custom_password_col:
                st.code(custom_password)
        else:
            with custom_password_col:
                st.error("Please enter a length greater than 8.")
    else:
        with custom_password_col:
            st.error("Please enter a valid number for the length")
st.divider()

#section-3

st.header("Word-Based Passphrase Generator")
st.caption("Create memorable passphrases using the given words and mixed cases and random symbols.")
passphrase_input_col, passphrase_output_col = st.columns(2)
words=[]
with passphrase_input_col:
    left1,left2=st.columns([3,1])
    with left1:
        st.markdown("Enter number of words:")
    with left2:
        no_of_words=st.text_input(label="count",value=4,label_visibility="collapsed")
    if no_of_words!="0":
        if no_of_words.isdigit():
            count=int(no_of_words)
            while count>0:
                words.append(st.text_input(label=f"{count}",value="abc",label_visibility="collapsed"))
                count-=1
            generated_passphrase=passphrase(words)
        else:
            st.error("Please enter a valid number")
    else:
        st.error("Please enter a valid number")
with passphrase_output_col:
    generate3=st.button("Generate",key="12@34")
    if generate3 and no_of_words.isdigit() and int(no_of_words)!=0:
        st.code(generated_passphrase)
st.divider()

#section-4

st.header("Password Strength Meter")
password_to_check=st.text_input("Enter a password to analyze:")
strength_label_col, strength_value_col=st.columns([1,4])
with strength_label_col:
    st.markdown("Password Strength:")

guess_label_col, guess_value_col=st.columns([1,2])
with guess_label_col:
    st.markdown("Estimated Number of Guesses:")
pattern_label_col, pattern_value_col=st.columns([1,4])
with pattern_label_col:
    st.markdown("Detected Pattern:")
st.markdown("Estimated Crack Time:")
online_label_col, online_value_col=st.columns([2,11])
with online_label_col:
    st.markdown("Online Attack:")
offline_label_col, offline_value_col=st.columns([2,11])
with offline_label_col:
    st.markdown("Offline Attack:")
warning_label_col, warning_value_col=st.columns([2,9])
with warning_label_col:
    st.markdown("Security Warning:")
suggestion_label_col, suggestion_value_col=st.columns([4,11])
with suggestion_label_col:
    st.markdown("Improvement Suggestions:")
if password_to_check:
    password_strength(password_to_check)
    with strength_value_col:
        st.markdown(score())
    with guess_value_col:
        st.markdown(attempts())
    with pattern_value_col:
        st.markdown(pattern())
    with online_value_col:
        st.markdown(cracking_time_online())
    with offline_value_col:
        st.markdown(cracking_time_offline())
    with warning_value_col:
        st.markdown(feedback_warning())
    with suggestion_value_col:
        st.markdown(feedback_suggestions())
                
st.markdown("""
---
###  Built by  **D.Hemanth Reddy**

🔗 [GitHub](https://github.com/hemanth24408)  

Password strength analysis powered by **zxcvbn**
""")



#to run the file enter the command in treminal: streamlit run your_filename.py or : Ctrl + `