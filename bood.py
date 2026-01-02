import sys
import sqlite3

def main(action, data, content=None):
    print("resulta que conviene aprender sql primero xd")

if len(sys.argv) == 2:
    print("bood usage: <list/add-delete/show/copy> <course/section/lesson-raw>")
elif len(sys.argv) == 3:
    main(sys.argv[1], sys.argv[2])
elif len(sys.argv) == 4:
    main(sys.argv[1], sys.argv[2], sys.argv[3])
