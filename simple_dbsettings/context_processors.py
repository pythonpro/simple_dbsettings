import simple_dbsettings


def config(request):
    return {"simple_dbsettings": simple_dbsettings.config}
