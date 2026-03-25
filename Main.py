import firebase_admin
from firebase_admin import credentials, db
import json
​class ContactConnector:
def init(self, cert_path, db_url):
  if not firebase_admin._apps:
cred = credentials.Certificate(cert_path)
firebase_admin.initialize_app(cred, {
'databaseURL': db_url
})
self.db_ref = db.reference('/contacts')
​def add_contact(self, name, email, phone, role="Developer"):
data = {
'name': name,
'email': email,
'phone': phone,
'role': role
}
new_entry = self.db_ref.push(data)
return new_entry.key
​def get_contact_by_name(self, search_name):
all_contacts = self.db_ref.get()
if not all_contacts:
return None
​matches = {k: v for k, v in all_contacts.items()
if search_name.lower() in v['name'].lower()}
return matches
​def export_to_json(self, filename="backup_contacts.json"):
data = self.db_ref.get()
with open(filename, 'w') as f:
json.dump(data, f, indent=4)
​if name == "main":
CERT_FILE = "serviceAccountKey.json"
DATABASE_URL = "https://your-project-id.firebaseio.com/"
​connector = ContactConnector(Your file...)
​contact_id = connector.add_contact(
"Miguel Albuquerque",
"miguel@example.com",
"+5511999999999"
)
​results = connector.get_contact_by_name("Miguel")
print(results)
