from supabase import create_client, Client
import csv
import time

class db_manager:
    def update_data(self, db_csv: str):


        url = 'https://ajlqvqtpqkrgjzacofii.supabase.co'
        key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFqbHF2cXRwcWtyZ2p6YWNvZmlpIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5MzgzMDY5NywiZXhwIjoyMDA5NDA2Njk3fQ.zeZPWJ15JiFzO9b7K9KCa6hd85bpZb5YeF-IP_pUZQU'


        supabase: Client = create_client(url, key)

        response = supabase.table('db_txt').select('*').execute()



        print(f"x {response}")

        ids = [x['id'] for x in supabase.table('db_txt').select('id').execute().data]
        res = supabase.table('db_txt').delete().in_('id', ids).execute()

        time.sleep(5)

        with open(db_csv, 'rt') as f:
            csv_reader = csv.reader(f)

            for line in csv_reader:
                print(line)
                supabase.table('db_txt').insert({"id": line[0], "dateadded": line[1],"url": line[2],"url_status": line[3],"last_online": line[4],"threat": line[5],"tags": line[6],"urlhaus_link": line[7]}).execute()


db_csv = "Db/small/db.csv"
db_manager = db_manager()
db_manager.update_data(db_csv)