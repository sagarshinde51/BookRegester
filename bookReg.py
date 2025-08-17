import streamlit as st
import mysql.connector

# Database connection details
host = "82.180.143.66"
user = "u263681140_students1"
password = "testStudents@123"
database = "u263681140_students1"

def get_connection():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

# Streamlit UI
st.title("📚 GPK Books - Insert Data")

# Input fields
book_name = st.text_input("Book Name")
author_name = st.text_input("Author Name")
stocks_of_books = st.number_input("Total Stocks of Books", min_value=0, step=1)
available_stock = st.number_input("Available Stock", min_value=0, step=1)

if st.button("Insert Data"):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO GPK_books (Book_Name, Author_Name, stocks_of_books)
        VALUES (%s, %s, %s)
        """
        values = (book_name, author_name, stocks_of_books)

        cursor.execute(sql, values)
        conn.commit()

        st.success("✅ Data inserted successfully!")

        cursor.close()
        conn.close()
    except Exception as e:
        st.error(f"❌ Error: {e}")
