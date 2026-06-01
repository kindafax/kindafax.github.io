=============
WebSocket API
=============

Understanding WebSockets
========================

A WebSocket is communication protocol that allow two-way communication, using only a single TCP connection.
KindaFax uses the WebSocket protocol to allow real-time, low latency communication between clients and the server.

Other than KindaFax, WebSockets are often used for real-time applications like:

- Muliplayer Games.
- Live Notifications.
- Live Dashboards.
- Streaming Data Feeds.

WebSockets are fully compatible with HTTP(S) connections. When connecting to WebSocket with HTTP(S), the server will instruct
the client to change to a WebSocket connection using the ``Upgrade`` header.
Below are examples, on how to start a WebSocket connection in a client application:

.. tab-set::

    .. tab-item:: Javascript

        .. literalinclude:: /_code_examples/websocket_connection.js
            :language: javascript
            :linenos:
    
    .. tab-item:: Python

        .. literalinclude:: /_code_examples/websocket_connection.py
            :language: python
            :linenos:

See Also
========

.. toctree::
   :glob:

   *