# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO INTERACT WITH ChatGPT using the library "openai"

# ChatGPT is developed by OpenAI. It is a large language model based on the GPT-3.5 architecture.
# It is a type of AI chatbot that can take input from users and generate solutions similar to
# humans. ChatGPT is well-trained AI that is trained on a large dataset, using that training it
# can be able to perform a wide range of tasks. It is designed to simulate a conversation with a
# human, making it a valuable tool for customer service, personal assistants, and other
# applications where natural language processing is required.

# The module can be installed using the command - pip install openai

# Steps to generate API Keys for communication with ChatGPT using Python openai library
# Step 1: Create an account on OpenAI and log into an account.
# Step 2: After login click on "Personal" on the top-right side and then click on "View API keys".
# Step 3: In the opened page, click on the "Create new secret key" and a secret key is generated.
# Step 4: Copy the generate secret key and save it in a Notepad.


# Importing necessary packages
import openai
from tkinter import *
import tkinter as tk

# Setting your OpenAI API Key
openai.api_key = "<INSERT_YOUR_OPEN_AI_API_KEY>"

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    root.conversationWindow = Text(root, width=50, height=23, bg="snow3")
    root.conversationWindow.grid(row=1, column=0, rowspan=17, columnspan=3, padx=15, pady=15)
    # Making the Text Widget un-editable by setting state parameter of config() to DISABLED
    root.conversationWindow.config(state=DISABLED)
    # Setting some additional configuration to the Text Widget including font and word wrap
    root.conversationWindow.config(font="Calibri 15", wrap="word", foreground="black")

    userMessageLabel = Label(root, text="MESSAGE : ", bg="skyblue4")
    userMessageLabel.grid(row=19, column=0, padx=15, pady=5)

    root.userMessageEntry = Entry(root, width=30, bg="snow3", textvariable=userMessage)
    root.userMessageEntry.grid(row=19, column=1, padx=5, pady=5)
    root.userMessageEntry.config(foreground="black")

    sendButton = Button(root, text="SEND", command=sendMessage)
    sendButton.grid(row=19, column=2, padx=5, pady=15)

# Defining sendMessage() to initiate and display the conversation between user & ChatGPT
def sendMessage():
    # Fetching the user-input message using get()
    inputMessage = userMessage.get()
    # Clearing the user-input field after fetching the message
    root.userMessageEntry.delete(0, END)
    # Appending the user-message into a list in the JSON format
    messagesList.append({"role": "user", "content": inputMessage})
    # Appending the user-message to another list for displaying in Conversation Window
    conversationList.append("User : " + str(inputMessage) + "\n\n")
    # Generating the chat using openai.ChatCompletion.create()
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messagesList)
    # Checking if there's content in chat
    if chat:
        # Storing the response from ChatGPT and adding the response it to the lists
        reply = chat.choices[0].message.content
        messagesList.append({"role": "assistant", "content": reply})
        conversationList.append("System : " + str(reply) + "\n\n")
    # Enabling the Conversation Window by setting state parameter of config() to NORMAL
    root.conversationWindow.config(state=NORMAL)
    # Clearing the window before diplaying the conversation
    root.conversationWindow.delete("1.0", END)
    # Looping through each message in the list and displaying it in Conversation Window
    for message in conversationList:
        # Displaying the Feed Details in the Text Widget
        root.conversationWindow.insert("end", message)
    # Making Conversation Window un-editable again after displaying the conversation
    root.conversationWindow.config(state=DISABLED)

# Creating object of tk class
root = tk.Tk()

# Setting the title, background color, window-size
# & disabling the resizing property
root.title("PythonChatBot")
root.config(background="skyblue4")
root.resizable(False, False)
root.geometry("540x540")

# Creating the tkinter variables
userMessage = StringVar()
# Declaring empty lists
conversationList = []
messagesList = []

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
