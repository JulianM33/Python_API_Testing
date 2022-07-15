# Python_API_Testing
In this project, some API endpoints from developers.themoviedb.org/3. Using an API key, we had access to some API endpoints. Tests were performed in Python 3.8,  and libraries Pytest and Requests were used, which are taken care of in the Dockerfile.

A total of 6 API tests were made, of which one does not successfully get the desired response, which is I think due to the site. This is explained further the comments of main.py.


## How to run
First we must build an image using the Dockerfile. When located in the root project of the folder, run 

    docker build --tag <app_name>


After the image is built successfully, run:

    docker run <app_name>
To execute the tests, run 

    pytest main.py

To generate a full HTML report, run 

    pytest --html=report.html
