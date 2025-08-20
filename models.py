import sqlite3

DB_NAME = 'orgtrackr.db'

SCHEMA = '''
CREATE TABLE IF NOT EXISTS organizations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    location TEXT,
    yearFounded INTEGER,
    contactEmail TEXT NOT NULL
);
'''

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(SCHEMA)
    conn.commit()
    conn.close()

class Organization:
    @staticmethod
    def all():
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('SELECT * FROM organizations')
        orgs = c.fetchall()
        conn.close()
        return orgs

    @staticmethod
    def get(org_id):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('SELECT * FROM organizations WHERE id=?', (org_id,))
        org = c.fetchone()
        conn.close()
        return org

    @staticmethod
    def create(data):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO organizations (name, type, location, yearFounded, contactEmail) VALUES (?, ?, ?, ?, ?)',
                  (data['name'], data['type'], data.get('location'), data.get('yearFounded'), data['contactEmail']))
        conn.commit()
        conn.close()

    @staticmethod
    def update(org_id, data):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('UPDATE organizations SET name=?, type=?, location=?, yearFounded=?, contactEmail=? WHERE id=?',
                  (data['name'], data['type'], data.get('location'), data.get('yearFounded'), data['contactEmail'], org_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(org_id):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('DELETE FROM organizations WHERE id=?', (org_id,))
        conn.commit()
        conn.close()
