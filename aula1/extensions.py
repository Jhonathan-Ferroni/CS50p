file = input("File name: ")

file = file.lower().strip()

# Obter os últimos 3 caracteres
last_three = file[-3:]

match last_three:
    case "jpg" | "peg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "gif":
        print("image/gif")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
