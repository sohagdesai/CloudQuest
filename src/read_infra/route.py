from . import routeTable

class Route:
    routes = []
    def __init__(self, routes):
        self.routes = routes

def get_routes(creds):
    r = []
    route_table_description = routeTable.get_route_tables (creds).description
    for route_tables in route_table_description['RouteTables']:
        r.append(route_tables['Routes'])
    routes = Route(r)
    return routes