import tika
import time
from tika import parser


tika.TIKA_SERVER_JAR="file:////tika-server.jar"


def execute_extractor(filename):
    """
    """
    t0 = time.time()
    meta = run_tika(file_path=filename)
    t1 = time.time()
    meta.update({'extract time': t1-t0})
    return meta


def run_tika(file_path):
    """
    """
    meta = parser.from_file(file_path)
    return meta
