# Jeff Johnson

def symbolic_classifier(input_string):
    spam_keywords = ["buy now", "free", "click here", "winner", "limited time", 
                     "offer", "congratulations", "act now", "money back"]
    
    message_length = len(input_string)
    
    if len(input_string) > 0:
        uppercase_ratio = sum(1 for c in input_string if c.isupper()) / len(input_string)
        if uppercase_ratio > 0.5 and len(input_string) > 5:
            return "spam"
    
    if input_string.count('!') >= 2:
        return "spam"
    
    if input_string.count('$') >= 2:
        return "spam"
    
    if message_length < 5 or message_length > 200:
        return "spam"
    
    for keyword in spam_keywords:
        if keyword in input_string.lower():
            return "spam"
    
    return "not spam"


def main():
    message = input("Enter a message: ")
    result = symbolic_classifier(message)
    print(result)


if __name__ == "__main__":
    main()