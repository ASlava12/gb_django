FROM python:3.8.12

WORKDIR /geekshop

COPY . /geekshop

RUN apt update && apt upgrade -y && apt-get purge && \
    python -m pip install --no-cache-dir -r /geekshop/requirements.txt && \
    useradd -g www-data -m django && \
    chown -R django:www-data /geekshop && \
    chmod -R 744 /geekshop && apt-get clean && apt-get autoclean

CMD ["/geekshop/init_app.sh"]
