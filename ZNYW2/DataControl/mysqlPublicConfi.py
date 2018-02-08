# coding=utf-8
import mysql.connector


class MysqlPublicConfi:
    def __init__(self):
        pass

    conn = mysql.connector.connect(
        host="172.16.40.240",
        port="3306",
        user="sito",
        password="tianhuzuji@91.112",
        database="iom365",
        charset="utf8"
    )
    cursor = conn.cursor()
