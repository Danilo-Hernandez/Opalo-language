import opalo

while True:
    text = input("opalo > ")
    if text.strip() == "": continue
    result, error = opalo.run("<stdin>",text)

    if error:
        print(error.as_string())