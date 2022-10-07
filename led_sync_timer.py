import time 
import enum
from flask import Flask, request, render_template

class TurnStatus(enum):
    OPEN = 1,
    CLOSED = 2,
    SCORING = 3

reference_time_ns = 0 # ns
turn_status = TurnStatus.READY
team_info_dict = {}

class TeamInfo:
    def __init__(self, team_id, device_time_ns) -> None:
        self.team_id = team_id
        self.device_time_ns = device_time_ns
        self.time_offset = device_time_ns - reference_time_ns

app = Flask(__name__)

def getNanoSeconds(seconds: int) -> int:
    return seconds * 1000000000


@app.route('/')
@app.route('/hello')
def hello():
    return 'hello world'
    
@app.route("/turn-status", methods=['GET'])
def hello():
    return turn_status

@app.route("/join", methods=['POST'])
def join():
    if turn_status != TurnStatus.OPEN:
        return "尚未開放加入", 400

    team_id = request.args["team_id"]
    device_time_ns = request.args["device_time_ns"]
    if reference_time_ns == 0:
        reference_time_ns = device_time_ns
    team_info_dict[team_id] = TeamInfo(team_id, device_time_ns)

@app.route("/subscribe", methods=['GET'])
def subscribe():
    if turn_status != TurnStatus.CLOSED:
        return "還沒封盤，請稍候", 400
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
