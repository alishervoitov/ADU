#!/usr/bin/env python3

import multiprocessing
import os


# Server socket
bind = "0.0.0.0:8000"
backlog = 2048


# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2
max_requests = 1000
max_requests_jitter = 50


# Logging
accesslog = "/var/www/adu/logs/gunicorn_access.log"
errorlog = "/var/www/adu/logs/gunicorn_error.log"
loglevel = "info"


# Process naming
proc_name = "adu_gunicorn"


# Server mechanics
preload_app = True
daemon = False
pidfile = "/var/www/adu/gunicorn.pid"
user = "www-data"
group = "www-data"
tmp_upload_dir = None


# SSL
keyfile = None
certfile = None
