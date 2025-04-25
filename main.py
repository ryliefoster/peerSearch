import myData as md
import myFriends as mf
import searchTable as st
import socket

resultBuffer = "result00000000result00000000result"
bufflen = len(resultBuffer)

if __name__ == "__main__":
    choice = ""
    choice = input("Would you like to (h)ost your data or make a (q)uery?\n")
    if choice[0] == "h":
        HOST = input("What IP would you like to use?\n")
        PORT = int(input("What port would you like to use?\n"))
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    results = md.myTable.search(data.decode("utf-8"))
                    result = ""
                    for e in results:
                        result += e.get_name() + "\n" + e.get_link() + "\n" + e.get_desc() + "\n" + resultBuffer
                    conn.sendall(result.encode("utf-8"))
                    conn, addr = s.accept()

    elif choice == "q":
        while True:
            query = input("Query:\n")
            results = md.myTable.search(query)
            result = ""
            for e in results:
                result += "From your data:\n" + e.get_name() + "\n" + e.get_link() + "\n" + e.get_desc() + "\n"
            for friend in mf.friends:
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.connect((friend[1], friend[2]))
                        s.sendall(query.encode("utf-8"))
                        data = s.recv(4096).decode("utf-8")
                        print(data)
                    entStart = 0
                    while True:
                        entEnd = data[entStart:].find(resultBuffer)
                        ent = data[entStart:entEnd]
                        linkStart = ent.find("www.")
                        if linkStart == -1:
                            break
                        linkEnd = linkStart + ent[linkStart:].find("\n")
                        link = data[linkStart:linkEnd]
                        if not link in result:
                            result += f"From {friend[0]}:\n {data[:entEnd]}"
                        entStart = entEnd + bufflen
                except:
                    print(f"{friend[0]} not connected.")
            if len(result) == 0:
                print("No matches found.")
            else:
                print(result)

