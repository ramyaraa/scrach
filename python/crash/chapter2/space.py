print("adam")
print("\tadam")  # tab space \t
print("programming languige: \n\t1.python\n\t2.C\n\t3.javascript") # new line \n and tab space


name = "     adam     "
# its just work for 1 letter if we have to letter the space bettwen cant be remove
print(name.strip()) # remove space before the letter and after the letter
print(name.rstrip()) # remove space before the letter 
print(name.lstrip()) # remove space after the letter


url = "https://adam22.net"
file = "crash.pdf"
print(url.removeprefix("https://")) #remove prefix https://
print(file.removesuffix(".pdf")) #remove suffix .pdf

