import psycopg2 
import csv
import json

class FilterModule(object):
    def filters(self):
        return {
            'insert_user_filter': self.insert_user,
            'export_users_filter': self.export_users_filter
        }

    
    def insert_user(self, var):
        # PostgreSQL connection details for the first database 
        host = "localhost" 
        database = "testdb" 
        user = "awxuser" 
        password = "pooja" 
        
        # Connect to the first PostgreSQL database 
        conn1 = psycopg2.connect(host=host, database=database, user=user, password=password) 
        
        # Create a cursor object for the first database 
        cursor1 = conn1.cursor() 
        
        # Insert new names into the complex_table of the first database 
        insert_query1 = """ 
            INSERT INTO users (name, email) 
            VALUES (%s, %s); 
        """ 
        data1 = [ 
            ("Deepthi", "deepthi@example.com"), 
            ("Rupesh", "rupesh@example.com"), 
            ("Mani", "mani@example.com"), 
            ("Atul", "atul@example.com"), 
            ("Pradeep", "pradeep@example.com"), 
            ("Abhishek", "abhishek@example.com"), 
            ("Sharnitha","sharnitha@example.com"), 
        ] 
        cursor1.executemany(insert_query1, data1) 
        
        # Commit the changes to the first database 
        conn1.commit() 
        
        # Close the cursor and the first database connection 
        cursor1.close() 
        conn1.close() 
        return "Inserted 7 new users"
    
    def export_users_filter(self, users_data):
        data = users_data['query_result']
        keys = data[0].keys()
        with open('users.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
        return "Exported users data into users.csv"
