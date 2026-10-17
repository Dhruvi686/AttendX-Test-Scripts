
import unittest


def mark_attendance(student_id, status):
    if not student_id:
        return "Student ID is required"
    if status not in ("Present", "Absent"):
        return "Invalid attendance status"
    return f"Attendance marked: {status}"


class AttendanceTest(unittest.TestCase):

    def test_mark_present(self):
        self.assertEqual(
            mark_attendance("STU101", "Present"),
            "Attendance marked: Present"
        )

    def test_mark_absent(self):
        self.assertEqual(
            mark_attendance("STU102", "Absent"),
            "Attendance marked: Absent"
        )

    def test_empty_student_id(self):
        self.assertEqual(
            mark_attendance("", "Present"),
            "Student ID is required"
        )


if __name__ == "__main__":
    unittest.main()
