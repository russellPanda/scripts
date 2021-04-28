# @Time : 2021/4/27
# @Author : russell
# @File : fabricTest.py

# -*- coding: utf-8 -*-

from fabric import Connection

from handleFile.handleYaml import HandleYaml
from handleFile.handlefile import read_file_lines
from io import StringIO, BytesIO

remote_host_config = HandleYaml(path="aboutHost/remoteHost.yml").data[0]


def sh_cmd(host_info: dict, work_path: str, cmd: str, time_out: int):
    result = None
    try:
        with Connection(**host_info) as conn:
            conn.cd(path=work_path)
            result = conn.run(command=cmd, warn=True, hide=True, timeout=time_out)

    except Exception as e:
        print(f'remote host:{host_info},{e}')

    finally:
        return result


def sh_local_scripts(host_info: dict, work_path: str, local_script: str, time_out: int):
    result = None
    try:
        with Connection(**host_info) as conn:
            conn.cd(path=work_path)
            cmd = f"sh {local_script}"
            result = conn.run(command=cmd, warn=True, hide=True, timeout=time_out)

    except Exception as e:
        print(f'remote host:{host_info},{e}')

    finally:
        return result


def sh_local_lines(host_info: dict, work_path: str, local_script: str, time_out: int):
    results = None
    try:
        with Connection(**host_info) as conn:
            conn.cd(path=work_path)
            lines = read_file_lines(path=local_script)
            results = []
            for line in lines:
                results.append(conn.run(command=line, warn=True, hide=True, timeout=time_out))
    except Exception as e:
        print(f'remote host:{host_info},{e}')
    finally:
        return results


def sh_remote_lines(host_info: dict, work_path: str, remote_script: str, time_out: int):
    results = None
    try:
        with BytesIO() as fd:
            with Connection(**remote_host_config) as conn:
                conn.cd(path=work_path)
                conn.get(remote_script, local=fd)
                lines = fd.getvalue().decode().splitlines()
                results = []
                for line in lines:
                    results.append(conn.run(command=line, warn=True, hide=True, timeout=time_out))
    except Exception as e:
        print(f'remote host:{host_info},{e}')
    finally:
        return results
