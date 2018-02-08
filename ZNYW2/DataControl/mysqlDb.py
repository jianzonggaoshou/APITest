# coding=utf-8
from mysqlPublicConfi import MysqlPublicConfi


class MysqlDb:
    def __init__(self):
        pass

    # # 清除表数据
    # def clear(self, table_name, data_name, data_value):
    #     sql = "DELETE FROM" + table_name + "Where" + data_name + "=" + data_value
    #     self.cursor.execute(sql)
    #     self.conn.commit()
    #     print "删除成功"

    @staticmethod
    def insert():
        cursor = MysqlPublicConfi.cursor
        conn = MysqlPublicConfi.conn

        keys = ["customer_name", "customer_address", "customer_introduction", "region_id", "agent_id", "create_time",
                "last_modify_time", "is_deleted"]
        values = ["'许臻客户2'", "'软件新城'", "'软件新城国家级新区'", "'1'", "'2'", "'2018-01-30 12:00'", "'2018-01-30 12:00'", "'0'"]

        for key in keys:
            keys = ''.join(key)
            print keys



        values = str(values)

        sql = "INSERT INTO base_customer(" + keys + ") VALUES (" + values + ")"

        print sql

        cursor.execute(sql)
        conn.commit()
        print "添加成功"
        conn.close()

    # 关闭数据库连接
    def close(self):
        pass


if __name__ == "__main__":
    MysqlDb.insert()
