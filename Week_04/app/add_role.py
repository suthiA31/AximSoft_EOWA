import sqlite3

conn = sqlite3.connect("../instance/database.db")
cursor = conn.cursor()

admin_email = "suthishna.k@gmail.com"   # replace with your email

cursor.execute(
    """
    UPDATE users
    SET role = 'admin'
    WHERE email = ?
    """,
    (admin_email,)
)

conn.commit()

if cursor.rowcount > 0:
    print(f"{admin_email} is now an admin.")
else:
    print("No user found with that email. Register first.")

conn.close()