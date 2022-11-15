from . import ConicalSlicerExtension


def getMetaData():
    return {}


def register(app):
    return {"extension": ConicalSlicerExtension.ConicalSlicerExtension()}