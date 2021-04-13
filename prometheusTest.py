from flask import Flask,Response
from prometheus_client import Counter,Gauge,CollectorRegistry,generate_latest
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



app=Flask(__name__)



counter=Counter('my_target','an test target',['machine_ip'])

registry=CollectorRegistry()
gauge=Gauge('container CPU','read container cpu percent','container_ip',registry=registry)


@app.route('/metrics')
def hello():
    host=HostDocker()
    containers=host.allContainers()
    metrics=[  (con.name,host.contsinerCPUPercent(con)) for con in containers  ]
    for mes in metrics:
        gauge.labels(mes[0],mes[1])
    return Response(generate_latest(gauge),mimetype='text/plain')


@app.route('/')
def test():
    return 'hello'





if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8089,debug=True)
