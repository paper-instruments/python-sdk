"""The supported pyqwest must verify HTTPS against the system CA store."""

from unittest.mock import patch

import tinker._base_client as base_client

from fireworks.training.sdk.patches import _tinker_tls_patch


def test_tinker_default_transport_loads_system_roots():
    with (
        patch.object(_tinker_tls_patch.pyqwest, "HTTPTransport") as native,
        patch.object(_tinker_tls_patch, "AsyncPyqwestTransport") as adapter,
    ):
        transport = base_client._default_pyqwest_transport()

    native.assert_called_once_with(tls_include_system_certs=True)
    adapter.assert_called_once_with(transport=native.return_value)
    assert transport is adapter.return_value
