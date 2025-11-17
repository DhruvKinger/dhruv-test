
FROM dhruvreg.azurecr.io/azurefunctionsimage:v1.0.0

ENV host:logger:consoleLoggingMode=always

COPY . /home/site/wwwroot

RUN cd /home/site/wwwroot && pip install -r requirements.txt
