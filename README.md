# Weather App with OpenWeather API
![image](https://user-images.githubusercontent.com/75499598/174004516-8e044cee-349b-4739-9343-797221080173.png)

With this program, you can be informed about the weather conditions in different cities of the world. This program uses OpenWeather APIs. Therefore, before running the program, you must register on [its website](https://openweathermap.org).

**The API key is all you need to call any of our weather APIs. Once you sign up using your email, the API key (APPID) will be sent to you in a confirmation email. Your API keys can always be found on your account page, where you can also generate additional API keys if needed.**

## How does this program work?
This program sends a request to the desired API every 24 hours. Its response is converted to ```JSON``` format by the program and after receiving the desired data from this response, that information is entered into the database.

## How to use this program
1.To run this program, you need to install the dependencies related to the program so that you can run the program. All the necessary libraries are placed in the requirements.txt file. You can install them one by one with the command pip install or install all the libraries together with the following command:
```
$ pip install -r requirements.txt
```

2.How all parts of the program work are specified with the comments I put in each part.

3.For more security this program we recommended that you create an ```.env``` file in the ```src/``` folder and put the API KEY in it as follows:
```
API_KEY=your API KEY
```

4.To build a table in the database, we suggest you build your table in the database as follows:
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
5- After doing all the above and connecting API KEY and database to the program, you can enter the ```src/``` folder, then open the terminal in this folder and run the program with the following command
```
$ python3 main.py
```

**Please email me(shahriaarrr@gmail.com) your feedback from this project And to report problems with this program or request a new feature, you can register an [issue](https://github.com/shahriaarrr/Weather_App/issues/new).**

----
Developing with ♥ by Shahriar Ghasempour. 2022 ©
