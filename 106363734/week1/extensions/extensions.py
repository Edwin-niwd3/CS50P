extension = input("File name: ")
extension = extension.strip()
extension = extension.lower()
#look for the . since that is what seperates the file name and type
period_location = extension.rfind('.')

if extension[period_location:len(extension)] == ".gif":
    print("image/gif")
elif extension[period_location:len(extension)] == ".jpg" or extension[period_location:len(extension)] == ".jpeg":
    print("image/jpeg")
elif extension[period_location:len(extension)] == ".png":
    print("image/png")
elif extension[period_location:len(extension)] == ".pdf":
    print("application/pdf")
elif extension[period_location:len(extension)] == ".txt":
    print("text/plain")
elif extension[period_location:len(extension)] == ".zip":
    print("application/zip")
else:
    print("application/octet-stream")
