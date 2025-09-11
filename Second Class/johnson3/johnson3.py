import glob

def SingleWordCheck(userWord):
    if " " in userWord:
        return False
    else:
        return True
 
def AllWordCount(words):
    wordCounter = {}
    for word in words:
        if word in wordCounter:
            wordCounter[word] +=1
        else:
            wordCounter[word] = 1

    return sorted(wordCounter.items(), key=lambda x: x[1], reverse=True)[:5]

def SingleWordCount(text, userWord):
    count = text.count(userWord)
    return count

def readTextFile():
    with open("./test.txt" , 'r') as file:
        return file.read()

def saveTextFile(updateContent):
    with open("./test.txt", "w") as file:
        file.write(updateContent)

def ReplaceAWord(userWord, replacement):
    updateContent = readTextFile().replace(userWord, replacement)
    saveTextFile(updateContent)

def AddAWord(userWord):
    updateContent = readTextFile().__add__(userWord)
    saveTextFile(updateContent)

def DeleteAWord(userWord):
    updateContent = readTextFile().replace(userWord, "", 1)
    saveTextFile(updateContent)
        
def HighlightAWord(userWord):
    updateContent = readTextFile().replace(userWord, f"**{userWord}**")
    saveTextFile(updateContent)

def main():
    try:
        files = glob.glob("./test.txt")
        text = []

        if not files:
            raise FileNotFoundError("The file 'test.txt' was not found.")
        
        for file in files:
            with open(file, "r", encoding='ISO-8859-1') as f:
                text.append(f.read())

        text = text[0].split()

        while True:
            print("===Edit Menu===")
            print("1: Top 5 most common words")
            print("2. Single Word Frequency")
            print("3. Replace a word")
            print("4. Add Text")
            print("5. Delete Text")
            print("6. Highlight Text")  
            print("7. Exit Program")

            choice = int(input("Select an option from above: ")) 
            
            match choice:
                case 1:
                    top5 = AllWordCount(text)
                    print("The 5 most common words are: ")
                    
                    for word, count in top5:
                        print(f"{word}: {count}")
                case 2:
                    userWord = input("Give me a single word to search its frequency : ")
                    
                    if SingleWordCheck(userWord):
                        wordCount = SingleWordCount(text, userWord)
                        print(f"The word {userWord} shows up {wordCount} times.")
                    else:
                        print("Has to be a single word.")
                case 3: 
                    userWord = input("Give me a word to target to replace in the file: ")
                    replacement = input(f"Give me the word to replace {userWord} with in the file: ")

                    if SingleWordCheck(userWord) and SingleWordCheck(replacement):
                        ReplaceAWord(userWord, replacement)
                        wordCount = SingleWordCount(text, userWord)
                        print(f"{wordCount} counts of the word {userWord} replaced with the word {replacement}.")
                    else:
                        print("Has to be a single word.")
                case 4:
                    userWord = input("Give me a word to add to the file: ")

                    if SingleWordCheck(userWord):
                        AddAWord(userWord)
                        print(f"You have added the word {userWord} to the text file.")
                    else:
                        print("Has to be a single word.")
                case 5:
                    userWord = input("Give me a word to delete from the file: ")

                    if SingleWordCheck(userWord):
                        DeleteAWord(userWord)
                        print(f"You have deleted the first instance of the word {userWord} from the text file.")
                    else:
                        print("Has to be a single word.")
                case 6: 
                    userWord = input("Give me a word to Highlight in this file: ")

                    if SingleWordCheck(userWord):
                        HighlightAWord(userWord)
                        print(f"You have deleted the first instance of the word {userWord} from the text file.")
                    else:
                        print("Has to be a single word.")
                case 7: 
                    print("Exiting Program.")
                    break
                case _:
                    print("Invalid entry try again")
    except FileNotFoundError:
        print("The file 'test.txt' was not found.")

if __name__ == '__main__':
    main()