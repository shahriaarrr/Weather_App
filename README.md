# Weather_App
With this program, you can be informed about the weather conditions in different cities of the world. This program uses OpenWeather APIs. Therefore, before running the program, you must register on [its website](https://openweathermap.org).

**The API key is all you need to call any of our weather APIs. Once you sign up using your email, the API key (APPID) will be sent to you in a confirmation email. Your API keys can always be found on your account page, where you can also generate additional API keys if needed.**

## How to use this program

1.How all parts of the program work are specified with the comments I put in each part.

2.For more security this program we recommended that you create an ```.env``` file in the ```src/``` folder and put the API KEY in it as follows:
```
API_KEY=your API KEY
```

3.To build a table in the database, we suggest you build your table in the database as follows:
```sql
CREATE TABLE {table name}(
  Temperature_C FLOAT(10),
  Humidity FLOAT,
  Wind_Speed FLOAT,
  General_weather varchar(50),
  Sun_rises varchar(50),
  Sun_Sets varchar(50)
)
```
----
Developing with ♥ by Shahriar Ghasempour. 202 ©
