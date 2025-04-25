
class Entry:
    def __init__(self, name, link, desc, tags):
        self.name = name
        self.link = link
        self.desc = desc
        self.tags = tags

    def get_name(self):
        return self.name

    def get_link(self):
        return self.link

    def get_desc(self):
        return self.desc

    def get_tags(self):
        return self.tags

    def set_name(self, name):
        self.name = name

    def set_link(self, link):
        self.link = link

    def set_summary(self, desc):
        self.desc = desc

    def set_tags(self, tags):
        self.tags = tags

    def __str__(self):
        return f"{self.name}\n{self.link}\n{self.desc}"

class SearchTable:
    def __init__(self, entries):
        self.entries = entries

    def search(self, query):
        result = []
        for entry in self.entries:
            text = f"{entry.get_name()} {entry.get_desc()}"
            if query in text:
                result.append(entry)
            elif query in entry.get_tags():
                result.append(entry)
        if len(result) == 0:
            ent = Entry("No matches found.", "", "", "")
            result.append(ent)
        return result

















