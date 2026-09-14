"""Backport Tinker's system-CA transport fix while retaining its 0.23.0 API.

pyqwest 0.7+ no longer loads trusted roots in a bare HTTPTransport. Tinker
0.23.3 fixes that, but its ServiceClient API is incompatible with this SDK.
Remove this patch when the supported Tinker version includes the native fix.
"""

import httpx
import pyqwest
import tinker._base_client as base_client
from pyqwest.httpx import AsyncPyqwestTransport


def _default_pyqwest_transport() -> httpx.AsyncBaseTransport:
    return AsyncPyqwestTransport(
        transport=pyqwest.HTTPTransport(tls_include_system_certs=True),
    )


base_client._default_pyqwest_transport = _default_pyqwest_transport
