from . import ConicalSlicingExtension


def getMetaData():
    return {}


def register(app):
    return {"extension": ConicalSlicingExtension.ConicalSlicingExtension()}