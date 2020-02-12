from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


def qos_policy_name(conn, id_, required=True):
    """Fetch name of QoS Policy identified by ID `id_`. Use OpenStack SDK
    connection `conn` to fetch the info. If `required`, ensure the
    fetch is successful.

    Returns: the name, or None if not found and not `required`

    Raises: openstack's ResourceNotFound when `required` but not found
    """
    return _fetch_name(conn.network.find_qos_policy, id_, required)


def qos_policy_id(conn, name, required=True):
    """Fetch ID of QoS Policy identified by name `name`. Use OpenStack SDK
    connection `conn` to fetch the info. If `required`, ensure the
    fetch is successful.

    Returns: the ID, or None if not found and not `required`

    Raises: openstack's ResourceNotFound when `required` but not found
    """
    return _fetch_id(conn.network.find_qos_policy, name, required)


def _fetch_name(get_method, id_, required=True):
    """Use `get_method` to fetch an OpenStack SDK resource by `id_` and
    return its name. If `required`, ensure the fetch is successful.

    Returns: the ID, or None if not found and not `required`

    Raises: openstack's ResourceNotFound when `required` but not found
    """
    if id_ is not None:
        return get_method(id_, ignore_missing=not required)['name']


def _fetch_id(get_method, name, required=True):
    """Use `get_method` to fetch an OpenStack SDK resource by `name` and
    return its ID. If `required`, ensure the fetch is successful.

    Returns: the ID, or None if not found and not `required`

    Raises: openstack's ResourceNotFound when `required` but not found
    """
    if name is not None:
        return get_method(name, ignore_missing=not required)['id']