import pandas as pd

# Load ur data into a data frame
df = pd.read_csv("health_data.csv")
# print(df)

print("Healthbot: Hello there, i am your Health Assistant bot. Ask me about any symptoms")

while True:
    # 1. Get the user input and store the same into a variable
    user_text = input("\n You: ").lower()

    # 2. Check if the user wants to exit from the converstion
    if user_text == "quit":
        print("Healthbot: Goodbye! Thank you for your consultance. All the best!")
        break

    # Create a variable that will store the details structured in the csv file
    found_answer = False

    # Come up with a loop that loops through the entire data frame created before
    for index, row in df.iterrows():
        # Clean up the keywords from the CSV row
        keywords_list = str(row['Keywords']).split(',')

        # Below we check every key word in that given row(keywords)

        for word in keywords_list:
            clean_word = word.strip().lower()
            
            # If the key word is inside the user's sentence
            if clean_word in user_text:
                print("Healthbot: ", row["Response"])
                found_answer = True
                break # Stop looking at other keywods
        if found_answer:
            break # Stop looking at other answers since we already found a match

    # 4. If we went through the entire?whole CSV and we never found a match of the keywords,
    # we need to display a message to the user
    if not found_answer:
        print("Healthbot: Sorry, I did not get you clearly. Perhaps you can try asking the question in anothr simpler way si that i can help you.")
        