from itertools import zip_longest
import streamlit as st
from streamlit_chat import message
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
openapi_key = st.secrets["OPENAI_API_KEY"]

# Set streamlit page configuration
# Set streamlit page configuration
st.set_page_config(page_title="Endicode ChatBot")
st.title("Endicode chatbot")

# Social media profile links
github_link = "[GitHub Profile](https://github.com/abdullah0325)"
linkedin_link = "[LinkedIn Profile](https://www.linkedin.com/in/muhammad-abdullah-41b82028b/)"
facebook_link = "[Facebook Profile](https://www.facebook.com/profile.php?id=100090638882853)"

# Display social media profile links in the sidebar
st.sidebar.title("Social Profiles")
st.sidebar.write(github_link, unsafe_allow_html=True)
st.sidebar.write(linkedin_link, unsafe_allow_html=True)
st.sidebar.write(facebook_link, unsafe_allow_html=True)



# Initialize session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []  # Store AI generated responses

if 'past' not in st.session_state:
    st.session_state['past'] = []  # Store past user inputs

if 'entered_prompt' not in st.session_state:
    st.session_state['entered_prompt'] = ""  # Store the latest user input

# Initialize the ChatOpenAI model
chat = ChatOpenAI(
    temperature=0.5,
    model_name="gpt-3.5-turbo",
    openai_api_key=openapi_key, 
    max_tokens=100
)


def build_message_list():
    """
    Build a list of messages including system, human and Ai chatbot of endicode it company messages.
    """
    # Start zipped_messages with the SystemMessage
    zipped_messages = [SystemMessage(
        # content="You are a helpful AI assistant talking with a human. If you do not know an answer, just say 'I don't know', do not make up an answer.")]
        content = """ when the user ask  hi  tell him Welcome to the Endicode Chatbot, developed by Muhammad Abdullah you  can ask any question about endicod  and muhammad abdullah. I am here to assist you as a knowledgeable consultant. 

---

**About Endicode:**

Endicode is your gateway to digital excellence, specializing in delivering innovative IT solutions to empower your business. Our commitment to excellence and innovation drives us to offer a comprehensive suite of solutions that cater to various industries and sectors.

---

**Our Services:**

1. **Android Development:** Crafting cutting-edge Android applications tailored to your requirements.
2. **Ecommerce Website Development:** Creating engaging and secure ecommerce platforms for business growth.
3. **Web Security Solutions:** Ensuring your online presence is protected with robust security measures.
4. **Shopify Website Designing:** Designing captivating and functional Shopify websites.
5. **Search Engine Optimization:** Enhancing online visibility and driving organic traffic.
6. **WordPress Designing:** Developing dynamic and user-friendly WordPress websites.
7. **Fixing Web Issues:** Resolving web-related issues efficiently to keep your business running smoothly.
8. **Web Development & Designing:** Crafting bespoke websites tailored to your specific needs.

---

**Company Information:**

Endicode is committed to digital excellence, offering innovative IT solutions to transform businesses.
    offical site of  endicod is    https://endicode.com/
- **Founder and CEO:** Muhammad Awais
- **Location:** Charsadda, KPK, Pakistan
- **Project Manager:** Muhammad Soleman
- **Marketing Manager and Developer:** Muhammad Abdullah
- **Contact Number of company is  +923118914131 (Muhammad Abdullah's WhatsApp: +923251851838)
- **LinkedIn Profile:** [Muhammad Abdullah](https://www.linkedin.com/in/muhammad-abdullah-41b82028b/)
- **GitHub Profile:** [Abdullah0325](https://github.com/abdullah0325/)
- **Education:** Muhammad Abdullah is also a student of Advanced AI at Hoop to Skills and Web 3.0, Generative AI, and Metaverse at PIAIC. His notable teachers include Sir Zia Khan, Sir Danyal Nagori, Sir Irfan Malik, Sir Dr. Sheraz Naseer, and Sir Haris.

---

Thank you for choosing Endicode. If you have any questions or require assistance, feel free to ask! """
    )]


    # Zip together the past and generated messages
    for human_msg, ai_msg in zip_longest(st.session_state['past'], st.session_state['generated']):
        if human_msg is not None:
            zipped_messages.append(HumanMessage(
                content=human_msg))  # Add user messages
        if ai_msg is not None:
            zipped_messages.append(
                AIMessage(content=ai_msg))  # Add AI messages

    return zipped_messages


def generate_response():
    """
    Generate AI response using the ChatOpenAI model.
    """
    # Build the list of messages
    zipped_messages = build_message_list()

    # Generate response using the chat model
    ai_response = chat(zipped_messages)

    return ai_response.content


# Define function to submit user input
def submit():
    # Set entered_prompt to the current value of prompt_input
    st.session_state.entered_prompt = st.session_state.prompt_input
    # Clear prompt_input
    st.session_state.prompt_input = ""


# Create a text input for user
st.text_input('YOU: ', key='prompt_input', on_change=submit)


if st.session_state.entered_prompt != "":
    # Get user query
    user_query = st.session_state.entered_prompt

    # Append user query to past queries
    st.session_state.past.append(user_query)

    # Generate response
    output = generate_response()

    # Append AI response to generated responses
    st.session_state.generated.append(output)


# Display the chat history
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        # Display AI response
        message(st.session_state["generated"][i], key=str(i))
        # Display user message
        message(st.session_state['past'][i],
                is_user=True, key=str(i) + '_user')








# import streamlit as st

# # Set streamlit page configuration
# st.set_page_config(page_title="Hope to Skill ChatBot")
# st.title("AI Mentor")

# # Create a sidebar for user information (optional)
# st.sidebar.title("User Information")
# st.sidebar.write("Name: Muhammad Abdullah")
# st.sidebar.write("Age: 21")
# st.sidebar.write("Location: Upper Dir, Khyber Pakhtunkhwa")
# st.sidebar.write("Education: Computer Science")

# # Create a text input for user
# st.text_input('YOU: ', key='prompt_input')

# # Display the chat history
# if st.session_state['generated']:
#     for i in range(len(st.session_state['generated'])-1, -1, -1):
#         # Display AI response
#         st.write(st.session_state["generated"][i])
#         # Display user message
#         st.write(st.session_state['past'][i])
