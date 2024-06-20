import psycopg2
from common.postgres import load_postgre_config

class PostgresService:
    def __init__(self):
        config = load_postgre_config()
        try:
            self.conn = psycopg2.connect(
                dbname=config.PG_DB,
                user=config.PG_USER,
                password=config.PG_PASS,
                host=config.PG_HOST,
                port=config.PG_PORT
            )
            print("Koneksi ke database berhasil.")
            self.cursor = self.conn.cursor()
        except psycopg2.Error as e:
            print(f"Error saat menghubungkan ke database: {e}")
            self.conn = None
            self.cursor = None
        
    def read(self):
        if self.cursor:
            try:
                table_name = 'tolerance_index_analysis_202402'
                name_field = '*'
                select_query = f"SELECT {name_field} FROM {table_name}"
                self.cursor.execute(select_query)
                rows = self.cursor.fetchall()
                print(rows)
            except psycopg2.Error as e:
                print(f"Error saat membaca data dari tabel: {e}")
            finally:
                if self.cursor:
                    self.cursor.close()
        else:
            print("Tidak dapat membaca data karena tidak ada koneksi ke database.")

    def insert(self, table_name, datas):
        if self.cursor:
            for data in datas:
                try:
                    query = f"""INSERT INTO {table_name} (province_name, city_name) VALUES 
                        {str(data)}
                    """
                    self.cursor.execute(query)
                    self.conn.commit()
                    print("Data Berhasil Masuk")
                except Exception as e:
                    print("Gagal Insert")

        else:
            print("Tidak dapat membaca data karena tidak ada koneksi ke database")
        return
    
    def read_column(self):
        if self.cursor:
            try:
                table_name = 'tolerance_index_analysis_202402'
                name_field = '*'
                select_query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'"
                self.cursor.execute(select_query)
                rows = self.cursor.fetchall()

                data_colomn = []
                for row in rows: 
                    column_name = row[0]
                    print(column_name)
                    data_colomn.append(column_name)
                return data_colomn
            except psycopg2.Error as e:
                print(f"Error saat membaca data dari tabel: {e}")
            finally:
                if self.cursor:
                    self.cursor.close()
        else:
            print("Tidak dapat membaca data karena tidak ada koneksi ke database.")
