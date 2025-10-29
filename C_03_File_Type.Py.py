# asks the user for file type (integer / image / text / xxx)
def get_filetype():
    response = input("File type: ").lower()

    #check for 'i' or the exit code
    if response == "xxx" or response == "i":
        return response

    elif response in ['integer', 'int']:
        return "integer"


    # check for an image...
    elif response in ['image', 'picture', 'img']:
        return "image"

    #check for text...
    elif response in ["text", 'txt', 't']:
        return "text"

        #if the response is invalid output an error
    else:
        print("please enter a valid file type")


    # Main routine goes here
    while True:
        file_type = get_filetype()
        print(f"You chose {file_type}")

        if file_type == "xxx":
            break
