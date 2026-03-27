'''
Assignment (19/03/2026)

Assignment Name : Mini Project Proposal
Description : Submit a 1-page proposal with problem, dataset, algorithm, expected output.
'''

'''
==========================================================
       MINI PROJECT PROPOSAL
       Solar Power Generation Forecasting
       For Residential and Industrial Distributed Solar Plants
==========================================================
Assignment : Mini Project Proposal
Date       : 19/03/2026
Domain     : Renewable Energy + Machine Learning
----------------------------------------------------------

1. PROBLEM STATEMENT
--------------------
Electricity consumers with rooftop or distributed solar
plants lack reliable tools to forecast their generation
output. This prevents optimal scheduling of energy-
intensive tasks, resulting in higher electricity bills
and underutilization of solar potential.

The goal is to financially empower individual and
industrial consumers by accurately predicting solar
generation, enabling them to schedule energy-consuming
tasks in coherence with solar generation patterns.

----------------------------------------------------------

2. DATASET
----------
The following data sources will be used:

  - Electricity generation logs of the solar plant
  - Local climatic data (Temperature, Humidity, Wind Speed)
  - Solar Irradiance measurements for the area of interest
  - Satellite-based cloud motion vectors
  - Historical cloud cover data

----------------------------------------------------------

3. ALGORITHM / METHODOLOGY
--------------------------
  Step 1 - Data Collection  : Aggregate solar generation
            logs, weather API data, and satellite feeds

  Step 2 - Preprocessing    : Handle missing values,
            normalize features, create time-series
            sequences

  Step 3 - Model (LSTM)     : Long Short-Term Memory
            neural network for time-series forecasting

  Step 4 - Validation       : Evaluate using MAE and
            RMSE on held-out test data

  Step 5 - Deployment       : Serve predictions via
            REST API to a dashboard frontend

----------------------------------------------------------

4. EXPECTED OUTPUT
------------------
  - Interactive dashboard with 2 to 7 day high-fidelity
    solar generation forecast for the plant

  - Hourly generation curves with confidence intervals

  - Smart scheduling suggestions for high-load appliances
    (e.g. EV charging, washing machines)

  - Savings estimator showing expected cost reduction
    vs. grid dependency


'''