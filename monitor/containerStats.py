#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 20:28
# @Author  : russell
# @File    : containerStats.py
import docker
from docker.models.containers import Container

# https://docs.docker.com/engine/api/v1.41/#operation/ContainerStats



class HostDocker():
    def __init__(self):
        self.client=docker.from_env()

    def allContainers(self):
        return self.client.containers.list()

    def getContainer(self,container_id:str):
        return self.client.containers.get(container_id)

    def contsinerCPUPercent(self,con:Container):
        stats = con.stats(stream=False)
        cpu_delta = stats['cpu_stats']['cpu_usage']['total_usage'] - \
                    stats['precpu_stats']['cpu_usage']['total_usage']
        system_cpu_delta = stats['cpu_stats']['system_cpu_usage'] - \
                           stats['precpu_stats']['system_cpu_usage']
        number_cpus = stats['cpu_stats']['online_cpus']
        return (cpu_delta / system_cpu_delta) * number_cpus * 100.0

