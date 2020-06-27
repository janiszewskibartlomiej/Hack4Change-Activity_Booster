import folium
from folium import DivIcon
from data_processing import DataProcessing
from connect_to_db import ConnectToDb


class CreatingMap:
    def __init__(self):
        pass

    def map_of_the_world(self):
        title = "Hack4Change: <br> Activity Booster"
        meetup_count = ConnectToDb().select_one_record(query="select count(*) from meetups;", parameter="")
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
                icon_size=(160, 200),
                icon_anchor=(200, 40),
                html=f'<div style="background-color:rgba(255, 255, 255, 0.4);">'
                     f'<center><div style="color: black; padding-top:2px;"><h4>{title}</h4></div>'
                     f'<img src="static/logo.png" alt="Logo" style="width:80px;">'
                     '<br>'
                     f'<h4 style="color: black;">Total meetups: <b style="color: red; padding-bottom:2px;"> {meetup_count[0]}</b></h4>'
                     f"</div>",
            ),
        ).add_to(cases_map)

        data = DataProcessing().get_all_towns()
        meetups = DataProcessing().get_all_meetups()
        # print(data)
        for row in data:
            coordinates = DataProcessing().slice_location(row[2])
            for item in meetups:
                meetup_id = item[1]
                town_id = item[0]
                name_meetup = item[3]
                create_time = item[2]
                if town_id == row[0]:

                    folium.Marker(
                        location=[coordinates[1], coordinates[0]],
                        popup=folium.Popup(
                            html=f"""<div style="opacity:1.3;">
                        <b><center><p style="color:red; font-size:14px;">{row[1]}</p></center></b>
                        <center><p style="color:black; font-size:14px; margin-top:-.9em; margin-bottom:0.2em;">Meetups:</p></center>
                        <center><button type="button" class="btn btn-primary btn-sm" style="padding: 5px; margin-top:3px; margin-bottom: 3px;" onclick=window.open("/meetup={meetup_id}")>{name_meetup}</button></center>
                        <center><button type="button" class="btn btn-primary btn-sm" style="padding: 5px; margin-top:3px; margin-bottom: 3px;" onclick=window.open("/meetup={meetup_id}")>{name_meetup}</button></center>
                        <center><button type="button" class="btn btn-primary btn-sm" style="padding: 5px; margin-top:3px; margin-bottom: 3px;" onclick=window.open("/meetup={meetup_id}")>{name_meetup}</button></center>
                        <center><button type="button" class="btn btn-primary btn-sm" style=" padding: 5px; line-height: 1; border-color: red; margin-block-start: 0.9em;     border-width: 2px;" onclick=window.open("/add-meetup")>{chr(128200)} New meetup</button></center>
                                 </div>""",
                            max_width=140,
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
        cases_map.save("templates/index.html")  # only for github


if __name__ == '__main__':
    CreatingMap().map_of_the_world()
