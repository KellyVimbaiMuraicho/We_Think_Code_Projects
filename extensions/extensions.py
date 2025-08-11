
file_name = input("What is your filename ?")
 
match file_name.rsplit(".", 1):# splits the file_name string from the right, at the first occurrence of a period (.).
    case [_, "gif"]:  # Matches a list with two elements, with the second being "gif"
        print("image/gif")
    case [_, "jpg"]:
        print("image/jpeg")
    case [_, "jpeg"]:
        print("image/jpeg")
    case [_, "png"]:
        print("image/png")
    case [_, "pdf"]:
        print("application/pdf")
    case [_, "txt"]:
        print("text/plain")
    case [_, "zip"]:
        print("application/zip")
    case _:
        print("application/octet-stream")







