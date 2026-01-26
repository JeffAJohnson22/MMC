# Jeff Johnson PA2

# sklearn is a ready-made machine learning toolkit that we are importing to uses its methods.

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.naive_bayes import MultinomialNB

def statistical_classifier(train_messages, train_labels, test_message):

    # CountVectorizer counts how many times each word appears in each sentence puts it in a matrix of integers.
    vectorizer = CountVectorizer()

    # Learns what words exist in all mys training messages and builds a dictionary of words and their frequencies.
    X_train = vectorizer.fit_transform(train_messages)

    # An empty model that will be filled with the training data.
    model = MultinomialNB()
    
    # Passing in the training data I made to the model to learn the word frequencies and then uses that to predict if a message is spam or not
    model.fit(X_train, train_labels)

    # Transforms the message the user give into numbers for the model to understand
    X_test = vectorizer.transform([test_message])

    # Predicts if the message is spam or not
    prediction = model.predict(X_test)[0]

    return prediction

def main():

    train_messages = [
        "Congratulations! You've won a free ticket to Barbados. Click here to claim.",
        "Dear friend, I am a Nigerian prince in need of your help to transfer funds.",
        "Limited time offer! Buy now and get 50% off on all products.",
        "Buy my course to learn how to make money online.",
        "$$$$$$$ WINNER WINNER WINNER $$$$$$$",
        "Hey, how are you doing today?",
        "Don't forget our date is tomorrow.",
        "Can you send me the report by the end of the day?",
        "My name is Jeff Johnson and I am a student at the Merrimack College.",
        "Can you buy me a new lock for my bike?",
    ]

    train_labels = [
        "spam",
        "spam",
        "spam",
        "spam",
        "spam",
        "not spam",
        "not spam",
        "not spam",
        "not spam",
        "not spam",
    ]
    
    user_message = input("Enter your message:")

    result = statistical_classifier(train_messages, train_labels, user_message)

    print(f"The message is classified as: {result}")
    
main()

# 1: What’s better, what’s more scalable, why?
# Simply because I can pass in as much data as I need/want makes this better more data in the sense that I have full sentences going in.
# The training data is scalable because I can add more data as I need/want.

# 2: Explain what each library is used for.
# CountVectorizer is used to count the number of times each word appears in each sentence
# MultinomialNB is used to predict if a message is spam or not based on the word frequencies in the training data
# a user gives it.

# 3: Compare this approach to your Spam Classifier approach in week 1.
# In comparison to the Spam Classifier approach in week 1, week 2 is just more real world applicable. Week 1
# is essentially hard coded while this is able to scale/evolve with the data. Week 2 is looking for patterns
# where week 1 is looking for specific words.

# Bonus:
# 1: added two lists
# 2: added 10 examples 5 spam and 5 not spam
# 3: added a none spam example with the word buy

# 4: how adding more diverse data changed the result of your test_message classification.
# I think add mire diverse data give the model the ability to judge a message better. For example 
# you asked us to give it a message with a known spam buzz word of buy. However the ML is able to 
# figure out context with its judgement so it can decide if its spam or not. Also giving it a 
# message out of left field like I did with the Dragon Ball Z a basic model would probably say its spam.