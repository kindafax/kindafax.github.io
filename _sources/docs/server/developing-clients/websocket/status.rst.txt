============
Status Codes
============


Successful Messages
===================

Error Messages
==============

``RECEIVER_NOT_FOUND``
----------------------

You cannot send a message to this recipient, as they do not exist.

``SENDER_NOT_FOUND``
--------------------

A confirmation message could be sent, because the user who sent the client no longer exists.

This is a rare status, often caused by a user deletion in the duration between 
the original message being sent, and a confirmation message being sent.
 

``INVALID_MESSAGE_SCHEMA``
--------------------------

The message sent, does not follow the correct schema.

``CLIENT_AUTH_REQUIRED``
------------------------

The 


``TOO_MANY_REQUESTS``
---------------------

``SERVER_ERROR``
----------------

The server is currently unable to handle the request because of an error internally.
This is usually temporary, and often indicates a bug with KindaFax.

Handshake Status Codes (HTTP)
=============================

Codes that may be used during handshake.

.. seealso::

    For reference, 
    `see the full list <https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status>`_
    of HTTP status codes.

.. note::

   Status codes not listed here are not returned by KindaFax server.
   For example, a 503 status code might mean the server is temporary unavailable,
   this status would be returned from a reverse proxy.


101 Switching Protocols
-----------------------

Handshake has been successful and the client can now switch to the WebSocket protocol.


401 Unauthorized
----------------

The client is not authenticated, or provided invalid credentials.


426 Upgrade Required
--------------------

This is often caused when a HTTP request was sent to the WebSocket endpoint, but the
client could not change to the WebSocket protocol. For example, accessing the
endpoint directly in a web browser.


429 Too Many Requests
---------------------

The client has been temporary restricted from connecting for a short period. This
is part of rate limiting and is to prevent abuse.


500 Internal Server Error
-------------------------

The server is currently unable to handle the request because of an error internally.
This is usually temporary, and often indicates a bug with KindaFax.