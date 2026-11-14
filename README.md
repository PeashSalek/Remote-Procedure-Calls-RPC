# 📝 RPC Notebook — Client/Server with XML-RPC

A small distributed notebook built in **Python** to practise **Remote Procedure Calls (RPC)**: the client calls functions that actually run on the server, as if they were local.

The server stores notes by topic in an XML file and can also search Wikipedia on the client's behalf.

## How it works

```
 client.py  ──── XML-RPC over HTTP (localhost:8000) ────▶  server.py
 (text menu)   append_or_create_topic(...)                 NoteServer
               get_notes_by_topic(...)                      ├─ notes.xml  (storage)
               query_wikipedia(...)                         └─ Wikipedia API
```

| Remote function | What it does |
|---|---|
| `append_or_create_topic(topic, name, text, timestamp)` | Adds a note, creating the topic if it doesn't exist |
| `get_notes_by_topic(topic)` | Returns every note saved under a topic |
| `query_wikipedia(term)` | Server queries the Wikipedia API and returns matching articles |

## Tech

- Python standard library `xmlrpc.server` / `xmlrpc.client`
- `xml.etree.ElementTree` for the XML "database"
- `requests` for the Wikipedia API

## Run it

```bash
pip install -r requirements.txt

# terminal 1 – start the server
python server.py

# terminal 2 – start the client
python client.py
```

Then choose from the menu: add a note, read notes by topic, or search Wikipedia.

## What I learned

- How RPC hides network calls behind ordinary function calls
- Designing a simple client–server protocol and keeping server state in a file
- Calling an external REST API from the server side

*Built for a distributed systems course at LUT University.*

**Peash Salek** · [GitHub](https://github.com/PeashSalek)
