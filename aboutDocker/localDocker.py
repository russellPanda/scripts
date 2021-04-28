import docker
from docker.models.containers import Container


# https://docs.docker.com/engine/api/v1.41/#operation/ContainerStats


class HostDocker:
    def __init__(self) -> None:
        self.client = docker.from_env()

    def all_containers(self):
        return self.client.containers.list()

    def get_container(self, container_id: str):
        return self.client.containers.get(container_id)

    @staticmethod
    def container_cpu_percent(con: Container):
        stats_dict = con.stats(stream=False)
        cpu_delta = stats_dict['cpu_stats']['cpu_usage']['total_usage'] - stats_dict['precpu_stats']['cpu_usage']['total_usage']
        system_cpu_delta = stats_dict['cpu_stats']['system_cpu_usage'] - stats_dict['precpu_stats']['system_cpu_usage']
        number_cpus = stats_dict['cpu_stats']['online_cpus']
        return (cpu_delta / system_cpu_delta) * number_cpus * 100.0
