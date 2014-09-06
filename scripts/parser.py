#!/usr/bin/env python
#-*-coding:utf-8-*-

__author__ = 'ugursogukpinar'

import argparse


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('servername',help='VirtualHost server name')
    parser.add_argument('directory', help='VirtualHost document root')
    parser.add_argument('-g','--git',help='Git repostiroy url to clone given directory',default=False)
    parser.add_argument('-cf','--conf',help='VirtualHosts configuration file path',default=False)
    parser.add_argument('-h','--host', action="store_true" , help='With this option you can insert your server name into hosts file.',default=False)
    args = parser.parse_args()
    return args


