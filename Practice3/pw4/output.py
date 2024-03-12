import curses


def display_student_info(student):
    def main(stdscr):

        stdscr.clear()


        stdscr.addstr(0, 0, f"Student ID: {student.id}")
        stdscr.addstr(1, 0, f"Student Name: {student.name}")
        stdscr.addstr(2, 0, f"Date of Birth: {student.dob}")


        row = 4
        for course, mark in student.marks.items():
            stdscr.addstr(row, 0, f"{course}: {mark}")
            row += 1

        stdscr.refresh()
        stdscr.getch()


    curses.wrapper(main)
