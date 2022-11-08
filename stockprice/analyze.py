import vnquant.plot as pl

pl.vnquant_candle_stick(
    data='VND',
    title='VND symbol from 2019-09-01 to 2019-11-01',
    xlab='Date', ylab='Price',
    start_date='2019-09-01',
    end_date='2019-11-01',
    data_source='CAFE',
    show_advanced=['volume', 'macd', 'rsi']
)
# %%
