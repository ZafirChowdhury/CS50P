user_input = input("File name: ").lower().strip().split(".")
ex = user_input[-1]

ex_dic = {
    "gif":"image/gif",
    "jpg":"image/jpeg",
    "jpeg":"image/jpeg",
    "png":"image/png",
    "pdf":"application/pdf",
    "txt":"text/plain",
    "zip":"application/zip"
}

print(ex_dic.get(ex, "application/octet-stream"))