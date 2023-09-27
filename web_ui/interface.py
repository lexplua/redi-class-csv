import streamlit as st

from exercises.classwork import get_csv_filename, fetch_csv_content, add_record, get_next_id


def draw_content():
    left_column, right_column = st.columns(2)
    draw_submit_form(left_column)
    draw_book_catalog(right_column)


def draw_book_catalog(right_column):
    filename = get_csv_filename()
    with right_column:
        st.subheader("Book catalog")
        lines = fetch_csv_content(filename)
        for line in lines:
            st.write(line)


def draw_submit_form(left_column):
    with left_column:
        st.subheader("Add book to catalog")

        with st.form("Add book", clear_on_submit=True):
            author = st.text_input("Author")
            book_name = st.text_input("Book name")
            submitted = st.form_submit_button("Store")

            if submitted:
                filename = './data_files/database.csv'
                max_id = get_next_id(filename)
                add_record(filename, max_id + 1, author, book_name)


def draw_header():
    st.header("Filo I/O demo")
