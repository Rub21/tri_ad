FROM python:3.6-alpine

COPY requirements.txt .
RUN pip install --upgrade --ignore-installed --no-cache-dir -r requirements.txt
WORKDIR /mnt/scripts/
COPY . .
RUN python setup.py install
RUN python -m unittest
CMD ["tri_ad"]
