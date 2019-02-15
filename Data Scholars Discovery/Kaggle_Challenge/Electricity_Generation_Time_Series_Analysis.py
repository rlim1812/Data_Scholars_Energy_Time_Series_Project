import pandas as pd
import plotly
from plotly.plotly import plot_mpl
import plotly.plotly as ply
from statsmodels.tsa.seasonal import seasonal_decompose
from pmdarima.arima import auto_arima

energy_data = pd.read_csv("electricity_generation_total.csv")
print(energy_data.shape)