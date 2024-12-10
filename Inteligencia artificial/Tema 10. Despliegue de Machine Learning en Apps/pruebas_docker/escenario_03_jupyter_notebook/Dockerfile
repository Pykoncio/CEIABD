FROM python:3.10
RUN pip install numpy pandas scikit-learn seaborn jupyter notebook
WORKDIR /home/notebooks
EXPOSE 8888
COPY . .
ENTRYPOINT [ "jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser" ]

# Si queremos que no tengamos que usar token podemos usar:
# --NotebookApp.token='', --NotebookApp.password=''
