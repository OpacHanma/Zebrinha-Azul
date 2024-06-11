from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    location = Column(String, nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=True)
    datetime = Column(DateTime, nullable=False)

class TrafficData(Base):
    __tablename__ = 'traffic_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    duration_seconds = Column(Float, nullable=False)
    distance_meters = Column(Float, nullable=False)
    datetime = Column(DateTime, nullable=False)

def create_db_and_tables(engine_url='sqlite:///zebrinha_azul.db'):
    if isinstance(engine_url, str):
        engine = create_engine(engine_url)
    else:
        engine = engine_url
    Base.metadata.create_all(engine)
    return engine

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

if __name__ == "__main__":
    engine = create_db_and_tables()
    session = get_session(engine)

    weather_sample = WeatherData(
        location='London',
        temperature=280.32,
        humidity=81,
        datetime='2020-11-12 12:00:00'
    )
    traffic_sample = TrafficData(
        origin='New York',
        destination='Los Angeles',
        duration_seconds=3600,
        distance_meters=10000,
        datetime='2020-11-12 12:00:00'
    )

    session.add(weather_sample)
    session.add(traffic_sample)
    session.commit()
