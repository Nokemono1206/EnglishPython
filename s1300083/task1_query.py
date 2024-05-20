import sqlite3
import os

def get_new_name(cur: sqlite3.Cursor, new_name="") -> str:
    """
        Reads input until get input of a unique name.

        Parameters
        ----------
            cur : sqlite3.Cursor
                cursor of database.
            new_name : str
                if specified, this will be processed as a first input.

        Returns
        -------
            new_name : str
                new identical name for the file.
    """
    if new_name == "":
        print("Please input new name: ", end="")
        new_name = input()

    while True:
        cur.execute(f"SELECT * FROM items WHERE name = ?", (new_name,))
        if not cur.fetchone():
            break
        print(f"Name '{new_name}' already used.")
        print("Please input new name: ", end="")
        new_name = input()

    return new_name


def upload_file(path: str, cur: sqlite3.Cursor) -> bool:
    """
        Adds a specified file to the database.

        Parameters
        ----------
            path : str
                path of the file.
            cur : sqlite3.Cursor
                cursor of database.

        Returns
        -------
            Returns true if the file successfully uploaded to the database.
    """
    if not os.path.isfile(path):
        return False

    with open(path, "r") as f:
        content = f.read()
        name = f.name
        cur.execute(f"SELECT * FROM items WHERE name = ?", (f.name,))
        if cur.fetchone():
            print(f"file '{f.name}' already exists in the dataset. Would you like to add the file anyway?(y/n)")
            if input() == 'y':
                name = get_new_name()
            else:
                return False
        else:
            print("Would you like to give a new name?(y/n)")
            if input() == 'y':
                name = get_new_name(cur)
        cur.execute("INSERT INTO items (content, original_name, name) VALUES(?,?,?)", (content, f.name, name))
        return True
            

def find(name: str, cur: sqlite3.Cursor) -> bool:
    """
        Finds the data that has same name as argument.

        Parameters
        ----------
            name : str
                name of search target.
            cur : sqlite3.Cursor
                cursor of database.

        Returns
        -------
            Returns whether the data exists.
    """
    cur.execute(f"SELECT * FROM items WHERE name = ?", (name,))
    if cur.fetchone():
        return True
    else:
        print("File not found.")
        return False


def rename(current: str, new: str, cur: sqlite3.Cursor) -> None:
    """
        Changes the 'name' attribute of specified record.
        Does nothing if data doesn't exist.

        Parameters
        ----------
            current : str
                name of the file to rename.
            new : str
                new name.
            cur : sqlite3.Cursor
                cursor of database.
    """
    if not find(current, cur):
        return
    new = get_new_name(cur, new)
    cur.execute("UPDATE items SET name = ? WHERE name = ?", (new, current))
    print(f"Renamed {current} to {new}.")


datapath = "task1.sqlite"
conn = sqlite3.connect(datapath)
cur = conn.cursor()

# 必要なら, help コマンドに対する出力, 引数が足りない時のメッセージ出力の処理を追加する。
while True:
    print("Input a command.\n>", end="")
    query = input().split(" ")
    if query[0] == "help":
        print("exit:Shut down the system.\nupload(filename):Upload file."
        print("find(target):Find the file which include target.\nrename(target)(newname):Change the filename (target) to (newname).")
        print("delete(target):Delete the file.")

    elif query[0] == "exit":
        exit()
    elif query[0] == "upload":
        # upload filepath
        if upload_file(query[1], cur):
            conn.commit()
    elif query[0] == "find":
        # find name
        if find(query[1], cur):
            print("File found. Would you like to review the content?(y/n)")
            if input() == 'y':
                cur.execute(f"SELECT content FROM items WHERE name = ?", (query[1],))
                print(cur.fetchall())
    elif query[0] == "rename":
        # rename current_name new_name
        rename(query[1], query[2], cur)
        conn.commit()
    elif query[0] == "delete":
        # delete name
        if(find(query[1], cur)):
            cur.execute(f"DELETE FROM items WHERE name = ?", (query[1],))
            conn.commit()
            print(f"Deleted '{query[1]}'")
    else:
        print("Command not found.\nType 'help' to see usage.")
