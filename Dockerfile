FROM python:3.11-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
RUN mkdir ~/.streamlit
WORKDIR /app
ENTRYPOINT ["streamlit", "run"]
CMD ["PoolApp.py"]