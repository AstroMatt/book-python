********
Examples
********


ISS Ground Track
================
.. code-block:: python
    :caption: Source: https://beyond.readthedocs.io/en/latest/examples.html

    #!/usr/bin/env python

    """Script showing the position of the ISS at the time of the TLE
    and the ground track for the previous and the next orbit
    """

    import sys
    from pathlib import Path

    import matplotlib.pyplot as plt
    import numpy as np

    from beyond.io.tle import Tle
    from beyond.dates import Date, timedelta


    # Parsing of TLE
    tle = Tle("""ISS (ZARYA)
    1 25544U 98067A   19004.59354167  .00000715  00000-0  18267-4 0  9995
    2 25544  51.6416  95.0104 0002419 236.2184 323.8248 15.53730729149833""")

    # Conversion into `Orbit` object
    orb = tle.orbit()

    # Tables containing the positions of the ground track
    latitudes, longitudes = [], []
    prev_lon, prev_lat = None, None

    period = orb.infos.period
    start = orb.date - period
    stop = 2 * period
    step = period / 100

    for point in orb.ephemeris(start=start, stop=stop, step=step):

        # Conversion to earth rotating frame
        point.frame = 'ITRF'

        # Conversion from cartesian to spherical coordinates (range, latitude, longitude)
        point.form = 'spherical'

        # Conversion from radians to degrees
        lon, lat = np.degrees(point[1:3])

        # Creation of multiple segments in order to not have a ground track
        # doing impossible paths
        if prev_lon is None:
            lons = []
            lats = []
            longitudes.append(lons)
            latitudes.append(lats)
        elif orb.i < np.pi /2 and (np.sign(prev_lon) == 1 and np.sign(lon) == -1):
            lons.append(lon + 360)
            lats.append(lat)
            lons = [prev_lon - 360]
            lats = [prev_lat]
            longitudes.append(lons)
            latitudes.append(lats)
        elif orb.i > np.pi/2 and (np.sign(prev_lon) == -1 and np.sign(lon) == 1):
            lons.append(lon - 360)
            lats.append(lat)
            lons = [prev_lon + 360]
            lats = [prev_lat]
            longitudes.append(lons)
            latitudes.append(lats)

        lons.append(lon)
        lats.append(lat)
        prev_lon = lon
        prev_lat = lat

    img = Path(__file__).parent / "earth.png"

    im = plt.imread(str(img))
    plt.figure(figsize=(15.2, 8.2))
    plt.imshow(im, extent=[-180, 180, -90, 90])

    for lons, lats in zip(longitudes, latitudes):
        plt.plot(lons, lats, 'r')

    lon, lat = np.degrees(orb.copy(frame='ITRF', form='spherical')[1:3])
    plt.plot([lon], [lat], 'ro')

    plt.xlim([-180, 180])
    plt.ylim([-90, 90])
    plt.grid(True, color='w', linestyle=":", alpha=0.4)
    plt.xticks(range(-180, 181, 30))
    plt.yticks(range(-90, 91, 30))
    plt.tight_layout()

    if "no-display" not in sys.argv:
        plt.show()


