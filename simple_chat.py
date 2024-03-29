import tkinter as tk
from threading import Thread
import socket

def receive():
    """Handle receiving messages from the server."""
    while True:
        try:
            msg = client_socket.recv(1024).decode("utf8")
            msg_list.insert(tk.END, msg)
        except OSError:  # Possibly client has left the chat.
            break

def send(event=None):
    """Handle sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        window.quit()

# ----Now comes the sockets part----
HOST = 'localhost'
PORT = 33000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

receive_thread = Thread(target=receive)
receive_thread.start()

# Tkinter GUI setup
window = tk.Tk()
window.title("Chat")

messages_frame = tk.Frame(window)
my_msg = tk.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbar = tk.Scrollbar(messages_frame)  # To navigate through past messages.

msg_list = tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tk.Entry(window, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tk.Button(window, text="Send", command=send)
send_button.pack()

window.mainloop()
