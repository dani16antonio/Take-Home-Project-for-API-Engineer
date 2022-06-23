# Take Home Project for API Engineer
This is project is an only one endpoint backend service, follow these steps to run the project.
## Create python virtual environment (optional)
If you are running this project in your local machine, I recommend using a python virtual environment, but this is optional, to create and activate a virtual environment run these commands:

`virtualenv .venv`
`source .venv/bin/activate`
Note: make sure you have `virtualenv` installed.

## Install dependencies
To install all python packaged required to run this project execute this command:
`pip install -r requirements.txt`

## Create envvar file
There is a file named `.env-example` rename it to `.env` and change the value of all environment variables to the actual values.

## Run the project
Once everything is ready execute this code to run the project:
`uvicorn main:app`

## Make a request
In order to make a request, make a `GET` request to `/menu/<YYYY-MM-DD>/<type>`
NOTE:`<YYYY-MM-DD>` is a date i.e. **2021-03-03** and `<type>` is a string i.e. **MEAL_KIT**.

Thank you for reading.