<h1 align="center"><font color="orange"> Flask API for NPS Scores </font></h1>

This repository contains the code for a Flask API which uses MongoDB to store the JSON Data. This API takes the date-range as input parameters and returns a list of NPS scores for each individual date for that date-range.<br><br><br>

<h2><font color="cyan"> Task </font></h2>
<hr>
Returns a list of NPS scores for each individual date for that date-range.

<font color="yellow"> Sample Query : http://localhost:5000/getnps?startDate=2020-10-15&endDate=2020-10-17 </font>
<br><br><br>

<h2><font color="cyan"> Setup </font></h2>
<hr>
1. Clone this repository. <br>
2. Create a virtualenv and activate. <br>
3. Install requirement packages. <br>
4. Edit the executionary.py file and paste your MongoDB Database URL there as directed in the executionary.py file. <br>
5. Start the Flask application on your original terminal window: `python flask_app.py` <br>
6. Open Postman and send a get request.
<br><br><br>

<h2><font color="cyan"> Sample JSON Data </font></h2>

<hr>

```
{ 'responses'  : {
	'Response-id-1' : {
		'Score' : 8,
		'Date' : '2020-10-15'
      },
	'Response-id-2' : {
		'Score' : 3,
            'Date' : '2019-10-07'

      },
      ……. Add more data points like above …...
}}
```

<br><br>

<h2><font color="cyan"> Sample Response </font></h2>

<hr>

```
{
	"2020-10-07":8.87,
	"2020-10-10":6,
	"2020-10-15":4.23,
	"2020-10-20":0.67,
	"2020-11-15":2.09,
	and so on......
}

```
