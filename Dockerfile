FROM python:3.8 
# Or any preferred Python version.
ADD main.py .
RUN pip install requests pytest pytest-html
CMD ["python", "./main.py"] 
# Or enter the name of your unique directory and parameter set.