from abc import ABC, abstractmethod


class CloudStorage(ABC):
    def __init__(self):
        self.files = {}                 # simulated storage

    @abstractmethod
    def upload_file(self, name, content):
        pass

    @abstractmethod
    def download_file(self, name):
        pass

    @abstractmethod
    def delete_file(self, name):
        pass


class GoogleDriveStorage(CloudStorage):
    def upload_file(self, name, content):
        self.files[name] = content
        print(f"[Google Drive] Uploaded '{name}'")

    def download_file(self, name):
        if name in self.files:
            print(f"[Google Drive] Downloaded '{name}': {self.files[name]}")
        else:
            print(f"[Google Drive] '{name}' not found")

    def delete_file(self, name):
        if self.files.pop(name, None) is not None:
            print(f"[Google Drive] Deleted '{name}'")
        else:
            print(f"[Google Drive] '{name}' not found")


class DropboxStorage(CloudStorage):
    def upload_file(self, name, content):
        self.files[name] = content
        print(f"[Dropbox] File '{name}' synced to cloud")

    def download_file(self, name):
        if name in self.files:
            print(f"[Dropbox] File '{name}' retrieved: {self.files[name]}")
        else:
            print(f"[Dropbox] '{name}' not found")

    def delete_file(self, name):
        if self.files.pop(name, None) is not None:
            print(f"[Dropbox] File '{name}' removed")
        else:
            print(f"[Dropbox] '{name}' not found")


for service in (GoogleDriveStorage(), DropboxStorage()):
    service.upload_file("notes.txt", "Hello Cloud")
    service.download_file("notes.txt")
    service.delete_file("notes.txt")
    service.download_file("notes.txt")
    print("-" * 35)
