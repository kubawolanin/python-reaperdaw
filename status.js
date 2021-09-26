function _toConsumableArray(arr) {
  return (
    _arrayWithoutHoles(arr) ||
    _iterableToArray(arr) ||
    _unsupportedIterableToArray(arr) ||
    _nonIterableSpread()
  );
}

function _nonIterableSpread() {
  throw new TypeError(
    "Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
  );
}

function _unsupportedIterableToArray(o, minLen) {
  if (!o) return;
  if (typeof o === "string") return _arrayLikeToArray(o, minLen);
  var n = Object.prototype.toString.call(o).slice(8, -1);
  if (n === "Object" && o.constructor) n = o.constructor.name;
  if (n === "Map" || n === "Set") return Array.from(o);
  if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))
    return _arrayLikeToArray(o, minLen);
}

function _iterableToArray(iter) {
  if (
    (typeof Symbol !== "undefined" && iter[Symbol.iterator] != null) ||
    iter["@@iterator"] != null
  )
    return Array.from(iter);
}

function _arrayWithoutHoles(arr) {
  if (Array.isArray(arr)) return _arrayLikeToArray(arr);
}

function _arrayLikeToArray(arr, len) {
  if (len == null || len > arr.length) len = arr.length;
  for (var i = 0, arr2 = new Array(len); i < len; i++) {
    arr2[i] = arr[i];
  }
  return arr2;
}

var playState = {
  0: "stopped",
  1: "playing",
  2: "paused",
  5: "recording",
  6: "recordpaused",
};

var trackFlags = function trackFlags(field) {
  var flags = [];

  if (field & 1) {
    flags.push("folder");
  }

  if (field & 2) {
    flags.push("selected");
  }

  if (field & 4) {
    flags.push("has FX");
  }

  if (field & 8) {
    flags.push("muted");
  }

  if (field & 16) {
    flags.push("soloed");
  }

  if (field & 32) {
    flags.push("solo-in-place");
  }

  if (field & 64) {
    flags.push("record armed");
  }

  if (field & 128) {
    flags.push("record monitoring on");
  }

  if (field & 256) {
    flags.push("record monitoring auto");
  }

  return flags;
};

var parse = function parse(payload) {
  var tracks = [];
  var array = payload
    .split("\n")
    .filter(Boolean)
    .map(function (line) {
      var token = line.trim().split("\t");

      switch (token[0]) {
        case "NTRACK":
          return {
            number_of_tracks: Number(token[1]),
          };

        case "TRANSPORT":
          return {
            transport: {
              playstate: playState[Number(token[1])],
              position_seconds: token[2],
              repeat: Boolean(token[3]),
              position_string: token[4],
              position_string_beats: token[5],
            },
          };

        case "BEATPOS":
          return {
            beatpos: {
              playstate: playState[Number(token[1])],
              position_seconds: token[2],
              full_beat_position: token[3],
              measure_cnt: token[4],
              beats_in_measure: token[5],
              time_signature: ""
                .concat(Number(token[6]), "/")
                .concat(Number(token[7])),
            },
          };

        case "CMDSTATE":
          if (token[1] === "40364") {
            return {
              metronome: Boolean(Number(token[2])),
            };
          } else if (token[1] === "1157") {
            return {
              repeat: Boolean(Number(token[2])),
            };
          }

        case "TRACK":
          tracks.push({
            index: Number(token[1]),
            name: token[2],
            flags: trackFlags(Number(token[3])),
            volume: token[4],
            pan: token[5],
            last_meter_peak: token[6],
            last_meter_pos: token[7],
            width_pan2: token[8],
            panmode: token[9],
            sendcnt: token[10],
            recvcnt: token[11],
            hwoutcnt: token[12],
            color: token[13],
          });
          return false;
      }
    });
  return Object.assign.apply(
    Object,
    [
      {
        tracks: tracks,
      },
    ].concat(_toConsumableArray(array))
  );
};
