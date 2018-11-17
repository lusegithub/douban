import pymysql


class DAO(object):
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          db='douban',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def insert_item(self, title, movie_type, score, date, length, introduction):
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `movie` (`title`, `movie_type`, `score`, `date`, `length`, `introduction`) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (title, movie_type, score, date, length, introduction))
            self.connection.commit()
        except:
            self.connection.close()

    def close_db(self):
        self.connection.close()
