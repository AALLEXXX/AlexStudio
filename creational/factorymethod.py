from abc import ABCMeta, abstractmethod


class Plugin(metaclass=ABCMeta):
    @abstractmethod
    def type(self):
        raise NotImplementedError


class EffectPLugin(Plugin):
    def __init__(self):
        self.type = 'Effect'


class SynthPlugin(Plugin):
    def __init__(self):
        self.type = "Synth"


class Creator:
    @staticmethod
    def Factory(type):
        if type == 'Effect':
            return EffectPLugin()
        elif type == 'Synth':
            return SynthPlugin()
        return None
