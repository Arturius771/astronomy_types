from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from math import radians
import math
from typing import Generic, NewType, TypeVar

T = TypeVar("T")

# ---------------------------------------------------------------------
# Physics
# ---------------------------------------------------------------------


@dataclass(frozen=True)
class Coordinate2D(Generic[T]):
    x: T
    y: T


@dataclass(frozen=True)
class Coordinate3D(Generic[T]):
    x: T
    y: T
    z: T


@dataclass(frozen=True)
class Vector2D(Generic[T]):
    x: T
    y: T


@dataclass(frozen=True)
class Vector3D(Generic[T]):
    x: T
    y: T
    z: T


# A quantity defined by a single value *and* a unit
Scalar = NewType("Scalar", float)
Distance = NewType("Distance", Scalar)
Ratio = NewType("Ratio", Scalar)
Velocity = NewType("Velocity", Scalar)
Acceleration = NewType("Acceleration", Scalar)
Position = NewType("Position", Scalar)
VelocityVector = Vector3D[Velocity]
AccelerationVector = Vector3D[Acceleration]
PositionVector = Vector3D[Position]
Displacement = NewType("Displacement", Scalar)


# ---------------------------------------------------------------------
# Time
# ---------------------------------------------------------------------


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
Day = NewType("Day", Scalar)
Hour = NewType("Hour", int)
Minute = NewType("Minute", int)
Second = NewType("Second", Scalar)
JulianDate = NewType("JulianDate", Scalar)
DecimalTime = NewType("DecimalTime", Scalar)
Epoch = NewType("Epoch", JulianDate)

# ---------------------------------------------------------------------
# Core angle representations
# ---------------------------------------------------------------------

Radians = NewType("Radians", Scalar)
Degrees = NewType("Degrees", Scalar)


@dataclass(frozen=True)
class DMS:
    """
    Degrees, arcminutes, arcseconds.
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


# ---------------------------------------------------------------------
# Conversion helpers
# ---------------------------------------------------------------------


def degrees_to_radians(value: Degrees) -> Radians:
    return Radians(Scalar(radians(float(value))))


def dms_to_degrees(value: DMS) -> Degrees:
    sign = -1 if value.degrees < 0 else 1
    return Degrees(
        Scalar(sign * (abs(value.degrees) + value.minutes / 60 + value.seconds / 3600))
    )


def dms_to_radians(value: DMS) -> Radians:
    return degrees_to_radians(dms_to_degrees(value))


def hms_to_degrees(value: HMS) -> Degrees:
    return Degrees(
        Scalar(15 * (value.hours + value.minutes / 60 + value.seconds / 3600))
    )


def hms_to_radians(value: HMS) -> Radians:
    return degrees_to_radians(hms_to_degrees(value))


def hours_to_degrees(hours: DecimalTime) -> Degrees:
    return Degrees(Scalar(float(hours) * 15))


def degrees_to_hours(degrees: Degrees) -> DecimalTime:
    return DecimalTime(Scalar(float(degrees) / 15))


def time_to_decimal_time(time: Time) -> DecimalTime:
    unsigned_decimal = (
        int(time.hour) + int(time.minute) / 60 + float(time.second) / 3600
    )

    return DecimalTime(Scalar(unsigned_decimal))


def decimal_time_to_time(decimal_value: DecimalTime) -> Time:
    unsigned_decimal = abs(float(decimal_value))

    total_seconds = unsigned_decimal * 3600
    rounded_seconds = round(total_seconds % 60, 2)

    seconds = 0 if rounded_seconds == 60 else rounded_seconds
    remainder = total_seconds + 60 if rounded_seconds == 60 else total_seconds

    minutes = math.floor(remainder / 60) % 60
    hours = math.floor(remainder / 3600)

    return Time(
        Hour(hours),
        Minute(minutes),
        Second(Scalar(seconds)),
    )


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

# ---------------------------------------------------------------------

Rate = NewType("Rate", Scalar)

# ---------------------------------------------------------------------
# Semantic astronomy types
# ---------------------------------------------------------------------

Latitude = NewType("Latitude", Radians)
Longitude = NewType("Longitude", Radians)
Declination = NewType("Declination", Radians)
HourAngle = NewType("HourAngle", Radians)
RightAscension = NewType("RightAscension", Radians)
Azimuth = NewType("Azimuth", Radians)
Altitude = NewType("Altitude", Radians)
Obliquity = NewType("Obliquity", Radians)
GravitationalParameter = NewType("GravitationalParameter", Scalar)


@dataclass(frozen=True)
class GeographicCoordinates(Coordinate2D[Radians]):
    @property
    def latitude(self) -> Latitude:
        return Latitude(self.x)

    @property
    def longitude(self) -> Longitude:
        return Longitude(self.y)


@dataclass(frozen=True)
class HorizontalCoordinates(Coordinate2D[Radians]):
    @property
    def altitude(self) -> Altitude:
        return Altitude(self.x)

    @property
    def azimuth(self) -> Azimuth:
        return Azimuth(self.y)


@dataclass(frozen=True)
class EquatorialCoordinatesHourAngle(Coordinate2D[Radians]):
    @property
    def declination(self) -> Declination:
        return Declination(self.x)

    @property
    def hour_angle(self) -> HourAngle:
        return HourAngle(self.y)


@dataclass(frozen=True)
class EquatorialCoordinates(Coordinate2D[Radians]):
    @property
    def declination(self) -> Declination:
        return Declination(self.x)

    @property
    def right_ascension(self) -> RightAscension:
        return RightAscension(self.y)


@dataclass(frozen=True)
class EclipticCoordinates(Coordinate2D[Radians]):
    @property
    def latitude(self) -> Latitude:
        return Latitude(self.x)

    @property
    def longitude(self) -> Longitude:
        return Longitude(self.y)


@dataclass(frozen=True)
class GalacticCoordinates(Coordinate2D[Radians]):
    @property
    def latitude(self) -> Latitude:
        return Latitude(self.x)

    @property
    def longitude(self) -> Longitude:
        return Longitude(self.y)


# ---------------------------------------------------------------------
# Orbital element types
# ---------------------------------------------------------------------

# Describe the orbital ellipse:
Inclination = NewType("Inclination", Radians)
ArgumentOfPerigee = NewType("ArgumentOfPerigee", Radians)
SemiMajorAxis = NewType("SemiMajorAxis", Distance)
Eccentricity = NewType("Eccentricity", Ratio)
SemiMinorAxis = NewType("SemiMinorAxis", Distance)

# Describe the position on the ellipse:
Anomaly = NewType("Anomaly", Radians)
EccentricAnomaly = NewType(
    "EccentricAnomaly", Anomaly
)  # Angle of object in its orbit relative to a fictional circular orbit from the centre of orbital ellipse
TrueAnomaly = NewType(
    "TrueAnomaly", Anomaly
)  # Angle of object on orbit ellipse measured from the focus.
MeanAnomaly = NewType(
    "MeanAnomaly", Anomaly
)  # Angle in which an object would move along a fictional circle in the same amount of time as the actual object.

MeanMotion = NewType("MeanMotion", Rate)


@dataclass(frozen=True)
class OrbitalElements:
    inclination: Inclination
    right_ascension_of_ascending_node: RightAscension
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


@dataclass(frozen=True)
class StateVectors:
    position: PositionVector
    velocity: VelocityVector
