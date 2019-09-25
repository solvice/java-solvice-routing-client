# coding: utf-8

"""
    OnRoute API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Options(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'profile': 'str',
        'allow_overtime': 'bool',
        'overconstrained': 'bool',
        'minimize_vehicle_use': 'bool',
        'traffic': 'int',
        'polylines': 'bool',
        'time_unit': 'str',
        'force_type_constraints': 'bool'
    }

    attribute_map = {
        'profile': 'profile',
        'allow_overtime': 'allow_overtime',
        'overconstrained': 'overconstrained',
        'minimize_vehicle_use': 'minimize_vehicle_use',
        'traffic': 'traffic',
        'polylines': 'polylines',
        'time_unit': 'timeUnit',
        'force_type_constraints': 'force_type_constraints'
    }

    def __init__(self, profile=None, allow_overtime=None, overconstrained=None, minimize_vehicle_use=None, traffic=None, polylines=None, time_unit='MINUTES', force_type_constraints=None):  # noqa: E501
        """Options - a model defined in Swagger"""  # noqa: E501
        self._profile = None
        self._allow_overtime = None
        self._overconstrained = None
        self._minimize_vehicle_use = None
        self._traffic = None
        self._polylines = None
        self._time_unit = None
        self._force_type_constraints = None
        self.discriminator = None
        if profile is not None:
            self.profile = profile
        if allow_overtime is not None:
            self.allow_overtime = allow_overtime
        if overconstrained is not None:
            self.overconstrained = overconstrained
        if minimize_vehicle_use is not None:
            self.minimize_vehicle_use = minimize_vehicle_use
        if traffic is not None:
            self.traffic = traffic
        if polylines is not None:
            self.polylines = polylines
        if time_unit is not None:
            self.time_unit = time_unit
        if force_type_constraints is not None:
            self.force_type_constraints = force_type_constraints

    @property
    def profile(self):
        """Gets the profile of this Options.  # noqa: E501

        All vehicles are either CAR or TRUCK.  # noqa: E501

        :return: The profile of this Options.  # noqa: E501
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this Options.

        All vehicles are either CAR or TRUCK.  # noqa: E501

        :param profile: The profile of this Options.  # noqa: E501
        :type: str
        """
        allowed_values = ["CAR", "TRUCK"]  # noqa: E501
        if profile not in allowed_values:
            raise ValueError(
                "Invalid value for `profile` ({0}), must be one of {1}"  # noqa: E501
                .format(profile, allowed_values)
            )

        self._profile = profile

    @property
    def allow_overtime(self):
        """Gets the allow_overtime of this Options.  # noqa: E501

        If the `shiftend` should be a soft condition to take into account. When `allow_overtime: true` then some orders will be planned after `shiftend`.   # noqa: E501

        :return: The allow_overtime of this Options.  # noqa: E501
        :rtype: bool
        """
        return self._allow_overtime

    @allow_overtime.setter
    def allow_overtime(self, allow_overtime):
        """Sets the allow_overtime of this Options.

        If the `shiftend` should be a soft condition to take into account. When `allow_overtime: true` then some orders will be planned after `shiftend`.   # noqa: E501

        :param allow_overtime: The allow_overtime of this Options.  # noqa: E501
        :type: bool
        """

        self._allow_overtime = allow_overtime

    @property
    def overconstrained(self):
        """Gets the overconstrained of this Options.  # noqa: E501

        If you do not need to assign every order to a vehicle, then set `overconstrained: true`.   # noqa: E501

        :return: The overconstrained of this Options.  # noqa: E501
        :rtype: bool
        """
        return self._overconstrained

    @overconstrained.setter
    def overconstrained(self, overconstrained):
        """Sets the overconstrained of this Options.

        If you do not need to assign every order to a vehicle, then set `overconstrained: true`.   # noqa: E501

        :param overconstrained: The overconstrained of this Options.  # noqa: E501
        :type: bool
        """

        self._overconstrained = overconstrained

    @property
    def minimize_vehicle_use(self):
        """Gets the minimize_vehicle_use of this Options.  # noqa: E501

        Minimise the vehicle useage or minimise total travel time. Two different objective functions.  # noqa: E501

        :return: The minimize_vehicle_use of this Options.  # noqa: E501
        :rtype: bool
        """
        return self._minimize_vehicle_use

    @minimize_vehicle_use.setter
    def minimize_vehicle_use(self, minimize_vehicle_use):
        """Sets the minimize_vehicle_use of this Options.

        Minimise the vehicle useage or minimise total travel time. Two different objective functions.  # noqa: E501

        :param minimize_vehicle_use: The minimize_vehicle_use of this Options.  # noqa: E501
        :type: bool
        """

        self._minimize_vehicle_use = minimize_vehicle_use

    @property
    def traffic(self):
        """Gets the traffic of this Options.  # noqa: E501

        Modifier for traffic.  # noqa: E501

        :return: The traffic of this Options.  # noqa: E501
        :rtype: int
        """
        return self._traffic

    @traffic.setter
    def traffic(self, traffic):
        """Sets the traffic of this Options.

        Modifier for traffic.  # noqa: E501

        :param traffic: The traffic of this Options.  # noqa: E501
        :type: int
        """

        self._traffic = traffic

    @property
    def polylines(self):
        """Gets the polylines of this Options.  # noqa: E501

        Let our map server calculate the actual polylines for connecting the visits. Processing will take longer.  # noqa: E501

        :return: The polylines of this Options.  # noqa: E501
        :rtype: bool
        """
        return self._polylines

    @polylines.setter
    def polylines(self, polylines):
        """Sets the polylines of this Options.

        Let our map server calculate the actual polylines for connecting the visits. Processing will take longer.  # noqa: E501

        :param polylines: The polylines of this Options.  # noqa: E501
        :type: bool
        """

        self._polylines = polylines

    @property
    def time_unit(self):
        """Gets the time_unit of this Options.  # noqa: E501

        Calculate in minutes or seconds. Minutes is advised.  # noqa: E501

        :return: The time_unit of this Options.  # noqa: E501
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this Options.

        Calculate in minutes or seconds. Minutes is advised.  # noqa: E501

        :param time_unit: The time_unit of this Options.  # noqa: E501
        :type: str
        """
        allowed_values = ["MINUTES", "SECONDS"]  # noqa: E501
        if time_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `time_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(time_unit, allowed_values)
            )

        self._time_unit = time_unit

    @property
    def force_type_constraints(self):
        """Gets the force_type_constraints of this Options.  # noqa: E501

        If yes, then the type constraints violations are not allowed. Only do this when you are sure about type definitions.  # noqa: E501

        :return: The force_type_constraints of this Options.  # noqa: E501
        :rtype: bool
        """
        return self._force_type_constraints

    @force_type_constraints.setter
    def force_type_constraints(self, force_type_constraints):
        """Sets the force_type_constraints of this Options.

        If yes, then the type constraints violations are not allowed. Only do this when you are sure about type definitions.  # noqa: E501

        :param force_type_constraints: The force_type_constraints of this Options.  # noqa: E501
        :type: bool
        """

        self._force_type_constraints = force_type_constraints

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Options, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Options):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other