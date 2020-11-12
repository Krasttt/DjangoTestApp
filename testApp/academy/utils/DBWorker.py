from django.db import connection

FIND_ALL_QUERY = "SELECT id,title, description, image FROM lesson "
FIND_LESSON_BY_ID_QUERY = 'SELECT id,title, description, image FROM Lesson WHERE id = %s'


def find_by_id(id):
    with connection.cursor() as cursor:
        cursor.execute(FIND_LESSON_BY_ID_QUERY % id)
        row = cursor.fetchone()
    if row:
        row_list = list(row)
        lesson = {'id': row_list[0],
                  'title': row_list[1],
                  'description': row_list[2],
                  'image': row_list[3]}
        return lesson
    else:
        return []


def find_all():
    with connection.cursor() as cursor:
        cursor.execute(FIND_ALL_QUERY)
        row = list(cursor.fetchall())

    lessons = []
    for lesson in row:
        lessons.append({
            'id': lesson[0],
            'title': lesson[1],
            'description': lesson[2],
            'image': lesson[3]})
    return lessons