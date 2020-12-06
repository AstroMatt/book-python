import json
from datetime import datetime, timezone
import logging
import sqlite3
import serial


logging.basicConfig(
    format='[%(asctime).19s] %(levelname)s %(message)s',
    level=logging.INFO)

DATABASE = '/home/pi/database/sensor-data.sqlite3'
DEVICE = '/dev/ttyACM0'
UNITS = {
    'air_temperature': 'C',
    'air_humidity': '%',
    'water_temperature': 'C',
    'luminosity': 'lux',
    'power_k1': 'on/off',
    'power_k2': 'on/off',
    'power_k3': 'on/off',
    'power_k4': 'on/off'}

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS sensor_data (
        datetime DATETIME PRIMARY KEY,
        sync_datetime DATETIME DEFAULT NULL,
        device VARCHAR(255),
        parameter VARCHAR(255),
        value REAL,
        unit VARCHAR(255));"""

SQL_CREATE_INDEX_SYNCDATETIME = """
    CREATE INDEX IF NOT EXISTS sensor_data_sync_datetime_index
    ON sensor_data (sync_datetime);"""

SQL_CREATE_INDEX_DATETIME = """
    CREATE UNIQUE INDEX IF NOT EXISTS sensor_data_datetime_index
    ON sensor_data (datetime);"""

SQL_INSERT = """
    INSERT INTO sensor_data
    VALUES (:datetime, NULL, :device, :parameter, :value, :unit);"""


with sqlite3.connect(DATABASE) as db:
    db.execute(SQL_CREATE_TABLE)
    db.execute(SQL_CREATE_INDEX_DATETIME)
    db.execute(SQL_CREATE_INDEX_SYNCDATETIME)


def save_to_sqlite3(data):
    data = [{'datetime': datetime.now(timezone.utc),
             'parameter': parameter,
             'value': float(value),
             'unit': UNITS.get(parameter, None),
             'device': 'hydroponics'}
            for parameter, value in data.items()]

    with sqlite3.connect(DATABASE) as db:
        db.executemany(SQL_INSERT, data)


with serial.Serial(port=DEVICE, baudrate=115200) as usb:
    while True:
        line = usb.readline()
        try:
            data = json.loads(line)
            save_to_sqlite3(data)
            logging.info(data)
        except json.decoder.JSONDecodeError:
            logging.error(line)
