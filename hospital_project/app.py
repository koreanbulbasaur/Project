from flask import Flask, request, render_template
import mysql.connector
import random
import string

def generate_random_doctor_id(length):
    characters = string.ascii_uppercase + string.digits
    doctor_id = ''.join(random.choice(characters) for _ in range(length))
    return doctor_id

app = Flask(__name__)

# MySQL Connection Configuration
db_config = {
    'user': 'hospital',
    'password': '1111',
    'host': 'localhost',
    'database': 'hospital',
    'port' : 3306
}

# home
@app.route("/")
def home():
    return render_template('home.html')

@app.route('/doctor_sc', methods=['GET', 'POST'])
def doctor_schedule():
    try:
        if request.method == 'POST':
            doctor_id = request.form['doctor_id']
            working_day = request.form['working_day']
            start_time = request.form['start_time']
            end_time = request.form['end_time']

            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            query = "INSERT INTO doctor_schedule (doctor_id, working_day, start_time, end_time)" \
                    "VALUES (%s, %s, %s, %s)"
            values = (doctor_id, working_day, start_time, end_time)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query_sc = "select a.*, b.name from hospital.doctor_schedule a inner join hospital.doctors b on a.doctor_id = b.doctor_id"
        cursor.execute(query_sc)

        doctor_schedules = cursor.fetchall()
        cursor.close()
        conn.close()

        return render_template('doctor_sc.html', doctor_schedules=doctor_schedules)
    
    except mysql.connector.Error as error:
        return {'error' : str(error)}

# doctor_dt
@app.route('/doctor_sc/doctor_dt', methods=['GET', 'POST'])
def doctor_index():
    if request.method == 'POST':
        random_doctor_id = generate_random_doctor_id(5)
        doctor_ID = 'D' + random_doctor_id
        doctor_name = request.form['name']
        doctor_PH = request.form['phone_number']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = "INSERT INTO doctors (doctor_id, name, phone_number)"\
            "VALUES (%s, %s, %s)"
        values = doctor_ID, doctor_name, doctor_PH
        cursor.execute(query, values)

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM hospital.doctors"
    cursor.execute(query)
    doctors = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('doctor_dt.html', doctors=doctors)

if __name__ == "__main__":
    app.run()