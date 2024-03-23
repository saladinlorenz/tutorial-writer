from openai import OpenAI  # Importing the OpenAI library
import re  # Importing the regular expression library
from txt2html import txt2html  # Importing the custom function to convert text to HTML
import os

# Establishing connection with the local LMStudio server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

filelog = ""  # Initializing a variable to log the conversation

# Path of the folder to create
folder_path = "outpu"

# Check if the folder does not already exist
if not os.path.exists(folder_path):
    # Create the folder
    os.makedirs(folder_path)

# Prompting the user to enter a request for a tutorial
user_input = input("Enter a request for a tutorial: ")

filelog += f"{user_input}\n\n"  # Logging user input

try :
    filename = user_input
except:
    filename = user_input[:50] + ".txt"  # Generating a filename from user input

print(user_input)

# Creating a completion with the user request
completion = client.chat.completions.create(
    model="local-model",
    messages=[
        {"role": "system", "content": "Break down the response into concise tasks with clear titles, each starting with Task 1:, Task 2:, and so forth, avoiding excessive detail."},
        {"role": "user", "content": user_input}
    ],
    temperature=0.7,
)

# Getting the response generated by the model
response = completion.choices[0].message.content
print((response))
print("-----------------------------")

# Creating a list to store the steps
step_list = []

# Using regular expressions to extract tasks
step_list = re.findall(r'\*\*Task \d+:.*?(?=\*\*Task \d+:|\Z)', response, re.DOTALL)

# Displaying the extracted tasks
for step in step_list:
    filelog += step + "\n"
    print(step + "\n")

filelog += "\n\n\n"

# Displaying the extracted tasks
for step in step_list:
    print()
    print(step + "\n")
    user_input = step

    # Creating an initial story
    history = [
        {"role": "system", "content": "Brimming with intelligence, you serve as an esteemed assistant, known for imparting invaluable insights and guidance"},
        {"role": "user", "content": user_input},
    ]

    while True:
        if history[-1]["content"]:  # Checking if the content of the last message is not empty

            completion = client.chat.completions.create(
                model="local-model",
                messages=history,
                temperature=0.7,
                stream=True,
            )

            new_message = {"role": "assistant", "content": ""}

            for chunk in completion:
                if chunk.choices[0].delta.content:
                    print(chunk.choices[0].delta.content, end="", flush=True)
                    new_message["content"] += chunk.choices[0].delta.content

            history.append(new_message)
            filelog += new_message["content"] + '\n\n\n'
        else:
            break  # If the content is empty, exit the loop
filename = os.path.join(folder_path, filename)
# Writing the conversation log to a file
with open(filename, "w", encoding="utf-8") as file:
    file.write(filelog)

# Converting the conversation log to HTML
txt2html(filename)