from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from math import radians
from typing import NewType


class DaysOfWeek(str, Enum):
    Sunday = "Sunday"
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
    Saturday = "Saturday"


Year = NewType("Year", int)
Month = NewType("Month", int)
Day = NewType("Day", float)

Hour = NewType("Hour", int)
Minute = NewType("Minute", int)
Second = NewType("Second", float)

JulianDate = NewType("JulianDate", float)
DecimalTime = NewType("DecimalTime", float)
Epoch = NewType("Epoch", JulianDate)


# ---------------------------------------------------------------------
# Core angle representations
# ---------------------------------------------------------------------

Radians = NewType("Radians", float)
Degrees = NewType("Degrees", float)


@dataclass(frozen=True)
class DMS:
    """
    Degrees, arcminutes, arcseconds.

    Used for input/output formatting, not for internal calculations.
    """

    degrees: int
    minutes: int
    seconds: float


@dataclass(frozen=True)
class HMS:
    """
    Hours, minutes, seconds.

    Used for right ascension and sidereal time style values.
    """

    hours: int
    minutes: int
    seconds: float


def degrees_to_radians(value: Degrees) -> Radians:
    return Radians(radians(float(value)))


def dms_to_degrees(value: DMS) -> Degrees:
    sign = -1 if value.degrees < 0 else 1

    return Degrees(
        sign * (abs(value.degrees) + value.minutes / 60 + value.seconds / 3600)
    )


def dms_to_radians(value: DMS) -> Radians:
    return degrees_to_radians(dms_to_degrees(value))


def hms_to_degrees(value: HMS) -> Degrees:
    return Degrees(15 * (value.hours + value.minutes / 60 + value.seconds / 3600))


def hms_to_radians(value: HMS) -> Radians:
    return degrees_to_radians(hms_to_degrees(value))


# ---------------------------------------------------------------------
# Date and time structures
# ---------------------------------------------------------------------


@dataclass(frozen=True)
class Date:
    year: Year
    month: Month
    day: Day


@dataclass(frozen=True)
class Time:
    hour: Hour
    minute: Minute
    second: Second


@dataclass(frozen=True)
class FullDate:
    date: Date
    time: Time


# ---------------------------------------------------------------------
# Semantic astronomy angle types
# ---------------------------------------------------------------------

Latitude = NewType("Latitude", Radians)
Longitude = NewType("Longitude", Radians)

Declination = NewType("Declination", Radians)
HourAngle = NewType("HourAngle", Radians)
RightAscension = NewType("RightAscension", Radians)

Azimuth = NewType("Azimuth", Radians)
Altitude = NewType("Altitude", Radians)

Obliquity = NewType("Obliquity", Radians)


@dataclass(frozen=True)
class GeographicCoordinates:
    latitude: Latitude
    longitude: Longitude


@dataclass(frozen=True)
class HorizontalCoordinates:
    altitude: Altitude
    azimuth: Azimuth


@dataclass(frozen=True)
class EquatorialCoordinatesHourAngle:
    declination: Declination
    hour_angle: HourAngle


@dataclass(frozen=True)
class EquatorialCoordinates:
    declination: Declination
    right_ascension: RightAscension


@dataclass(frozen=True)
class EclipticCoordinates:
    latitude: Latitude
    longitude: Longitude


@dataclass(frozen=True)
class GalacticCoordinates:
    latitude: Latitude
    longitude: Longitude


# ---------------------------------------------------------------------
# Orbital element types
# ---------------------------------------------------------------------

Inclination = NewType("Inclination", Radians)
RightAscensionOfAscendingNode = NewType(
    "RightAscensionOfAscendingNode",
    Radians,
)
ArgumentOfPerigee = NewType("ArgumentOfPerigee", Radians)
TrueAnomaly = NewType("TrueAnomaly", Radians)

SemiMajorAxis = NewType("SemiMajorAxis", float)
Eccentricity = NewType("Eccentricity", float)


@dataclass(frozen=True)
class OrbitalElements:
    inclination: Inclination
    right_ascension_of_ascending_node: RightAscensionOfAscendingNode
    argument_of_perigee: ArgumentOfPerigee
    semi_major_axis: SemiMajorAxis
    eccentricity: Eccentricity
    true_anomaly: TrueAnomaly


@dataclass(frozen=True)
class RisingAndSetting:
    circumpolar: bool
    rise_time: Time
    set_time: Time
    rise_azimuth: Azimuth
    set_azimuth: Azimuth


@dataclass(frozen=True)
class NutationAndObliquity:
    nutation_longitude: Longitude
    nutation_obliquity: Obliquity
