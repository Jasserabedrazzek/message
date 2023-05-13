import streamlit as st
from validate_email import validate_email
import time

st.set_page_config(
    page_title="Report a bug",
    page_icon=":rotating_light:",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.header("Send your Report")
Email = st.text_input("Enter your Email:")

validé = validate_email(Email)
if Email == '':
	pass
else:
	if validé:
		pass
	else:
		st.error("Failed to verify the email. Invalid email or couldn't check MX records.")
message=st.text_area("Write Your message :",)
send = st.button("send :e-mail:")
if Email == '':
	pass
else:
	if send :
		if message == "":
			st.error("Please write a message.")
		else:
			with st.spinner("Please wait..."):
				time.sleep(10)
			st.success('The message has been sent successfully. Thank you for sharing your opinion.')
		
	
	
st.write()
st.write("---")
st.write("Copyright for this page is reserved. ©")