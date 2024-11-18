import streamlit as st
import pandas as pd
import time

#stolen function
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)



# Title of the app
st.title('McClure Water Resevoir Level')

# Load CSV file named "Joey"
try:
    df = pd.read_csv("data_to_send.csv")
    st.write("Data from data_to_send.csv:")
    st.write(df)
    x = st.slider(';)', min_value=10, max_value=500) 
    st.image("OIP.jpg", width=x)
    st.write('https://docs.streamlit.io/get-started/fundamentals/main-concepts')

    #sample code I stole from the docs:
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
    
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())
         # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        response = f"Chadi Harmouche: c'mon guys"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    # end sample code I stole

    
    # Dropdowns for X and Y axes selection
    columns = df.columns.tolist()
    x_axis = st.selectbox('Select column for X-axis', columns)
    y_axis = st.selectbox('Select column for Y-axis', columns)
    
    # Choose chart type: Bar Chart or Line Chart
    chart_type = st.selectbox('Select chart type', ['Bar Chart', 'Line Chart'])
    
    # Display chart based on user selections
    if chart_type == 'Bar Chart':
        st.bar_chart(df[[x_axis, y_axis]].set_index(x_axis))
    elif chart_type == 'Line Chart':
        st.line_chart(df[[x_axis, y_axis]].set_index(x_axis))

except FileNotFoundError:
    st.error("The file 'Joey.csv' was not found. Please ensure the file is available in the directory.")
