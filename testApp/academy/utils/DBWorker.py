from django.db import connection

FIND_ALL_QUERY = "SELECT id,title, description, image FROM lesson "
FIND_LESSON_BY_ID_QUERY = 'SELECT id,title, description, image FROM Lesson WHERE id = %s'


def find_by_id(id):
    with connection.cursor() as cursor:
        cursor.execute(FIND_LESSON_BY_ID_QUERY % id)
        row = list(cursor.fetchone())

    lesson = {'id': row[0],
              'title': row[1],
              'description': row[2],
              'image': row[3]}
    return lesson


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