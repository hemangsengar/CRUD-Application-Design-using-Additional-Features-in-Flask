# Import libraries
from flask import Flask, redirect, request, render_template, url_for

# TO RUN THE SERVER                  python app.py

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

@app.route("/edit/<int:transaction_id>", methods = ["GET", "POST"])
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
                transaction['date'] = date      
                transaction['amount'] = amount  
                break 

        return redirect(url_for("get_transactions"))


    return {"message": "Transaction not found"}, 404

# Delete operation


@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break

    return redirect(url_for("get_transactions"))

#Search

@app.route("/search", methods = ["GET","POST"])
def search_transactions():
    if request.method == "POST":
        min_amount = float(request.form['min_amount'])
        max_amount = float(request.form['max_amount'])
        filtered_transactions = [
            transaction for transaction in transactions
            if min_amount <= transaction['amount'] <= max_amount
        ]
        return render_template("transactions.html", transactions=filtered_transactions)
    
    return render_template("search.html")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
