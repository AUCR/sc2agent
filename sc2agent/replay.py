import json
import click
import time
import logging
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class Handler(FileSystemEventHandler):
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def on_any_event(self, event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            result = upload_replay(str(event.src_path), self.api_url, self.api_key)
            logging.info(result)
            if result:
                pass


def upload_replay(file_name, api_url, api_key):
    headers = {'Authorization': 'Bearer ' + api_key}
    with open(file_name, 'rb') as fp:
        file_data = fp.read()
    payload = {'filename': str("sc2replay.SC2Replay"),
               'group_access': 2,
               'description': "APIUpload SC2",
               'classification': 2}
    response = requests.post('{}/api/unum_file_upload/'.format(
        api_url), headers=headers, data=file_data, params=payload)
    test = json.loads(response.text)
    json_result = json.dumps(test, indent=4, sort_keys=True)
    return json_result


directory_help_text = "The desired directory to monitor for sc2 replay json output files."


@click.command()
@click.option("--directory", "-d", envvar='REPLAY_FILE_PATH', help=directory_help_text,  required=True)
@click.option("--api_url", "-apiurl",  envvar='API_URL', help="API URL",  required=True)
@click.option("--api_key", "-apikey",  envvar='API_KEY', help="API OAUTH Key",  required=True)
def sc2_replay_monitor(directory, api_url, api_key):
    """SC2 Agent file monitor function."""
    logging.info("Starting Session Stats Tracker!")
    path = directory
    event_handler = Handler(api_key=api_key, api_url=api_url)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        logging.info("Shutting Down Session Stats Tracker!")
        observer.stop()
    observer.join()

