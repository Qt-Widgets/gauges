PyQt5 + Autobahn/Twisted Gauges Demo
====================================

PyQt5 + Autobahn/Twisted version of the Crossbar Gauges demo_ using Python 2.

Download with::

   $ git clone git@github.com:estan/gauges.git

Install with::

   $ virtualenv2 --system-site-packages ~/demo_env
   $ source ~/demo_env/bin/activate
   $ cd gauges
   $ pip install -e .

Run against the Crossbar demo router with::

   $ gauges-qt --url wss://demo.crossbar.io/ws

Screenshot
----------

.. image:: https://raw.githubusercontent.com/estan/gauges/master/screenshot.png
    :alt: Screenshot of the demo client
    :align: center

.. _demo: https://demo.crossbar.io/gauges/index.html
