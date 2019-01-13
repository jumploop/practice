#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import logging.config

def main():
    # Configure the logging system
    logging.config.fileConfig('logconfig.ini')