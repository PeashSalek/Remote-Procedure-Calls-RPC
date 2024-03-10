import xmlrpc.client

# Connect to the server
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Function to interact with the server
def add_or_create_note():
    topic_name = input("Enter topic name: ")
    note_name = input("Enter note name: ")
    note_text = input("Enter note text: ")
    timestamp = input("Enter timestamp: ")
    server.append_or_create_topic(topic_name, note_name, note_text, timestamp)

def get_notes():
    topic_name = input("Enter topic name: ")
    notes = server.get_notes_by_topic(topic_name)
    if isinstance(notes, list):
        for note in notes:
            print(f"Note Name: {note['name']}")
            print(f"Text: {note['text']}")
            print(f"Timestamp: {note['timestamp']}")
    else:
        print(notes)

def query_wikipedia():
    search_term = input("Enter search term: ")
    results = server.query_wikipedia(search_term)
    if isinstance(results, list):
        print("Wikipedia search results:")
        for result in results:
            print(result['title'])
            print(result['snippet'])
            print("----------")
    else:
        print(results)

# Main menu
while True:
    print("\n1. Add or create note")
    print("2. Get notes by topic")
    print("3. Query Wikipedia")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_or_create_note()
    elif choice == "2":
        get_notes()
    elif choice == "3":
        query_wikipedia()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
