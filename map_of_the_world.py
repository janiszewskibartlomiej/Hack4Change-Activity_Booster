import folium
from folium import DivIcon
from data_processing import DataProcessing


class CreatingMap:
    def __init__(self):
        pass

    def map_of_the_world(self):
        title = "Hack4Change: Join a meeting"

        cases_map = folium.Map(
            location=[52.0, 20.0],
            width="99%",
            height="99%",
            left="0%",
            top="0%",
            zoom_start=6.5,
            max_zoom=9,
            min_zoom=5,
            titles=title,
            attr="attribution",
        )

        folium.map.Marker(
            [54.0, 26.0],
            icon=DivIcon(
                icon_size=(280, 600),
                icon_anchor=(200, 40),
                html=f'<div style="background-color:rgba(255, 255, 255, 0.4);">'
                     f'<center><div style="color: black; padding-top:2px;"><h4>{title}</h4></div>'
                     '<br>'
                     f'<b style="font-size:13px;"><img src="./templates/image4690-1.png" alt="Logo" width="100px"></b>'
                     '<br>'
                     '<br>'
                     f'<h4 style="color: black;">Total meetups: <b> {10}</b></h4>'
                     '<br>'
                     f'<div style=" display: flex; justify-content: space-around">'
                     f'<button class="btn btn-primary btn-sm" type="button" style=" padding: 8px 8px; font-size:15px;" onclick=window.open("/new-meetup")>{chr(128200)} New mettup</button></center>'
                     '<br>'
                     f"</div>",
            ),
        ).add_to(cases_map)

        data = DataProcessing().get_all_towns()
        # print(data)
        for row in data:
            coordinates = DataProcessing().slice_location(row[2])
            folium.Marker(
                location=[coordinates[1], coordinates[0]],
                popup=folium.Popup(
                    html=f"""<div style="opacity:1.3;">
                </br>
                Confirmed: <b><center><p style="color:red;  font-size:14px; margin-block-start: 0.6em;">{chr(127973)} {0}</p></center></b>
                Deaths: <b><center><p style="color:black; font-size:14px; margin-block-start: 0.6em;">{chr(10015)} {0}</p></center></b>
                Recovered: <b><center><p style="color:green; font-size:14px; margin-block-start: 0.6em;">{chr(128154)} {0}</p></center></b>
                <center><button type="button" class="btn btn-primary btn-sm" style=" padding: 5px; line-height: 1;" onclick=window.open("/graph={0}")>{chr(128200)} total</button></center>
                <center><button type="button" class="btn btn-primary btn-sm" style=" padding: 5px; line-height: 1; border-color: red; margin-block-start: 0.9em;     border-width: 2px;" onclick=window.open("/graph-diff={0}")>{chr(128200)} per day</button></center>
                         </div>""",
                    max_width=150,
                ),
                icon=folium.Icon(
                    color="green",
                    icon="certificate",
                    html="position: absolute; z-index: 1",
                ),
                tooltip=f"""
                <center>Click me</center>
                         """,
                ).add_to(cases_map)

            color = "yelow"

            folium.CircleMarker(
                location=[coordinates[1], coordinates[0]],
                radius=10,
                color=f"{color}",
                fill=True,
                fill_color=f"{color}",
                ).add_to(cases_map)

        cases_map.save("index.html")  # only for github


if __name__ == '__main__':
    CreatingMap().map_of_the_world()
