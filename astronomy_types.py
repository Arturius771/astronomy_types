from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Generic, NewType, TypeAlias, TypeVar

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


Scalar = NewType("Scalar", float)
Distance = NewType("Distance", Scalar)
Ratio = NewType("Ratio", Scalar)
Velocity = NewType("Velocity", Scalar)
Acceleration = NewType("Acceleration", Scalar)
Position = NewType("Position", Scalar)
Displacement = NewType("Displacement", Scalar)

AccelerationVector: TypeAlias = Vector3D[Acceleration]

# Measures an offset from origin (eg. a satellite relative to the Earth) in some reference frame. In orbital mechanics, the magnitude of the position vector is the orbital radius.
PositionVector: TypeAlias = Vector3D[Position]

# Measures the rate of change of a position vector in a reference frame.
VelocityVector: TypeAlias = Vector3D[Velocity]

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

Angle: TypeAlias = Radians | Degrees


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
# Semantic astronomy types
# ---------------------------------------------------------------------

Rate = NewType("Rate", Scalar)

Latitude: TypeAlias = Angle
Longitude: TypeAlias = Angle

Declination = NewType("Declination", Radians)
HourAngle = NewType("HourAngle", Radians)
RightAscension = NewType("RightAscension", Radians)
Azimuth = NewType("Azimuth", Radians)
Altitude = NewType("Altitude", Radians)
Obliquity = NewType("Obliquity", Radians)

GravitationalParameter = NewType("GravitationalParameter", Scalar)


@dataclass(frozen=True)
class GeographicCoordinates(Coordinate2D[Angle]):
    @property
    def latitude(self) -> Latitude:
        return self.x

    @property
    def longitude(self) -> Longitude:
        return self.y


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
class EclipticCoordinates(Coordinate2D[Angle]):
    @property
    def latitude(self) -> Latitude:
        return self.x

    @property
    def longitude(self) -> Longitude:
        return self.y


@dataclass(frozen=True)
class GalacticCoordinates(Coordinate2D[Angle]):
    @property
    def latitude(self) -> Latitude:
        return self.x

    @property
    def longitude(self) -> Longitude:
        return self.y


# ---------------------------------------------------------------------
# Orbital element types
# ---------------------------------------------------------------------

Inclination = NewType("Inclination", Radians)
ArgumentOfPeriapsis = NewType("ArgumentOfPeriapsis", Radians)
SemiMajorAxis = NewType("SemiMajorAxis", Distance)
Eccentricity = NewType("Eccentricity", Ratio)
SemiMinorAxis = NewType("SemiMinorAxis", Distance)

Anomaly = NewType("Anomaly", Radians)
EccentricAnomaly = NewType("EccentricAnomaly", Anomaly)
TrueAnomaly = NewType("TrueAnomaly", Anomaly)
MeanAnomaly = NewType("MeanAnomaly", Anomaly)

MeanMotion = NewType("MeanMotion", Rate)
SemiLatusRectum = NewType("SemiLatusRectum", Distance)


@dataclass(frozen=True)
class OrbitalElements:
    inclination: Inclination
    right_ascension_of_ascending_node: RightAscension
    argument_of_periapsis: ArgumentOfPeriapsis
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
