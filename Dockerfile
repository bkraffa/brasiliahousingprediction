FROM python:3.8

WORKDIR /bsbhousingprediction

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /bsbhousingprediction/start.bash

CMD ["sh", "-c", "uvicorn model_api:app --host 0.0.0.0 --port $PORT"]
#codigo acima pra rodar localmente, depois é necessário rodar o streamlit run streamlit.py

#CMD ["/bin/bash", "-c", "/bsbhousing/start.bash && sleep 5 && streamlit run streamlit.py --server.port $PORT"]
#codigo acima é pra o deploy em produção


#docker build . -t bsbhousing:latest
#docker run -p 8000:4000 -e PORT=4000 bsbhousing:latest
#streamlit run streamlit.py