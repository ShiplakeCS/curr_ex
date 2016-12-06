from flask import Flask, request, render_template
import currency
app = Flask(__name__) # set up a new web app

@app.route('/')
def index():
    return render_template('currency_form.html', cur_list = currency.getCurrencyList() )

@app.route('/getamount', methods=['POST', 'GET'])
def getAmount():
    if request.method == 'POST':
        print("POST data found")
        amount = request.form['amount']
        cur = request.form['currency']
        return str(currency.getConvertedAmount(amount, cur))
    else:
        return 'Form data not found'

@app.route('/convert/<cur>/<amount>')
def doConversion(cur, amount):
    return str(currency.getConvertedAmount(amount,cur))


if __name__ == '__main__':
    app.run(debug=True, port=8080)
