#!/usr/bin/env python2

from setuptools import setup

setup(name='KismetCaptureRtlamr',
      version='2018.0.0',
      description='Kismet rtlamr datasource',
      author='Russ Handorf / @dntlookbehindu',
      author_email='russell@handorf.com',
      url='https://www.handorf.com/',
      install_requires=['protobuf', 'KismetExternal'],
      packages=['KismetCaptureRtlamr'],
      scripts=['kismet_cap_sdr_rtlamr', 'kismet_cap_sdr_rtlamr_mqtt'],
     )


