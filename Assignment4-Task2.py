input_text = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(input_text + "\n")
print("Data successfully written to output.txt.\n")


append_text = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(append_text + "\n")
print("Data successfully appended.\n")


print("Final content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)