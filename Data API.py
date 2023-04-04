#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify


# In[2]:


app = Flask(__name__)


# In[3]:


# Get all companies’ stock data for a particular day(input api would be date)
@app.route('/stocks/<string:date>', methods=['GET'])
def get_all_stock_data_by_date(date):
    # stock_data = {
         #'date': date,
        #'companies': [
           # {
            #    'name': 'IBM',
            #    'price': 100.0
            #},
            #{
            #    'name': 'AAPL',
            #    'price': 200.0
           # },
            #{
            #    'name': 'GOOG',
            #    'price': 300.0
           # }
       # ]
    #}
# Here, you can fetch the stock data for all companies on the given date from the database
# and return it as a JSON response
   return jsonify(stock_data)
#if __name__ == '__main__':
    #app.run(debug=True)


# In[4]:


# Get all stock data for a particular company for a particular day(input to API would be company ID/name and date)
@app.route('/stocks/<string:company>/<string:date>', methods=['GET'])
def get_stock_data_by_company_and_date(company, date):
     # stock_data = {
        #'company': company,
        #'date': date,
       # 'price': 100.0
   # }
    
# Here, you can fetch the stock data for the given company on the given date from the database
# and return it as a JSON response
    return jsonify(stock_data)
# if __name__ == '__main__':
    # app.run(debug=True)


# In[5]:


# Get all stock data for a particular company(input to API would be company ID)
@app.route('/stocks/<string:company>', methods=['GET'])
def get_stock_data_by_company(company):
# Here, you can fetch all the stock data for the given company from the database
# and return it as a JSON response
    return jsonify(stock_data)


# In[6]:


# POST/Patch API to update stock data for a company by date
@app.route('/stocks/<string:company>/<string:date>', methods=['POST', 'PATCH'])
def update_stock_data(company, date):
           # Here, you can update the stock data for the given company on the given date in the database

# based on the data received in the request body and return a success message as a JSON response
     return jsonify({'message': 'Stock data updated successfully'})


# In[ ]:




