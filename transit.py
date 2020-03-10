import nyct_pb2
import requests

from secret import TRANSIT_API_KEY

class Transit:
  def __init__(self):
    line_id  = "16"
    api_key  = TRANSIT_API_KEY
    self.url = f"https://datamine.mta.info/mta_esi.php?key={api_key}&feed_id={line_id}"
    self.stop_id = "R05"
    self.transit = self.get_transit()
    self.process_transit()

  def get_transit(self):
    with open('transit.proto', 'rb') as wfile:
      return wfile.read()
    """
    self.transit = requests.get(self.url)
    with open('transit.proto', 'wb') as wfile:
      wfile.write(self.transit.content)
    """

  def process_transit(self):
    from google.transit import gtfs_realtime_pb2
    self.feed = gtfs_realtime_pb2.FeedMessage()
    self.feed.ParseFromString(self.transit)
    from protobuf_to_dict import protobuf_to_dict
    self.transit_dict = protobuf_to_dict(self.feed)
    pass


if __name__=="__main__":
  t = Transit()
  import pdb;pdb.set_trace()
