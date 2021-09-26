"""Models for Reaper DAW"""
from collections import ChainMap
from .const import (
    PLAYSTATE_STOPPED,
    PLAYSTATE_PLAYING,
    PLAYSTATE_PAUSED,
    PLAYSTATE_RECORDING,
    PLAYSTATE_RECORDPAUSED,
    FLAG_FOLDER,
    FLAG_SELECTED,
    FLAG_HAS_FX,
    FLAG_MUTED,
    FLAG_SOLOED,
    FLAG_SOLO_IN_PLACE,
    FLAG_RECORD_ARMED,
    FLAG_RECORD_MONITORING_ON,
    FLAG_RECORD_MONITORING_AUTO,
)

playState = {
    0: PLAYSTATE_STOPPED,
    1: PLAYSTATE_PLAYING,
    2: PLAYSTATE_PAUSED,
    5: PLAYSTATE_RECORDING,
    6: PLAYSTATE_RECORDPAUSED,
}

tracks = []


def trackFlags(field: int):
    flags = []
    if field & 1:
        flags.append(FLAG_FOLDER)

    if field & 2:
        flags.append(FLAG_SELECTED)

    if field & 4:
        flags.append(FLAG_HAS_FX)

    if field & 8:
        flags.append(FLAG_MUTED)

    if field & 16:
        flags.append(FLAG_SOLOED)

    if field & 32:
        flags.append(FLAG_SOLO_IN_PLACE)

    if field & 64:
        flags.append(FLAG_RECORD_ARMED)

    if field & 128:
        flags.append(FLAG_RECORD_MONITORING_ON)

    if field & 256:
        flags.append(FLAG_RECORD_MONITORING_AUTO)

    return flags


def processLine(line: str):
    token = line.strip().split("\t")
    name = token[0]

    if(name == "NTRACK"):
        return {"number_of_tracks": int(token[1])}
    elif(name == "TRANSPORT"):
        return {
            "transport": {
                "playstate": playState[int(token[1])],
                "position_seconds": token[2],
                "repeat": bool(token[3]),
                "position_string": token[4],
                "position_string_beats": token[5],
            },
        }
    elif(name == "BEATPOS"):
        return {
            "beatpos": {
                "playstate": playState[int(token[1])],
                "position_seconds": token[2],
                "full_beat_position": token[3],
                "measure_cnt": token[4],
                "beats_in_measure": token[5],
                "time_signature": f"{int(token[6])}/{int(token[7])}",
            },
        }
    elif(name == "CMDSTATE"):
        if (token[1] == "40364"):
            return {"metronome": bool(int(token[2]))}
        elif (token[1] == "1157"):
            return {"repeat": bool(int(token[2]))}
    elif(name == "TRACK"):
        tracks.append({
            "index": int(token[1]),
            "name": token[2],
            "flags": trackFlags(int(token[3])),
            "volume": token[4],
            "pan": token[5],
            "last_meter_peak": token[6],
            "last_meter_pos": token[7],
            "width_pan2": token[8],
            "panmode": token[9],
            "sendcnt": token[10],
            "recvcnt": token[11],
            "hwoutcnt": token[12],
            "color": token[13],
        })
        return False


def parse(payload: str):
    array = payload.split("\n")
    lines = [element for element in array if element]
    processedLines = map(processLine, lines)
    tracksDict = {"tracks": tracks}
    parsed = list(processedLines)
    parsed.append(tracksDict)
    result = [element for element in parsed if element]

    return dict(ChainMap(*result))
