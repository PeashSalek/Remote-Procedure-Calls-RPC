from xmlrpc.server import SimpleXMLRPCServer
import xml.etree.ElementTree as ET
import os
import requests

# Function to handle client requests
class NoteServer:
    def __init__(self):
        self.data_file = "notes.xml"
        if not os.path.exists(self.data_file):
            self.initialize_database()

    def initialize_database(self):
        root = ET.Element("data")
        tree = ET.ElementTree(root)
        tree.write(self.data_file)

    def append_or_create_topic(self, topic_name, note_name, note_text, timestamp):
        tree = ET.parse(self.data_file)
        root = tree.getroot()
        topic = root.find(f"./topic[@name='{topic_name}']")
        if topic is None:
            topic = ET.SubElement(root, "topic", name=topic_name)
        note = ET.SubElement(topic, "note", name=note_name)
        note_text_elem = ET.SubElement(note, "text")
        note_text_elem.text = note_text
        timestamp_elem = ET.SubElement(note, "timestamp")
        timestamp_elem.text = timestamp
        tree.write(self.data_file)

    def get_notes_by_topic(self, topic_name):
        tree = ET.parse(self.data_file)
        root = tree.getroot()
        topic = root.find(f"./topic[@name='{topic_name}']")
        if topic is None:
            return "Topic not found"
        else:
            notes = []
            for note in topic.findall("note"):
                notes.append({
                    "name": note.attrib["name"],
                    "text": note.find("text").text,
                    "timestamp": note.find("timestamp").text
                })
            return notes

    def query_wikipedia(self, search_term):
        # Example: querying Wikipedia API
        url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={search_term}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'query' in data and 'search' in data['query']:
                return data['query']['search']
        return "No results found"

# Start XML-RPC server
server = SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(NoteServer())
print("Server listening on port 8000...")
server.serve_forever()