ISS Hohmann transfer
====================
.. code-block:: python
    :caption: https://beyond.readthedocs.io/en/latest/examples.html

    """Example of Hohmann transfer

    The orbit we are starting with is a Tle of the ISS. The amplitude of the maneuver is greatly
    exagerated regarding the ISS's capability, but has the convenience to be particularly visual.
    """

    import sys

    import matplotlib.pyplot as plt
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D

    from beyond.io.tle import Tle
    from beyond.dates import timedelta
    from beyond.propagators.keplernum import KeplerNum
    from beyond.env.solarsystem import get_body
    from beyond.orbits.man import ImpulsiveMan
    from beyond.orbits.listeners import ApsideListener, find_event


    orb = Tle("""ISS (ZARYA)
    1 25544U 98067A   18124.55610684  .00001524  00000-0  30197-4 0  9997
    2 25544  51.6421 236.2139 0003381  47.8509  47.6767 15.54198229111731""").orbit()

    start = orb.date
    stop = timedelta(minutes=300)
    step = timedelta(seconds=60)

    # Changing the propagator to Keplerian, as SGP4 is not able to perform maneuvers
    orb.propagator = KeplerNum(step, bodies=get_body("Earth"))

    # Research for the next perigee
    perigee = find_event(orb.iter(stop=stop, listeners=ApsideListener()), 'Periapsis')

    man1 = ImpulsiveMan(perigee.date, (280, 0, 0), frame="TNW")
    orb.maneuvers = [man1]

    dates1, alt1 = [], []

    # Research for the next apogee after the first maneuver
    apogee = find_event(orb.iter(start=perigee.date - step * 10, stop=stop, listeners=ApsideListener()), 'Apoapsis')
    # apogee = find_event(orb.iter(stop=stop, listeners=ApsideListener()), 'Apoapsis', offset=1)

    # Adding the second maneuver to the orbit
    man2 = ImpulsiveMan(apogee.date, (270, 0, 0), frame="TNW")
    orb.maneuvers.append(man2)

    print(man1.date)
    print(man2.date)

    # Propagation throught the two maneuvers
    ephem = orb.ephem(start=start, stop=stop, step=step)

    # graphs
    plt.figure()

    data = np.array(ephem)
    dates = [x.date for x in ephem]
    # Altitude in km
    alt = (np.linalg.norm(data[:, :3], axis=1) - orb.frame.center.body.r) / 1000
    events_dates = [perigee.date, apogee.date]
    events_alt = (np.linalg.norm([perigee[:3], apogee[:3]], axis=1) - orb.frame.center.body.r) / 1000

    plt.plot(dates, alt)
    plt.plot([events_dates[0]], [events_alt[0]], 'ro', label="perigee")
    plt.plot([events_dates[1]], [events_alt[1]], 'ko', label="apogee")

    plt.ylabel("altitude (km)")
    plt.legend()
    plt.grid(linestyle=':', alpha=0.4)
    plt.tight_layout()

    fig = plt.figure()
    ax = plt.gca(projection='3d')
    ax.view_init(elev=52, azim=140)

    x, y, z = zip(perigee[:3], apogee[:3])

    plt.plot(data[:, 0], data[:, 1], data[:, 2])
    plt.plot([perigee[0]], [perigee[1]], [perigee[2]], 'ro')
    plt.plot([apogee[0]], [apogee[1]], [apogee[2]], 'ko')

    if "no-display" not in sys.argv:
        plt.show()


COVID-19
========
* Data Source: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
* https://www.youtube.com/watch?v=54XLXg4fYsc
* https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
* https://aatishb.com/covidtrends/?location=Poland
* https://aatishb.com/covidtrends/?location=Brazil&location=China&location=India&location=Poland&location=Russia&location=US
* https://youtu.be/xtZYKcOdJp0?t=168


.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd

    CONFIRMED = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    DEATHS = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
    RECOVERED = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

    confirmed = pd.read_csv(CONFIRMED)
    deaths = pd.read_csv(DEATHS)
    recovered = pd.read_csv(RECOVERED)


    def plot(name: str) -> None:
        # Select matching country
        c = confirmed['Country/Region'] == name
        d = deaths['Country/Region'] == name
        r = recovered['Country/Region'] == name

        # Merge data and discard not needed columns
        df = pd.concat([
            confirmed.loc[c].transpose()[4:],
            deaths.loc[d].transpose()[4:],
            recovered.loc[r].transpose()[4:]
        ], axis=1, keys=['Confirmed', 'Deaths', 'Recovered'])

        # Set columns and index
        df.columns = df.columns.droplevel(1)
        df.index = pd.to_datetime(df.index)
        df.sort_index(ascending=True, inplace=True)

        # Create figure and axis objects
        fig, ax = plt.subplots(
            nrows=3,
            ncols=1,
            sharex=True,
            sharey=False,
            gridspec_kw={'height_ratios': [2, 1, 1]},
            figsize=(15, 5))

        # Set layout for 'Confirmed' cases
        ax[0].plot(df['Confirmed'], color='red')
        ax[0].set_ylim(ymin=0, ymax=None)
        ax[0].set_ylabel('Confirmed')
        ax[0].grid(True, which='major')

        # Set layout for 'Deaths' cases
        ax[1].plot(df['Deaths'], color='black')
        ax[1].set_ylim(ymin=0, ymax=None)
        ax[1].set_ylabel('Deaths')
        ax[1].grid(True, which='major')

        # Set layout for 'Recovered' cases
        ax[2].plot(df['Recovered'], color='green')
        ax[2].set_ylim(ymin=0, ymax=None)
        ax[2].set_ylabel('Recovered')
        ax[2].grid(True, which='major')

        # Set general layout for figure (all axis)
        fig.tight_layout()
        plt.setp(ax[2].get_xticklabels(), rotation=45, horizontalalignment='right')
        plt.show()


    plot('Poland')
    plot('Germany')
    plot('France')
    plot('Spain')
    plot('Italy')
