import json
import datetime

NOTES_FILE = "notes.json"

def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note(title, message):
    notes = load_notes()
    timestamp = datetime.datetime.now().isoformat()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def list_notes(filter_date=None):
    notes = load_notes()
    if filter_date:
        filtered_notes = [note for note in notes if filter_date in note["timestamp"]]
    else:
        filtered_notes = notes

    for note in filtered_notes:
        print(f"ID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Message: {note['message']}")
        print(f"Timestamp: {note['timestamp']}")
        print("=" * 30)

def edit_note(note_id, new_title, new_message):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = new_title
            note["message"] = new_message
            note["timestamp"] = datetime.datetime.now().isoformat()
            save_notes(notes)
            print("Заметка успешно отредактирована")
            break
    else:
        print("Заметка с указанным ID не найдена")

def delete_note(note_id):
    notes = load_notes()
    updated_notes = [note for note in notes if note["id"] != note_id]
    if len(updated_notes) < len(notes):
        save_notes(updated_notes)
        print("Заметка успешно удалена")
    else:
        print("Заметка с указанным ID не найдена")

def main():
    while True:
        print("Введите команду: add, list, edit, delete, exit")
        command = input()

        if command == "add":
            title = input("Введите заголовок заметки: ")
            message = input("Введите тело заметки: ")
            add_note(title, message)

        elif command == "list":
            filter_date = input("Введите дату для фильтрации (YYYY-MM-DD): ")
            list_notes(filter_date)

        elif command == "edit":
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок заметки: ")
            new_message = input("Введите новое тело заметки: ")
            edit_note(note_id, new_title, new_message)

        elif command == "delete":
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)

        elif command == "exit":
            break

        else:
            print("Неверная команда. Пожалуйста, выберите допустимую команду.")

if __name__ == "__main__":
    main()