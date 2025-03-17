# Import libraries
from flask import Flask, redirect, request, render_template, url_for

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]
# Read operation
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)



# Create operation

@app.route("/add", methods = ["GET","POST"])
def add_transaction():
    if request.method == "POST":
        transation = {
              'id': len(transactions)+1 ,
              'date': request.form['date'],
              'amount': float(request.form['amount'])
             }
        transactions.append(transation)

        return redirect(url_for("get_transactions"))
    

    return render_template("form.html")

# Update operation

@app.route("/edit/<int:transaction_id>", method = ["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == "GET":
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                return render_template("edit.html",transaction = transaction)
    
    if request.method == "POST":
        date = request.form['date']
        amount = float(request.form['amount'])

        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date       # Update the 'date' field of the transaction
                transaction['amount'] = amount   # Update the 'amount' field of the transaction
                break 

        return redirect(url_for("get_transactions"))


    return {"message": "Transaction not found"}, 404

# Delete operation

# Run the Flask app
    