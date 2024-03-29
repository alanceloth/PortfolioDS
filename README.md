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
   * [Project 5 - Investment Fund Analysis](#project-5---investment-fund-analysis)
   * [Project 6 - Deep Learning & Crypto](#project-6---Deep-Learning-&-Crypto)
   * [Project 7 - Real Estate Investment Trusts](#project-7---Real-Estate-Investment-Trusts)
   * [Project 8 - Unsupervised Analysis for Decision Making](#project-8---Unsupervised-Analysis-for-Decision-Making)
   * [Project 9 - Autocorrelation](#project-9---Autocorrelation)
   * [Project 10 - Plotting Price and Volume of a Stock](#project-10---Plotting-Price-and-Volume-of-a-Stock)
   * [Project 11 - Analyzing Gas Price Trends with SARIMA: Estimating Past and Future Prices](#project-11---analyzing-gas-price-trends-with-sarima-estimating-past-and-future-prices)
   * [Project 12 - ETF Analysis](#project-12---ETF-Analysis)
   * [Project 13 - LinkedIn Bot](#project-13---LinkedIn-Bot)
   * [Project 14 - Weekly Report](#project-14---Weekly-Report)
<!--te-->

### [Project 1 - Previsao de Vendas - Sales Predict](https://github.com/alanceloth/PortfolioDS/tree/main/Previsao%20de%20Vendas)
 **Goal:** The goal of this project is to predict the Sales of a company by their advertising investment using Machine Learning.  

 **Description:** In this project I've made a comparrison with Linear Regression and Decision Tree models.  

 **Results:** The Decision Tree proved a R2 higher and have returned that the TV advertisement investment have more impact in the Sales revenue.  
 Also, we've checked that the company is spending more money with a form of advertising that is not so efficient (*'Jornal'* compared with *'Radio'*).  
 
### [Project 2 - Binance bot](https://github.com/alanceloth/PortfolioDS/tree/main/Bot%20Telegram%20Binance)

**Goal:** The main goal of this project is to build a bot that can send orders to Binance based on preset strategies.

**Description:** This robot currently has the ability to compare the price paid in Bitcoin, and compare it every X hours (predefined by user) with the current price. After the comparison, the robot sends a message to the user informing the current Bitcoin price and if the user is making a profit.
In the future, this price comparison module will be absorbed by the main objective of the project - the execution of orders based on predefined strategies.

**Results:** So far, a module for comparing prices and sending results via Telegram has been built.
The robot also has the ability to access the asset price via the Binance API and the Dollar quote via the awesomeapi API.

### [Project 3 - Olist Database](https://github.com/alanceloth/PortfolioDS/tree/main/Projeto%20-%20dados%20Olist)

**Goal:** The goal of this project is to demonstrate the use of essential skills for a data scientist.

**Description:** Using data obtained from Kaggle through [link](https://www.kaggle.com/leandroal/an-lise-do-e-commerce-no-brasil-olist-dataset), it was created a project in order to demonstrate necessary skills for a data scientist. Are they:
  - Creation of a database in a Cloud environment (Google Cloud Platform - GCP) from CSV files.
  - Extraction, Transformation and Load of data through Python using APIs to connect with GCP.
  - Exploratory data analysis
  - Machine Learning
  - Feature Engineering

**Results:** In development.

### [Project 4 - Portfolio Optimization](https://github.com/alanceloth/PortfolioDS/tree/main/Portfolio%20Optimization%20-%20Markowitz)

**Goal:** The goal of this project is to demonstrate a Portfolio Optimization using Markowitz Efficient Frontier method.

**Description:** In this project, we're demonstrating the Portfolio Optimization using Markowitz Efficient Frontier method using the Valor Economico Wallet in the Brazillian Stock Market.

**Disclaimer:**  I am not a financial advisor. Do not take anything on this code as financial advice, ever.
Do your own research.
Consult a professional investment advisor before making any investment decisions!

**Results:** The result obtained was an optimized portfolio, with a Sharpe index above 1 (which can be considered good), low volatility (below 20%) and expected annual return above 100%.

Results from [PyPortfolioOpt](https://pyportfolioopt.readthedocs.io/en/latest/index.html) using the [Mean-variance optimization](https://pyportfolioopt.readthedocs.io/en/latest/UserGuide.html#mean-variance-optimization):
  - Expected annual return: 112.5%
  - Annual volatility: 18.2%
  - Sharpe Ratio: 6.05

An Out of Sample backtest using [Vectorbt](https://vectorbt.dev/api/portfolio/base/)  was also carried out including the same portfolio in another period to carry out the backtest. This test prevents model Overfit.

Results from Vectorbt forcing the Overfit (using the dataset from the same period of the weights to backtest):
  - Start                                    2021-11-22
  - End                                      2022-05-20
  - Period                                   124 days
  - Total Return [%]                        43.452249
  - Benchmark Return [%]                     3.645865
  - Max Drawdown [%]                         5.852377
  - Sharpe Ratio                             4.813585
  - Max Drawdown Duration                    15 days

Results from Vectorbt using the Out of Sample (using the dataset from another period of the weights to backtest):
  - Start                                    2022-05-23
  - End                                      2022-11-22
  - Period                                   127 days
  - Total Return [%]                         9.180265
  - Benchmark Return [%]                     1.494079
  - Max Drawdown [%]                        12.364891
  - Sharpe Ratio                             1.075218
  - Max Drawdown Duration                    49 days

Here is the porfolio allocation assuming a 20.000 BRL total portfolio value:

Stocks allocation:  {'AGRO3.SA': 54, 'CIEL3.SA': 990, 'CPLE6.SA': 340, 'EGIE3.SA': 6, 'ELET3.SA': 25, 'HYPE3.SA': 50, 'ITUB4.SA': 5, 'SBSP3.SA': 31, 'SLCE3.SA': 68, 'TAEE11.SA': 49, 'UNIP6.SA': 20, 'VALE3.SA': 6}

Leftover: 0.037377230371930636 BRL

### [Project 5 - Investment Fund Analysis](https://github.com/alanceloth/PortfolioDS/tree/main/Analise_de_Fundos_de_Investimentos)

**Goal:** How to obtain and analyze investment fund data  
Answer the following questions:
1. Which fund in Brazil has the highest NAV (Net Asset Value)?
2. How to obtain the variation of the share price for a specific fund?
3. How to retrieve data for a specific fund knowing only its name?
4. Which fund had the highest increase in share price?
5. Which fund had the highest decrease in share price?
6. TO-DO: Apply a strategy to choose funds based on fundamental analysis.

**Data source:** CVM data portal

**Description:** In this project, data from the CVM (Comissão de Valores Mobiliários, a regulatory agency linked to the Ministry of Finance of Brazil) was collected for investment funds with the aim of answering the above questions.

**Disclaimer:** I am not a financial advisor. Do not take anything in this code as financial advice, ever.  
Do your own research.  
Consult a professional investment advisor before making any investment decisions!

**Results:** It was possible to perform a detailed analysis on various investment funds, answer the main questions raised, and explore investment fund data.


### [Project 6 - Deep Learning & Crypto](https://github.com/alanceloth/PortfolioDS/tree/main/Deep%20Learning%20e%20Cryptomoeda)

**Goal:** Predict Bitcoin prices using a Deep Learning model.

**Data source:** IN PROGRESS

**Description:** IN PROGRESS

**Disclaimer:** I am not a financial advisor. Do not take anything in this code as financial advice, ever.  
Do your own research.  
Consult a professional investment advisor before making any investment decisions!

**Results:** IN PROGRESS

### [Project 7 - Real Estate Investment Trusts](https://github.com/alanceloth/PortfolioDS/tree/main/fundos_imobiliarios)

**Goal:** Simulate a portfolio of real estate investment trusts, their growth through contributions and earnings.

**Data source:** IN PROGRESS

**Description:** IN PROGRESS

**Disclaimer:** I am not a financial advisor. Do not take anything in this code as financial advice, ever.  
Do your own research.  
Consult a professional investment advisor before making any investment decisions!

**Results:** IN PROGRESS

### [Project 8 - Unsupervised Analysis for Decision Making](https://github.com/alanceloth/PortfolioDS/tree/main/An%C3%A1lise%20n%C3%A3o%20supervisionada%20para%20tomada%20de%20decis%C3%B5es)

**Goal:** IN PROGRESS

**Data source:** IN PROGRESS

**Description:** IN PROGRESS

**Disclaimer:** I am not a financial advisor. Do not take anything in this code as financial advice, ever.  
Do your own research.  
Consult a professional investment advisor before making any investment decisions!

**Results:** IN PROGRESS

### [Project 9 - Autocorrelation](https://github.com/alanceloth/PortfolioDS/tree/main/Autocorrelacao)

**Goal:** IN PROGRESS

**Data source:** IN PROGRESS

**Description:** IN PROGRESS

**Disclaimer:** I am not a financial advisor. Do not take anything in this code as financial advice, ever.  
Do your own research.  
Consult a professional investment advisor before making any investment decisions!

**Results:** IN PROGRESS

### [Project 10 - Plotting Price and Volume of a Stock](https://github.com/alanceloth/PortfolioDS/tree/main/Plotando%20cota%C3%A7%C3%A3o%20de%20um%20ativo%20com%20volume)

**Goal:** Plot stock prices and volume in the same chart.

**Data source:** Yfinance

**Description:** Learn how to create a chart that displays multiple pieces of information simultaneously.

**Disclaimer:** I am not a financial advisor. Do not take anything in this code as financial advice, ever.  
Do your own research.  
Consult a professional investment advisor before making any investment decisions!

**Results:** In addition to plotting both pieces of information, a candlestick plot, commonly used by platforms that provide this type of data, was included.

### [Project 11 - Analyzing Gas Price Trends with SARIMA: Estimating Past and Future Prices](https://github.com/alanceloth/PortfolioDS/tree/main/JP%20MOrgan%20Chase%20%26%20Co%20Intern/Task%201%20-%20Estimate%20gas%20prices)

[LinkedIn Article](https://www.linkedin.com/pulse/analyzing-gas-price-trends-sarima-estimating-past-rodrigues-silva-/?trackingId=M5JXjW0rGUTguPCmXpW8vg%3D%3D)

**Goal:** Analyze the data to estimate the purchase price of gas at any date in the past and extrapolate it for one year into the future. 

**Data source:** CSV provided by JPMorgan Chase & Co.

**Description:** Learn how to create a chart that displays multiple pieces of information simultaneously. (simulated internship program JPMorgan Chase & Co.)

**Disclaimer:** I am not a financial advisor. Do not take anything in this code as financial advice, ever.  
Do your own research.  
Consult a professional investment advisor before making any investment decisions!

**Results:** In addition to plotting both pieces of information, a candlestick plot, commonly used by platforms that provide this type of data, was included.

### [Project 12 - ETF Analysis](https://github.com/alanceloth/PortfolioDS/tree/main/Analisando%20ETFs)

[LinkedIn Article](https://www.linkedin.com/pulse/analise-de-etfs-alan-lanceloth-rodrigues-silva-/?trackingId=Jk6YWFjDYo8e1TFK4LGUmg%3D%3D)

**Goal:** Create two or three hypothetical portfolios with varying numbers of ETFs and different strategies, and compare their performance. 

**Data source:** Yfinance Stocks and ETF data.

**Disclaimer:** I am not a financial advisor. Do not take anything in this code as financial advice, ever.  
Do your own research.  
Consult a professional investment advisor before making any investment decisions!

**Results:** In this project, various technical skills related to data handling, asset selection, data acquisition, and financial market data analysis were exercised. For future improvements, we can define our own strategies for stock selection or explore other asset classes (such as real estate funds). One of the most important aspects I would like to highlight in this project were the moments when it was necessary to pause and ask oneself 'Why?' or 'How am I going to define a strategy to choose this asset instead of the other one?


### [Project 13 - LinkedIn Bot](https://github.com/alanceloth/PortfolioDS/tree/main/Bot%20LinkedIn)

**Goal:** Explore the LinkedIn API to create automated posts on the platform. 

**Data source:** Various.

**Disclaimer:** I am not a financial advisor. Do not take anything in this code as financial advice, ever.  
Do your own research.  
Consult a professional investment advisor before making any investment decisions!

**Results:** Currently, the bot can make posts using the LinkedIn API on the user's account. You can add media or articles, or just text to your publication. 
Next Steps:
  - [ ] Add scheduling feature

### [Project 14 - Weekly Report](https://github.com/alanceloth/PortfolioDS/tree/main/Weekly%20Report)

**Goal:** Create a market overview report showing index results, and stock results weekly.

**Data source:** Yfinance Stocks and MetaTrader5

**Disclaimer:** I am not a financial advisor. Do not take anything in this code as financial advice, ever.  
Do your own research.  
Consult a professional investment advisor before making any investment decisions!

**Results:** As shown, in this project we managed to check the market index and stocks weekly with various types of charts.

