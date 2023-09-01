This project is quite simple, however it takes a special place into my journey since it was my first university project with Python. \
The idea was to work on a substantial quantity of data gathered in Lombardia (Italy) in order to provide a statistical explaination of the Covid-19 high number of cases in the region during the pandemic era. \

The project outline is to compare some Air Quality variables and also to use some climatic data to explain the severe pandemic situation in Lombardia/Milan. With a Naive analysis a correlation between worsening of air quality and new number of cases appears. \

The considered variables are:
- Air Quality variables: Air Quality Index (AQI), Particulate Matter 2.5 Period Average (PM2.5 Av), Particulate Matter 10 Period Average (PM10 Av), Particulate Matter 10 Maximum observation (PM10 Max)\
- Climatic Data: Air Temperature, Maximum Windspeed, Relative Humidity \

Since we have shown that AQI has a very similar pattern to the PMs and also considering the correlations between climatic data and response (new covid cases) the covariates are: 
- AQI
- Air Temperature
- Maximum Windspeed

Disclaimers:

The project was inspired by the following paper: \
M. A. Zoran R,., S., Savastru, D., M. Savastru, Marina. & N., Tautan. Assessing the relationship between surface levels of PM2.5 and PM10 particulate matter impact on COVID-19 in Milan, Italy \

Covid data are taken from:
https://github.com/pcm-dpc/COVID-19 \

This repository contains only some of the outputs
