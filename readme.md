# Building api with ython with FastAPI and Uvicorn, and Postgres
## Preparing Environment
 ``` 
 pip3 install fastapi "uvicorn[standard]"
 ```

 - Use <b>pydantic</b> to create and validate models 

 ### Running application
 - uvicorn {module_name}: app --reload
 ```
 uvicorn main:app --reload
 ```

 - accessing your api via swagger 
 http://localhost:8000/docs
