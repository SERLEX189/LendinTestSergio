from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={"/requLoanList": {"origins": "*"}})

from RequestLoan import RequestLoan, requLoanList

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# Get Data Routes
@app.route('/requLoanList')
def getProducts():
    # return jsonify(products)
    return jsonify({'requLoanList': requLoanList})


@app.route('/requLoanList/<string:taxId>')
def getProduct(taxId):
    requLoansFound = [
        requLoan for requLoan in requLoanList if requLoan['taxId'] == taxId]
    if (len(requLoansFound) > 0):
        return jsonify({'requLoan': requLoansFound[0]})
    return jsonify({'message': 'requLoan Not found'})

# Create Data 
@app.route('/requLoanList', methods=['POST'])
def addProduct():

    if float(request.json['amount'])>50000:
        requLoan =RequestLoan(request.json['taxId'],int(request.json['soSecNum']),
        float(request.json['amount']),'Declined')

    elif float(request.json['amount'])==50000:
        requLoan =RequestLoan(request.json['taxId'],int(request.json['soSecNum']),
        float(request.json['amount']),'Undecided')

    else:
        requLoan =RequestLoan(request.json['taxId'],int(request.json['soSecNum']),
        float(request.json['amount']),'Approved')

    new_requLoan= {
        'taxId': requLoan.taxId,
        'soSecNum': requLoan.soSecNum,
        'amount': requLoan.amount,
        'loanDecis': requLoan.loanDecis
    }
    requLoanList.append(new_requLoan)
    return jsonify({'newRequLoan': new_requLoan})


# Update Data 

@app.route('/requLoanList/<string:taxId>', methods=['PUT'])
def editProduct(taxId):
    
    requLoansFound = [requLoan for requLoan in requLoanList if requLoan['taxId'] == taxId]
    if (len(requLoansFound) > 0):
        requLoansFound[0]['taxId'] = request.json['taxId']
        requLoansFound[0]['soSecNum'] = request.json['soSecNum']
        requLoansFound[0]['amount'] = request.json['amount']
        requLoansFound[0]['loanDecis'] = request.json['loanDecis']
        return jsonify({
            'message': 'Product Updated',
            'product': requLoansFound[0]
        })
    return jsonify({'message': 'Product Not found'})

# DELETE Data
@app.route('/requLoanList/<string:taxId>', methods=['DELETE'])
def deleteProduct(taxId):
    requLoansFound = [requLoan for requLoan in requLoanList if requLoan['taxId'] == taxId]
    if len(requLoansFound) > 0:
        requLoanList.remove(requLoansFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': requLoanList
        })


if __name__ == '__main__':
    app.run(debug=True, port=4000)
