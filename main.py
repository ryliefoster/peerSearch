import myData as md
import myFriends as mf
import searchTable as st
import socket


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
                        result += e.get_name() + "\n" + e.get_link() + "\n" + e.get_desc() + "\n"
                    conn.sendall(result.encode("utf-8"))
                    conn, addr = s.accept()

    elif choice == "q":
        while True:
            query = input("Query:\n")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(("127.0.0.1", 20000))
                s.sendall(query.encode("utf-8"))
                data = s.recv(4096).decode("utf-8")
            print(data)
