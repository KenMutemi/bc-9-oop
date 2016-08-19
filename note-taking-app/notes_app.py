class NotesApplication(object):


    def __init__(self, author):
        self.author = author
        self.notes = []
    
    def create(self, note_content):
        self.notes.append(note_content)
        
    def list(self):
        print("Note ID: " + self.author + " - " + str(self.notes))
        
    def get(self, note_id):
        if note_id in self.notes:
                return note_id
        else:
                return "Invalid ID"
        
        
NotesApplication("Kennedy").create("Hello, World!")
NotesApplication("Cynthia").create("Hello, World!")
NotesApplication("Victor").create("Hello, World!")
NotesApplication("Didas").create("Hello, World!")
NotesApplication("Muthama").create("Hello, World!")


NotesApplication("Muthama").list()
NotesApplication("Kennedy").list()
NotesApplication("Victor").list()
NotesApplication("Didas").list()
NotesApplication("Cynthia").list()
