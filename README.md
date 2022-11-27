# Portfolio
 Hi my name is Alan Lanceloth, and welcome to my Github Portfolio.  
 This repo contains all of my Data Science projects.  

 Here is my [LinkedIn](https://www.linkedin.com/in/alanlanceloth/).
 
 Below, you can check a brief description of my projects.
 
 ## Table of Contents
=================
<!--ts-->
   * [Project 1 - Previsao de Vendas - Sales Predict](#project-1-previsao-de-vendas---sales-predict)
   * [Project 2 - Binance bot](#project-2---binance-bot)
   * [Project 3 - Olist Database](#project-3---olist-database)
   * [Project 4 - Portfolio Optimization](#project-4---portfolio-optimization)
<!--te-->

### Project 1 - Previsao de Vendas - Sales Predict
 **Goal:** The goal of this project is to predict the Sales of a company by their advertising investment using Machine Learning.  

 **Description:** In this project I've made a comparrison with Linear Regression and Decision Tree models.  

 **Results:** The Decision Tree proved a R2 higher and have returned that the TV advertisement investment have more impact in the Sales revenue.  
 Also, we've checked that the company is spending more money with a form of advertising that is not so efficient (*'Jornal'* compared with *'Radio'*).  
 
### Project 2 - Binance Bot

**Goal:** The main goal of this project is to build a bot that can send orders to Binance based on preset strategies.

**Description:** This robot currently has the ability to compare the price paid in Bitcoin, and compare it every X hours (predefined by user) with the current price. After the comparison, the robot sends a message to the user informing the current Bitcoin price and if the user is making a profit.
In the future, this price comparison module will be absorbed by the main objective of the project - the execution of orders based on predefined strategies.

**Results:** So far, a module for comparing prices and sending results via Telegram has been built.
The robot also has the ability to access the asset price via the Binance API and the Dollar quote via the awesomeapi API.

### Project 3 - Olist Database

**Goal:** The goal of this project is to demonstrate the use of essential skills for a data scientist.

**Description:** Using data obtained from Kaggle through [link](https://www.kaggle.com/leandroal/an-lise-do-e-commerce-no-brasil-olist-dataset), it was created a project in order to demonstrate necessary skills for a data scientist. Are they:
  - Creation of a database in a Cloud environment (Google Cloud Platform - GCP) from CSV files.
  - Extraction, Transformation and Load of data through Python using APIs to connect with GCP.
  - Exploratory data analysis
  - Machine Learning
  - Feature Engineering

**Results:** In development.

### Project 4 - Portfolio Optimization

**Goal:** The goal of this project is to demonstrate a Portfolio Optimization using Markowitz Efficient Frontier method.

**Description:** In this project, we're demonstrating the Portfolio Optimization using Markowitz Efficient Frontier method using the Valor Economico Wallet in the Brazillian Stock Market.

Disclaimer: I am not a financial advisor. Do not take anything on this code as financial advice, ever.
Do your own research.
Consult a professional investment advisor before making any investment decisions!

**Results:** The result obtained was an optimized portfolio, with a Sharpe index above 1 (which can be considered good), low volatility (below 20%) and expected annual return above 100%.

Results from [PyPortfolioOpt](https://pyportfolioopt.readthedocs.io/en/latest/index.html) using the [Mean-variance optimization](https://pyportfolioopt.readthedocs.io/en/latest/UserGuide.html#mean-variance-optimization):
Expected annual return: 112.5%
Annual volatility: 18.2%
Sharpe Ratio: 6.05

An Out of Sample backtest using [Vectorbt](https://vectorbt.dev/api/portfolio/base/)  was also carried out including the same portfolio in another period to carry out the backtest. This test prevents model Overfit.

Results from Vectorbt forcing the Overfit (using the dataset from the same period of the weights to backtest):
  Start                                    2021-11-22
  End                                      2022-05-20
  Period                                   124 days
  Total Return [%]                        43.452249
  Benchmark Return [%]                     3.645865
  Max Drawdown [%]                         5.852377
  Sharpe Ratio                             4.813585
  Max Drawdown Duration                    15 days

Results from Vectorbt using the Out of Sample (using the dataset from another period of the weights to backtest):
  Start                                    2022-05-23
  End                                      2022-11-22
  Period                                   127 days
  Total Return [%]                         9.180265
  Benchmark Return [%]                     1.494079
  Max Drawdown [%]                        12.364891
  Sharpe Ratio                             1.075218
  Max Drawdown Duration                    49 days

Here is the porfolio allocation assuming a 20.000 BRL total portfolio value:

Stocks allocation:  {'AGRO3.SA': 54, 'CIEL3.SA': 990, 'CPLE6.SA': 340, 'EGIE3.SA': 6, 'ELET3.SA': 25, 'HYPE3.SA': 50, 'ITUB4.SA': 5, 'SBSP3.SA': 31, 'SLCE3.SA': 68, 'TAEE11.SA': 49, 'UNIP6.SA': 20, 'VALE3.SA': 6}

Leftover: 0.037377230371930636 BRL