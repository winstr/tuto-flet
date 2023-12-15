import flet as ft

from lib.user_controls import VideoStreamer
from lib.navigation_rail import get_navigation_rail


def main(page: ft.Page):

    container = ft.Container()

    s = 2
    for i in range(0, s):
        row = ft.Row(expand=True)
        for j in range(0, s):
            col = ft.Column(expand=True)

    """
    rtsp = 'rtsp://192.168.1.101:554/profile2/media.smp'
    page.add(
        ft.Row(
            controls=[
                get_navigation_rail(),
                ft.VerticalDivider(width=1),
                VideoStreamer(rtsp)
            ],
            expand=True,
        ),
    )
    """


if __name__ == '__main__':
    ft.app(target=main, )
