## How to run

You can use `docker-compose` to run this application.  

1) Clone: `git clone https://github.com/dfesenko/policy-renew-predict-app.git` .  
2) Change directory: `cd policy-renew-predict-app/`.   
3) Run command: `docker-compose up`.  
4) Wait until everything will be ready.  
5) The application should be available in your browser: `http://localhost:1221/`.  

Alternatively, you can: 
1) Create new virtual environment (`python -m venv venv`).  
2) Use `requirements.txt` file to install dependencies. 
3) Run the test server using `python manage.py runserver` command.  
4) The application should be available here: `http://localhost:8000/`.   

## General information

The model was trained on the dataset with information about policy holders, their cars, etc.
The model was not fine-tuned, it is the baseline model.
On the testing dataset it gives around 69% of prediction accuracy 
(confusion matrix confirms this quality as well).

The Jupyter Notebook with training process is also available in the current repo:
`Training.ipynb`.

The focus of the development was on the backend side, so the frontend is minimal.
