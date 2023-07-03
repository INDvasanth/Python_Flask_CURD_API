from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2023",
    database="taskdb"
)

@app.route("/")
def hello():
    return "Welcome Flask with CURD operation!"

@app.route("/users", methods=["GET"])
def get_users():
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    cursor.close()
    users = []
    for row in result:
        user = {
            "Deal Date": row[1],
            "Security Code": row[2],
            "Security Name": row[3],
            "Client Name": row[4],
            "Deal Type": row[5],
            "Quantity": row[6],
            "Price": row[7]
        }
        users.append(user)
    return jsonify(users)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    deal_date = data["Deal Date"]
    sec_code = data["Security Code"]
    sec_name = data["Security Name"]
    client_name = data["Client Name"]
    deal_type = data["Deal Type"]
    qty = data["Quantity"]
    price = data["Price"]
    
    cursor = cnx.cursor()
    query = "INSERT INTO users (deal_date, sec_code, sec_name, client_name, deal_type, qty, price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (deal_date, sec_code, sec_name, client_name, deal_type, qty, price)
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()
    return jsonify({"message": "User created successfully"})

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    sec_name = data["Security Name"]
    client_name = data["Client Name"]
    qty = data["Quantity"]
    price = data["Price"]
    cursor = cnx.cursor()
    query = "UPDATE users SET sec_name = %s, client_name = %s, qty = %s, price = %s WHERE id = %s"
    values = (sec_name, client_name, qty, price, user_id)
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()
    return jsonify({"message": f"User with ID {user_id} updated successfully"})

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    cursor = cnx.cursor()
    query = "DELETE FROM users WHERE id = %s"
    values = (user_id,)
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()
    return jsonify({"message": f"User with ID {user_id} deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
