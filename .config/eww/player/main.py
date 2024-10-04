import dbus
import requests
from PIL import Image
from io import BytesIO

def get_current_track_cover():
    session_bus = dbus.SessionBus()
    
    # Получаем список всех доступных медиаплееров
    players = session_bus.list_names()
    mpris_players = [name for name in players if name.startswith('org.mpris.MediaPlayer2.')]

    if not mpris_players:
        print("No MPRIS-compatible media players found")
        return

    # Используем первый найденный медиаплеер
    player_name = mpris_players[0]
    player = session_bus.get_object(player_name, '/org/mpris/MediaPlayer2')
    properties_interface = dbus.Interface(player, 'org.freedesktop.DBus.Properties')
    metadata = properties_interface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
    
    if 'mpris:artUrl' in metadata:
        cover_url = metadata['mpris:artUrl']
        response = requests.get(cover_url)
        img = Image.open(BytesIO(response.content))
        img.show()
    else:
        print("No cover art found")

get_current_track_cover()
