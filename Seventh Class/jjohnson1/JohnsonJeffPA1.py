# Jeff Johnson

def symbolic_classifier(input_string):
    """
    Classifies a message as spam or not spam.
    
    Args:
        input_string: The email or text message
        
    Returns:
        spam or not spam
    """
    
    message_length = len(input_string)
    
    # Check for spam keywords
    spam_keywords = ["buy now", "free", "click here", "winner", "nigerian", "prince", "vote"]
        
    # 1 Check for spam keywords
    for keyword in spam_keywords:
        if keyword in input_string.lower():
            return "spam"
        
    # 2 Check message length if it too short or too long we call it spam
    if message_length < 5 or message_length > 300:
        return "spam"
    
    # 3 Check for excessive capitalization
    if message_length > 0:
        
        # Check for excessive punctuation
        if input_string.count('!') >= 2 or input_string.count('$') >= 2:
            return "spam"
        
        # Count how many uppercase letters are in the message
        count_uppercase = 0
        for letter in input_string:
            if letter.isupper():
                count_uppercase += 1
        
        # Calculate how much of the message is uppercase
        uppercase_amount = count_uppercase / message_length
        
        # If more than half the message is uppercase I think we call it spam
        if uppercase_amount > 0.5:
            return "spam"
    
    # If none of the spam rules happen then we call it not spam
    return "not spam"


def main():
    """
    Main function that asks for input
    """
    # Ask the user for a message
    message = input("Enter a message: ")
    
    # Call the function
    result = symbolic_classifier(message)
    
    # Show the result
    print(result)

# Entry point of the program
if __name__ == "__main__":
    main()