import parselmouth

from Voicelab.pipeline.Node import Node
from parselmouth.praat import call
from Voicelab.toolkits.Voicelab.VoicelabNode import VoicelabNode


###################################################################################################
# MEASURE Energy NODE
# WARIO pipeline node for measuring the duration of a voice.
###################################################################################################
# ARGUMENTS
# 'voice'   : sound file generated by parselmouth praat
###################################################################################################
# RETURNS
# 'energy'  : RMS amplitude, similar to ENERGY in Voice Sauce
###################################################################################################


class MeasureEnergyNode(VoicelabNode):
    def __init__(self, *args, **kwargs):
        """
        Args:
            *args:
            **kwargs:
        """
        super().__init__(*args, **kwargs)

        self.args = {"start": 0, "end": 0}  # 0 means select all

    ###############################################################################################
    # process: WARIO hook called once for each voice file.
    ###############################################################################################

    def process(self):
        """energy"""
        try:
            sound = self.args["voice"]
            start = self.args["start"]
            end = self.args["end"]
            energy = call(sound, "Get root-mean-square", start, end)
            return {"Energy": energy}
        except:
            return {"Energy": "Measurement failed"}
