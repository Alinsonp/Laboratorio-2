import folium
from folium.plugins import MarkerCluster
from folium.map import Marker
from jinja2 import Template
from template import HTML

click_template = """{% macro script(this, kwargs) %}
    var {{ this.get_name() }} = L.marker(
        {{ this.location|tojson }},
        {{ this.options|tojson }}
    ).addTo({{ this._parent.get_name() }}).on('click', onClick);
{% endmacro %}"""

# Change template to custom template
Marker._template = Template(click_template)

m = folium.Map()

click_js = """function onClick(e) {
                 console.log(e);
                 }"""

e = folium.Element(click_js)
html = m.get_root()
html.script.get_root().render()
html.script._children[e.get_name()] = e

marker_cluster = MarkerCluster().add_to(m)
folium.plugins.LocateControl(auto_start=True).add_to(m)

def add_markers(graph):
    for dic in graph.nodes:
        __add_marker(dic.Source_Airport_Latitude, dic.Source_Airport_Longitude, dic.Source_Airport_Name, dic)
    return m


def __add_marker(lat, lon, name, dic):
    html = f"""
          <b>Airport:</b></br>
          <code>{dic.Source_Airport_Code}</code>
          <p>{name}</p>
          <p>{dic.Source_Airport_City}</p>
          <p>{dic.Source_Airport_Country}</p>
          <code>{dic.Source_Airport_Latitude}</code>
          <code>{dic.Source_Airport_Longitude}</code>
        """
        
    a = folium.Marker(location=[lat, lon], popup=HTML(dic), icon=folium.Icon(color='blue', icon='plane', prefix='fa'), tooltip="Click me!").add_to(marker_cluster)


def aristas(lat1, lon1, lat2, lon2, code1, code2):
    folium.PolyLine(
    #smooth_factor=50,
    locations=[[lat1, lon1], [lat2, lon2]],
    color="grey",
    tooltip=code1 + " - " + code2,
    weight=2,
    ).add_to(m)


def show_in_browser():
    m.show_in_browser()


def location(lat, lon):
    radius = 50
    folium.CircleMarker(
        location=[lat, lon],
        radius=radius,
        color="cornflowerblue",
        stroke=False,
        fill=True,
        fill_opacity=0.6,
        opacity=1,
        popup="{} pixels".format(radius),
        tooltip="I am in pixels",
    ).add_to(m)

def conexion():
    folium.PolyLine(
    #smooth_factor=50,
    locations=[[64.81510162, -147.8560028],[ 66.04109955 ,66.04109955]],
    color="grey",
    tooltip="HUS - FAI",
    weight=2,
    ).add_to(m)
