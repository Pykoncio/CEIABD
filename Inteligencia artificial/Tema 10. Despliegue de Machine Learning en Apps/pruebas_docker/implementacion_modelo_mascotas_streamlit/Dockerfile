FROM python:3.12
RUN pip install -R requeriments.txt
WORKDIR /app
COPY ./* /app/
# EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "streamlit_app.py"]